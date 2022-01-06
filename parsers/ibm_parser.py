import pandas as pd

from bs4 import BeautifulSoup


qa = []

filename = "../data/raw/ibm.html"

with open(filename, "r") as fd:
    soup = BeautifulSoup(fd, "html.parser")

    root_div = soup.find("div", class_="docs--FaqList")
    for title_div in root_div.find_all("div", class_="bx--accordion__title"):

        if not title_div:
            continue

        question = title_div.text

        if not question or "?" not in question:
            continue

        content_div = title_div.parent.find_next_sibling(
            "div", class_="bx--accordion__content"
        )
        if not content_div:
            continue

        answer = content_div.text

        if question and answer:
            qa.append(
                {"question": question, "answer": answer, "source": "ibm",}
            )

print(len(qa))

df = pd.DataFrame(qa)
df.to_csv("../data/processed/ibm_processed.csv")
