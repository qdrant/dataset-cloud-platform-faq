import re

from pathlib import Path

import pandas as pd

from bs4 import BeautifulSoup


qa = []

dir_content = Path('../data/raw/azure/faq').glob('*.html')
# dir_content = sorted(list(dir_content))

for filepath in dir_content:
    filename = str(filepath).replace('../data/raw/azure/faq/', '').replace('.html', '')
    print(filename)
    local_qa = []
    with open(filepath, "r") as fd:
        soup = BeautifulSoup(fd, "html.parser")
        root_div = soup.find('main', class_="content")
        if not root_div:
            print('NOT ROOT DIV: ', filename)
            continue

        questions = soup.find_all(['h1', 'h2', 'h3', 'h4'], string=re.compile(".+\?"))
        for question_elem in questions:

            question = question_elem.text
            if '?' not in question:
                continue

            answer_elem = question_elem.find_next_sibling('p')

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
                        "source": "azure",
                        "filename": filename
                    }
                )
    qa.extend(local_qa)
    print(len(local_qa), len(qa))


print(len(qa))

df = pd.DataFrame(qa)
df.to_csv(f"../data/processed/azure_processed.csv")