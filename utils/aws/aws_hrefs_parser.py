from bs4 import BeautifulSoup

#  https://aws.amazon.com/faqs/?nc1=h_ls

origin_links = set()
augmented_links = set()
filename = "../../data/raw/aws/aws_main.html"
with open(filename, "r") as fd:
    soup = BeautifulSoup(fd, "html.parser")

    root_div = soup.find("div", class_="row column-builder")
    for a in root_div.find_all("a"):
        if not a:
            continue

        link = a.attrs.get('href')
        if link:
            link = link.replace('features/#FAQs', 'faqs').replace('product-details/#FAQs', 'faqs')
            if 'https' not in link:
                link = 'https://aws.amazon.com' + link
                augmented_links.add(link)
            else:
                origin_links.add(link)

print(origin_links)
print(augmented_links)
print(len(origin_links))
print(len(augmented_links))

with open('../../data/raw/aws/aws_links.txt', 'w') as fd:
    fd.write("\n".join(list(origin_links)))
    fd.write('\n')
    fd.write("\n".join(list(augmented_links)))
