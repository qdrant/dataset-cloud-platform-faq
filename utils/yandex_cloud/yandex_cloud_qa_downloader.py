import os
import requests

if not os.path.exists("../../data/raw/yandex_cloud/faq"):
    os.mkdir("../../data/raw/yandex_cloud/faq")

with open("../../data/raw/yandex_cloud/yandex_cloud_qa_links.txt", "r") as fd:
    link = fd.readline().strip()
    while link:
        page = requests.get(link)
        truncated_link = (
            link.replace("", "")
            .replace("https://cloud.yandex.com/en/", "")
            .replace("/", "_")
        )
        if truncated_link[-1] == "_":
            truncated_link = truncated_link[:-1]
        print(truncated_link)

        with open(
            "../../data/raw/yandex_cloud/faq/" + truncated_link + ".html", "w"
        ) as n_fd:
            n_fd.write(page.text)
        link = fd.readline().strip()
