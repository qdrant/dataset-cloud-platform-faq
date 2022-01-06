import re

from pathlib import Path

import pandas as pd

from bs4 import BeautifulSoup


qa = []

dir_content = Path('../data/raw/yandex_cloud/faq').glob('*')
for filepath in dir_content:
    filename = str(filepath).replace('../data/raw/yandex_cloud/faq/', '').replace('.html', '')
    print(filename)
    local_qa = []
    with open(filepath, "r") as fd:
        soup = BeautifulSoup(fd, "html.parser")
        # questions = soup.find_all("p", string=re.compile("(Q:|Q\.).+"))

        # it also can be "a", or in case of "a" it just hides "p" ?
        questions = soup.find_all("h4")
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

            print('question: ', question)
            print('answer: ', answer_elem.text)
            if question and answer:
                local_qa.append(
                    {
                        "question": question,
                        "answer": answer,
                        "source": "yandex_cloud",
                        "filename": filename
                    }
                )
    qa.extend(local_qa)
    print(len(local_qa), len(qa))


print(len(qa))

df = pd.DataFrame(qa)
df.to_csv(f"../data/processed/yandex_cloud_processed.csv")