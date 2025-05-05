#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
from pathlib import Path
import requests


def main():
    urls = [
            ("https://hackmd.io/@CSCBioMaria/ByS0nTrTh",
                "csc-enveff-20230919"),
            ("https://hackmd.io/@CSCBioMaria/Bk00RUSdp#",
                "csc-enveff-20240207"),
            ("https://hackmd.io/@CSCBioMaria/enveffapril2024",
                "csc-enveff-20240424"),
            ("https://hackmd.io/@CSCBioMaria/enveffmay2024",
                "csc-enveff-20240515"),
            ("https://hackmd.io/@CSCBioMaria/rkcTtCUaR",
                "csc-enveff-20241003"),
            ("https://hackmd.io/@CSCBioMaria/part2Nov24",
                "csc-enveff-20241107"),
            ]

    base_dir = Path("./data/raw")
    with requests.Session() as s:
        for url, subdir in urls:
            r = s.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            markdown = soup.find(id="publish-page").get_text()

            output_dir = base_dir / subdir
            os.makedirs(output_dir, exist_ok=True)

            output_file = output_dir / f"{url.split('/')[-1].rstrip('#')}.md"
            with open(output_file, "w") as file:
                file.write(markdown)


if __name__ == "__main__":
    main()
