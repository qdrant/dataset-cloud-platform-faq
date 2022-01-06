from bs4 import BeautifulSoup

#  azure

links = set()

filename = "../../data/raw/azure/azure_main.html"
with open(filename, "r") as fd:
    soup = BeautifulSoup(fd, "html.parser")

    root_div = soup.find("div", id="product-cards")
    for a in root_div.find_all("a", class_="is-hidden-tablet is-block has-external-link-indicator"):
        if not a:
            continue

        href = a.attrs.get('href')

        if 'http' in href:
            continue

        if href[0] == '/':
            href = href[1:]
        if href[-1] == '/':
            href = href[:-1]

        print(href)
        if 'en-us' in href:
            prefix = 'https://docs.microsoft.com/'
        else:
            prefix = 'https://docs.microsoft.com/en-us/azure/'

        link = prefix + href
        print(link)
        links.add(link)

with open('../../data/raw/azure/azure_links.txt', 'w') as fd:
    fd.write("\n".join(list(links)))
