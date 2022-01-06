import re
import json

from pathlib import Path
from bs4 import BeautifulSoup


with open("../../data/raw/azure/alias_link_map.json") as fd:
    alias_link_map = json.load(fd)

p = Path("../../data/raw/azure/products").glob("*.html")
links = set()
new_sections = 0
new_nones = 0
for path in p:
    with open(path, "r") as fd:
        split_path = str(path).rsplit("/", 1)
        key = split_path[1].replace(".html", "")
        parent_link = alias_link_map[key]

        soup = BeautifulSoup(fd, "html.parser")
        # region section conceptual content
        if (section := soup.find("section", id="conceptual-content")) :
            for a in section.find_all(
                "a",
                class_="has-external-link-indicator",
                string=re.compile("\.*\?"),
            ):
                href = a.attrs.get("href")
                link = parent_link + "/" + href
                links.add(link)
                # print(link)
        # endregion
        # region section landing content
        elif (section := soup.find("section", id="landing-content")) :

            new_sections += section is not None
            new_nones += section is None
            if section:
                for a in section.find_all(
                    "a",
                    class_="has-external-link-indicator",
                    string=re.compile("\.*\?"),
                ):
                    href = a.attrs.get("href")
                    if 'http' not in href:
                        link = parent_link + "/" + href
                    else:
                        link = href
                    links.add(link)

        # endregion

print(len(links))

with open("../../data/raw/azure/azure_article_links.txt", "w") as fd:
    fd.write("\n".join(list(links)))
