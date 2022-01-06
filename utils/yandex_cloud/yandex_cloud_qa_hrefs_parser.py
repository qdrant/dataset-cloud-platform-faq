import re

from pathlib import Path

from bs4 import BeautifulSoup


p = Path('../../data/raw/yandex_cloud/products').glob('*.html')
links = set()

for path in p:
    with open(path, 'r') as fd:
        soup = BeautifulSoup(fd, 'html.parser')
        a_iter = soup.find_all('a', href=re.compile('.*/qa.*'))
        for a in a_iter:
            href = a.attrs.get('href')
            if 'all' in href:
                continue
            link = 'https://cloud.yandex.com/en' + href
            links.add(link)
            print(link)
print(len(links))
with open('../../data/raw/yandex_cloud/yandex_cloud_qa_links.txt', 'w') as fd:
    fd.write("\n".join(list(links)))
