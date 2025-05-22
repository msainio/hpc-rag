from llama_index.vector_stores.qdrant import QdrantVectorStore
from markdown.inlinepatterns import BACKTICK_RE, AUTOLINK_RE, AUTOMAIL_RE
from markdown.inlinepatterns import HTML_RE
from nltk.corpus import brown
from qdrant_client import AsyncQdrantClient, QdrantClient
import random
import re
import warnings

host_map = {
    "csc-env-eff/_slides": (
        "https://a3s.fi/CSC_training"
        ),
    "csc-env-eff": (
        "https://csc-training.github.io/csc-env-eff"
        ),
    "csc-user-guide/docs": (
        "https://docs.csc.fi"
        ),
    "LUMI-EasyBuild-docs/docs-generated/docs": (
        "https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs"
        ),
    "lumi-userguide/docs": (
        "https://docs.lumi-supercomputer.eu"
        ),
    }


def clean_markdown(text):
    link_definition = r"^\s*\[[^\]]*\]: [^\s]+$"
    link_reference = r"\!?\[+([^\]]*)\]+(\([^\)]*\)|\[[^\]]*\])?(\{[^\}]*\})?"
    in_metadata = False
    in_code_block = False
    in_comment = False

    new_lines = []
    for line in text.split("\n"):
        if line.startswith("```"):
            in_code_block = not in_code_block

        if line == "---":
            in_metadata = not in_metadata
            continue

        if line == "<!--":
            in_comment = True
            continue
        if line == "-->":
            in_comment = False
            continue

        old_line = line

        if not in_code_block and not in_comment:
            # Do not apply substitutions inside code blocks
            # Inside comments it is just unnecessary
            backtick_strings = re.findall(BACKTICK_RE, line)

            for pattern in [link_definition, link_reference, AUTOLINK_RE, AUTOMAIL_RE, HTML_RE]:
                backtick_matches = []
                for triple in backtick_strings:
                    backtick_matches.extend(re.findall(pattern, triple[2]))

                for match in re.findall(pattern, line):
                    if match not in backtick_matches:
                        if pattern in {link_definition, HTML_RE}:
                            line = re.sub(pattern, "", line)
                        else:
                            line = re.sub(pattern, r"\1", line)

        if line != old_line and not line.strip():
            # Exclude lines that were not empty but became so
            continue

        if not in_metadata and not in_comment and line.strip():
            new_lines.append(re.sub(r"(\s)+", r"\1", line))

    return "\n".join(new_lines).strip()


def get_url(file_path, permalink):
    """Convert local file paths to URLs using a predefined scheme.
    """
    result = re.search(r"knowledge-base/(.*)", str(file_path.parent))
    local_parent = result.group(1)

    # Get remote hostname based on local file path.
    source = None
    host = None
    for key, value in host_map.items():
        if host is None and re.match(key, local_parent):
            source = key
            host = value

    if host is None:
        warnings.warn(f"Could not find URL for file: '{path}'", stacklevel=2)
        return None

    if source.startswith("csc-env-eff"):
        ext = ".html"
    else:
        ext = "/"

    # Replace local parent path with remote host
    if permalink:
        url = host + permalink
    else:
        remote_parent = re.sub(source, host, local_parent)
        if file_path.name != "index.md":
            name = re.sub(r"\.md", ext, file_path.name)
        else:
            name = ""
        url = remote_parent + "/" + name

    return url


def get_vector_store(collection_name, client_kwargs):
    vector_store = QdrantVectorStore(
            collection_name=collection_name,
            client=QdrantClient(**client_kwargs),
            aclient=AsyncQdrantClient(**client_kwargs),
            )

    return vector_store
