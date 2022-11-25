from bs4 import BeautifulSoup

with open('book.xml', 'r', encoding='utf-8') as xml_file:
    data = xml_file.read()

# print(data)
soup = BeautifulSoup(data, "lxml-xml")
# print(soup.catalog.book.author)
# print(soup.catalog.book["id"])
# print(soup.find('title'))
# print(soup.catalog)
autor = soup("author")
title = soup("title")
print(title[0], autor[0])
print(title[2], autor[2])
print(title[6].text, autor[6].text)
balon = soup("balon")

# for c in soup.catalog:

# print(soup.catalog.book.author)
# print(type(c))

# for book in catalog:
# print(book)
# print(soup.find("author"))
