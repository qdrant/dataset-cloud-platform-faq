from bs4 import BeautifulSoup

#  hetzner

links = set()
filename = "../../data/raw/hetzner/part_of_main.html"
with open(filename, "r") as fd:
    soup = BeautifulSoup(fd, "html.parser")
    for a in soup.find_all('a', class_="d-inline-flex"):
        href = a.attrs.get('href')
        link = "https://docs.hetzner.com" + href
        links.add(link)

with open('../../data/raw/hetzner/hetzner_links.txt', 'w') as fd:
    fd.write("\n".join(list(links)))
