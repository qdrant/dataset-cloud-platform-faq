import re

from pathlib import Path

import pandas as pd

from bs4 import BeautifulSoup


qa = []

dir_content = Path("../data/raw/gcp/faq").glob("*.html")
for filepath in dir_content:
    filename = (
        str(filepath).replace("../data/raw/gcp/faq/", "").replace(".html", "")
    )
    print(filename)
    local_qa = []
    with open(filepath, "r") as fd:
        soup = BeautifulSoup(fd, "html.parser")
        root_div = soup.find("div", class_="devsite-article-body clearfix")
        if not root_div:
            continue
        # region dt search
        for question_elem in root_div.find_all("dt"):
            question = question_elem.text
            if "?" not in question:
                continue

            answer_elem = question_elem.find_next_sibling("dd")
            if not answer_elem:
                continue

            answer = answer_elem.text.strip()
            if not answer:
                continue

            if answer[-1] == ":":
                continue

            # print('question: ', question)
            # print('answer: ', answer_elem.text)
            if question and answer:
                local_qa.append(
                    {
                        "question": question,
                        "answer": answer,
                        "source": "gcp",
                        "filename": filename,
                    }
                )
        # endregion
        # region p search
        if not local_qa:
            for question_elem in root_div.find_all(
                "p", string=re.compile(".+\?")
            ):
                question = question_elem.text
                if "?" not in question:
                    continue

                answer_elem = question_elem.find_next_sibling("p")
                if not answer_elem:
                    continue

                answer = answer_elem.text.strip()
                if not answer:
                    continue

                if answer[-1] == ":":
                    continue

                # print('question: ', question)
                # print('answer: ', answer_elem.text)
                if question and answer:
                    local_qa.append(
                        {
                            "question": question,
                            "answer": answer,
                            "source": "gcp",
                            "filename": filename,
                        }
                    )
        # endregion
        # region h2, h3, h4
        if not local_qa:
            for question_elem in root_div.find_all(
                ["h2", "h3", "h4"], string=re.compile(".+\?")
            ):
                question = question_elem.text
                if "?" not in question:
                    continue

                answer_elem = question_elem.find_next_sibling("p")
                if not answer_elem:
                    continue

                answer = answer_elem.text.strip()
                if not answer:
                    continue

                if answer[-1] == ":":
                    continue

                # print('question: ', question)
                # print('answer: ', answer_elem.text)
                if question and answer:
                    local_qa.append(
                        {
                            "question": question,
                            "answer": answer,
                            "source": "gcp",
                            "filename": filename,
                        }
                    )
        # endregion
        # region td
        if not local_qa:
            for question_elem in root_div.find_all(
                ["td"], string=re.compile(".+\?")
            ):
                question = question_elem.text
                if "?" not in question:
                    continue

                answer_elem = question_elem.find_next_sibling("td")
                if not answer_elem:
                    continue

                answer = answer_elem.text.strip()
                if not answer:
                    continue

                if answer[-1] == ":":
                    continue

                # print('question: ', question)
                # print('answer: ', answer_elem.text)
                if question and answer:
                    local_qa.append(
                        {
                            "question": question,
                            "answer": answer,
                            "source": "gcp",
                            "filename": filename,
                        }
                    )
        # endregion
    qa.extend(local_qa)
    print(len(local_qa), len(qa))


print(len(qa))

df = pd.DataFrame(qa)
df.to_csv(f"../data/processed/gcp_processed.csv")





