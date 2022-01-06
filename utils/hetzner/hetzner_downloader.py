import os
import requests

if not os.path.exists("../../data/raw/hetzner/faq"):
    os.mkdir("../../data/raw/hetzner/faq")

with open("../../data/raw/hetzner/hetzner_links.txt", "r") as fd:
    link = fd.readline().strip()
    while link:
        page = requests.get(link)
        truncated_link = (
            link.replace("https://docs.hetzner.com/", "")
            .replace("/", "_")
        )
        if truncated_link[-1] == "_":
            truncated_link = truncated_link[:-1]
        print(truncated_link)

        with open("../../data/raw/hetzner/faq/" + truncated_link + ".html", "w") as n_fd:
            n_fd.write(page.text)
        link = fd.readline().strip()
