from requests_html import HTMLSession
import chompjs
import pandas as pd

s = HTMLSession()

def fetch(url): # fetches the urls of each product
    url = "https://bicerin.it/negozio/"
    r = s.get(url)
    results = [link.attrs["href"] for link in r.html.find("#fw_c > ul > li > div > a")]
    return list(dict.fromkeys(results))

def parseproduct(url): # extracts all attributes for each product
    r = s.get(url)
    details = r.html.find("script[type=\"application/ld+json\"]", first=True)
    data = chompjs.parse_js_object(details.text)
    return data

def main(): # creates a list for each product
    urls = fetch("https://bicerin.it/negozio/")
    products = list(urls)
    return [parseproduct(url) for url in products]

if __name__ == "__main__": # creates table and saves to csv
     s = HTMLSession()
     df = pd.json_normalize(main())
     df.to_csv("bicerin.csv", index=False)
     print("done.")

