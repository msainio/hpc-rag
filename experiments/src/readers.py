from llama_index.core import Document
from llama_index.core.readers.base import BaseReader

import lxml.html
import markdown
import os
import re
import requests
from tqdm import tqdm
import warnings

from utils import clean_markdown, get_url


class CustomReader(BaseReader):

    def extract_metadata(self, input_file, md_content):
        # Look for resource permalink in Markdown metadata
        md_parser = markdown.Markdown(extensions=["meta"])
        md_parser.convert(md_content)  # extract metadata

        permalink = None
        if "permalink" in md_parser.Meta.keys():
            permalink = md_parser.Meta["permalink"][0]

        # Get resource URL
        url = get_url(input_file, permalink)

        if url is None:
            return {}

        # Check if resource is available online
        if "LUMI-EasyBuild-docs" in input_file.parts:
            local_path = re.sub(
                    r".*/LUMI-EasyBuild-docs",
                    "data/knowledge-base/LUMI-EasyBuild-docs/gh-pages",
                    url,
                    ) + "index.html"
            if os.path.isfile(local_path):
                with open(local_path) as file:
                    html_content = file.read()
            else:
                return {}
        else:
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                html_content = response.text
            else:
                warnings.warn(f"{url} {status_code}", stacklevel=2)
                return {}

        # Get resource title
        html_doc = lxml.html.fromstring(html_content)
        title = html_doc.find(".//title").text

        return {"doc_title": title, "doc_url": url}

    def load_file(self, input_file, output_format="original"):
        """Reads a Markdown file and returns a LlamaIndex document.

        Since it is important that a RAG system can provide accessible
        references, we generally only want to include resources that are
        hosted online as HTML resources.
        """
        # Read Markdown content
        with open(input_file, encoding="utf-8") as file:
            md_content = file.read()

        # Conversions depending on chosen output format
        if output_format in {"html", "plaintext"}:
            md_parser = markdown.Markdown(
                    extensions=["extra", "admonition", "meta", "toc"])
            html_content = md_parser.convert(md_content)

            if output_format == "html":
                text_resource = html_content
            elif output_format == "plaintext":
                html_doc = lxml.html.fromstring(html_content)
                text_resource = lxml.html.tostring(
                        html_doc, encoding="utf-8", method="text")
        else:
            text_resource = md_content

        # Remove hyperlinks and HTML tags
        text_resource = clean_markdown(text_resource)

        return Document(text=text_resource, metadata={}), md_content

    def get_documents(self, input_files, output_format, show_progress):
        if show_progress:
            iterator = tqdm(input_files, desc="Reading input files",
                    total=len(input_files))
        else:
            iterator = input_files

        tuples = []
        for input_file in iterator:
            tuples.append(self.load_file(input_file))

        return tuples

    def get_metadata(
            self, input_files, documents, is_experiment, md_content,
            only_hosted, show_progress,
            ):
        iterable = zip(input_files, md_content)
        if show_progress:
            iterator = tqdm(iterable, desc="Extracting metadata",
                    total=len(input_files))
        else:
            iterator = iterable

        metadata = []
        for input_file, md_doc in iterator:
            if is_experiment:
                # Although metadata from hosted documents is not used
                # in the experiments, it is retrieved to give a realistic
                # picture of the time required for loading the data.
                _ = self.extract_metadata(input_file, md_doc)
                metadata.append({"file_path": str(input_file)})
            else:
                metadata.append(self.extract_metadata(input_file, md_doc))


        # Enrich documents with metadata
        enriched_documents = []
        for i in range(len(documents)):
            if only_hosted and not metadata[i]:
                continue
            enriched_document = documents[i]
            enriched_document.metadata.update(metadata[i])
            enriched_documents.append(enriched_document)

        return enriched_documents
    
    def load_data(
            self, input_files, output_format="original",
            include_metadata=False, is_experiment=False, only_hosted=False,
            show_progress=False,
            ):
        """Load Markdown data.
        """
        if only_hosted and not include_metadata:
            # Metadata extraction is necessary to ensure files are hosted
            warnings.warn(
                    "'only_hosted' is enabled "
                    "but 'include_metadata' is disabled: "
                    "enabling 'include_metadata'",
                    stacklevel=2
                    )
            include_metadata = True

        # Get read files and return LlamaIndex documents
        tuples = self.get_documents(input_files, output_format, show_progress)

        documents = []
        md_content = []
        for tup in tuples:
            documents.append(tup[0])
            md_content.append(tup[1])

        if not include_metadata:
            return documents
        else:
            return self.get_metadata(
                    input_files, documents, is_experiment, md_content,
                    only_hosted, show_progress,
                    )
