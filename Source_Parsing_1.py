import requests
from bs4 import BeautifulSoup

req = requests.get("https://ruxpert.ru/Знаменитые_государственные_и_военные_люди_России")
req = req.text.encode('utf-8')

soup = BeautifulSoup(req, "lxml")
span1 = []
spans = soup.findAll('span')

for span in spans:
    span1 += span

target = span1.index(' См. также ')
del span1[target:]
target1 = span1.index(' Государственные и военные люди ')
del span1[:target1+1]
Titles = span1

galleries = soup.find_all("ul", class_="gallery")
i = 0

for gallery in galleries:
    print(Titles[i])
    globals()["URL_heroes" + str(i)] = []
    galleryBoxes = gallery.find_all("li", class_="gallerybox")

    for galleryBox in galleryBoxes:

        URL_hero = galleryBox.find("div").find("div", class_="gallerytext").find("p").find("b").find("a").get("href")
        URL_hero = str(URL_hero)

        if str("http://ru.wikipedia.org/wiki/") in URL_hero:
            globals()["URL_heroes" + str(i)].append(URL_hero)

        elif str("http://www.hrono.ru/biograf/bio_s/stepan_tverd.html") in URL_hero:
            globals()["URL_heroes" + str(i)].append(str("https://ru.wikipedia.org/wiki/Степан_Твердиславич"))

        elif str('http://100.histrf.ru') in URL_hero:
            if str('http://100.histrf.ru/commanders/mikulinskiy-semen-ivanovich/') in URL_hero:
                globals()["URL_heroes" + str(i)].append(str("https://ru.wikipedia.org/wiki/Микулинский,_Семён_Иванович"))
            if str('http://100.histrf.ru/commanders/basmanov-aleksey-danilovich/') in URL_hero:
                globals()["URL_heroes" + str(i)].append(str("https://ru.wikipedia.org/wiki/Басманов,_Алексей_Данилович"))

        elif 'http://www.endic.ru/brokgause/Ushkuniki-30426.html' in URL_hero:
            globals()["URL_heroes" + str(i)].append(str('https://ru.wikipedia.org/wiki/Александр_Абакумович'))

        # Общие статьи не имеющие дела к тому, что ищу я
        # http://coollib.com/b/308992/read
        # http://ruskline.ru/history

        elif str("http://coollib.com") or str("http://ruskline.ru"):
            continue
    i += 1