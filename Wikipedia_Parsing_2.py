from Source_Parsing_1 import *
import requests
from bs4 import BeautifulSoup
import re

i = 0
for Title in Titles:

    print("\n\n", i, "\n\n")
    globals()["Data_Page_title" + str(i)] = []
    globals()["Data_heroes_title" + str(i)] = []
    globals()["Data_heroes_Description_Image" + str(i)] = []
    globals()["Data_heroes_Image_URL" + str(i)] = []

    for link in globals()["URL_heroes" + str(i)]:

        print("loading")
        print(link)

        if "http://ru.wikipedia.org" in link:

            req1 = requests.get(link)
            req = req1.text.encode('utf-8')
            soup = BeautifulSoup(req, "lxml")

            # СПУСК ПО ТЕГАМ

            body = soup.find("body")
            mw_body = body.find("div", class_="mw-body")

            Page_title = mw_body.find("h1", class_="firstHeading mw-first-heading").text
            globals()["Data_Page_title" + str(i)].append(Page_title)

            vector_body = mw_body.find("div", class_="vector-body")

            # ДЛЯ ЗАГОЛОВКА САЙТА

            mw_body_content = vector_body.find("div", class_="mw-body-content mw-content-ltr")
            ps = mw_body_content.find_all("p")
            p_text = []

            for p in ps:
                p_text.append(p.text)

            # Дальше я пытаюсь удалить все символы из UTF - 8

            p_text = " ".join(p_text)
            p_text = p_text.replace("\n", "").replace("\xa0—", "").replace("\xa0", "").replace('"', "''")
            p_text = re.sub(r'\[\d+\]', '', p_text)

            text = p_text[:500]
            globals()["Data_heroes_title" + str(i)].append(text)

            # # Парсинг в поисках текста картинки справа ->

            td = soup.find('td', class_="infobox-image")
            try:
                for img in td.findAll('img'):
                    print("[+] ", img['alt'])
                    globals()["Data_heroes_Description_Image" + str(i)].append(img['alt'])
                    img_src_url = "https:" + img['src']
                    print("[+] ", img_src_url)
                    globals()["Data_heroes_Image_URL" + str(i)].append(img_src_url)
            except Exception:
                print("Нет описания картинки", '\n', "Нет картинки")
                globals()["Data_heroes_Description_Image" + str(i)].append("Нет описания картинки в таблице")
                globals()["Data_heroes_Image_URL" + str(i)].append("Нет картинки в таблице")
    i += 1
