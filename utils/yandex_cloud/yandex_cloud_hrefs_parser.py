from bs4 import BeautifulSoup


path = '../../data/raw/yandex_cloud/main_page.html'
links = set()
with open(path, 'r') as fd:
    soup = BeautifulSoup(fd, 'html.parser')
    a_iter = soup.find_all('a', class_='navigation-categorized-item__content')
    for a in a_iter:
        href = a.attrs.get('href')
        link = 'https://cloud.yandex.com/en' + href
        links.add(link)
print(len(links))
with open('../../data/raw/yandex_cloud/yandex_cloud_links.txt', 'w') as fd:
    fd.write("\n".join(list(links)))
