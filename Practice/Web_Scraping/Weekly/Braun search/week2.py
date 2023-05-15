from requests_html import HTMLSession
import requests
import pandas as pd

s = HTMLSession()
def create_link(word): # general search
    url = f"https://www.braunshop.co.uk/elysium.search?search={word}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
    r = s.get(url, headers=headers)
    z = r.html.find(".productBlock_imageLinkWrapper > a[href]")
    a = []
    for i in z:
        a.append(i.attrs["href"])
    return a

def print_link(word):
    baseurl = "https://www.braunshop.co.uk"
    b = create_link(word)
    c = []
    for url in b:
        c.append(baseurl + url)
    return c

def data(word):
    e = print_link(word)
    d = {}
    for i in e:
        url = s.get(i)
        #d.append(url.html.find("title", first=True).text)
        #d.append(url.html.find("p[data-product-price=price]", first=True).text)
        d[url.html.find("title", first=True).text] = url.html.find("p[data-product-price=price]", first=True).text
    return d
    print(d)

data("beard")
'''
def main(word):
    #df = pd.DataFrame(data(word))
    dj = pd.DataFrame(data(word))
    dj.to_csv(f"Braun {word} search.csv", index=False)
    print("done.")

if __name__ == "__main__": # creates table and saves to csv
     s = HTMLSession()
     word = input("Enter your single word to search: ")
     main(word)
'''