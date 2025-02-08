from bs4 import BeautifulSoup

with open("./dummy.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")

print(doc.prettify)
print(doc.find_all("div"))