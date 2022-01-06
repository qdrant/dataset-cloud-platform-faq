import os
import json

import requests


if not os.path.exists("../../data/raw/azure/products"):
    os.mkdir("../../data/raw/azure/products")

alias_link_map = {}
with open("../../data/raw/azure/azure_links.txt", "r") as fd:
    link = fd.readline().strip()
    while link:
        page = requests.get(link)
        truncated_link = (
            link.replace("https://docs.microsoft.com/", "")
            .replace("en-us/azure/", "")
            .replace("en-us/", "")
            .replace("/", "_")
        )
        if truncated_link[-1] == "_":
            truncated_link = truncated_link[:-1]
        print(truncated_link, link)

        with open("../../data/raw/azure/products/" + truncated_link + ".html", "w") as n_fd:
            n_fd.write(page.text)
        alias_link_map[truncated_link] = link

        link = fd.readline().strip()

with open('../../data/raw/azure/alias_link_map.json', 'w') as fd:
    json.dump(alias_link_map, fd)
