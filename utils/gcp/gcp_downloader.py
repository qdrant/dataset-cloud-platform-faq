import os
import requests

if not os.path.exists("../../data/raw/gcp/faq"):
    os.mkdir("../../data/raw/gcp/faq")


links = []
with open("../../data/raw/gcp/gcp_links.txt", "r") as fd:
    link = fd.readline().strip()
    while link:
        print(link)
        page = requests.get(link)
        com_ind = link.index('.com/')
        truncated_link = link[com_ind + 5:]
        normalized_link = "".join(char if char.isalnum() else '_' for char in truncated_link)

        with open("../../data/raw/gcp/faq/" + normalized_link + ".html", "w") as n_fd:
            n_fd.write(page.text)
        link = fd.readline().strip()

