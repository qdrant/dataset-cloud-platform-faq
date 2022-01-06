import re

from pathlib import Path

import pandas as pd

from bs4 import BeautifulSoup


qa = []

dir_content = Path('../data/raw/hetzner/faq').glob('*')
for filepath in dir_content:
    filename = str(filepath).replace('../data/raw/hetzner/faq/', '').replace('.html', '')
    print(filename)
    local_qa = []

    with open(filepath, "r") as fd:
        soup = BeautifulSoup(fd, "html.parser")
        article = soup.find('article')
        # region header fetch
        for header in article.find_all(['h2', 'h3']):
            if not header:
                continue

            question = header.text

            if '?' not in question:
                continue

            answer_elem = header.find_next_sibling('p')
            if not answer_elem:
                continue

            answer = answer_elem.text.strip()
            if not answer:
                continue

            if answer[-1] == ':':
                continue
            #
            # print('question: ', question)
            # print('answer: ', answer_elem.text)
            if question and answer:
                local_qa.append(
                    {
                        "question": question,
                        "answer": answer,
                        "source": "hetzner",
                        "filename": filename
                    }
                )
        # endregion

        # region p fetch
        questions = article.find_all("p", string=re.compile(".+\?$"))
        for question_elem in questions:
            question = question_elem.text

            if '?' not in question:
                continue

            # always four next?
            answer_elem = question_elem.find_next_sibling('p')
            if not answer_elem:
                continue

            answer = answer_elem.text.strip()
            if not answer:
                continue

            if answer[-1] == ':':
                continue

            if '?' in answer:
                continue

            # print('question: ', question)
            # print('answer: ', answer_elem.text)

            if question and answer:
                local_qa.append(
                    {
                        "question": question,
                        "answer": answer,
                        "source": "hetzner",
                        "filename": filename
                    }
                )
        # endregion
    qa.extend(local_qa)
    print(len(local_qa), len(qa))


print(len(qa))

df = pd.DataFrame(qa)
df.to_csv(f"../data/processed/hetzner_processed.csv")