from requests_html import HTMLSession

s = HTMLSession()

query = "london"
url = f"https://www.google.com/search?q=weather+{query}"

r = s.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9,ar;q=0.8"})

temp = r.html.find("span#wob_tm", first=True).text #uses the # to search for the item name

unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text #uses the space to search for sub category

desc =r.html.find("div.VQF4g", first=True).find("span#wob_dc", first=True).text

print(query,temp,unit,desc)