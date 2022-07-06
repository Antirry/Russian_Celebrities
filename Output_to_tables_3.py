from Wikipedia_Parsing_2 import *
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

link = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
russian_celebrities = ServiceAccountCredentials.from_json_keyfile_name('russian_celebrities.json', link)
client = gspread.authorize(russian_celebrities)
Worksheet_Pattern = client.open('Заготовка').worksheet("Заготовка")

# Счетчик для расположения копии страницы
h0 = 2
# Счетчик списков
i = 0
for Title in Titles:
    Worksheet_Copy = Worksheet_Pattern.copy_to("15JDKGE28ZDbJf5JRzlXtwxCTcTMOJHTGOHEGRoDvb2A")
    time.sleep(1)
    print("Sleep Zzzz Worksheet_Copy")
    WorkSheet = client.open('Знаменитости России').worksheet("Заготовка (копия)")
    time.sleep(1)
    print("Sleep Zzzz WorkSheet")
    Worksheet_Title = WorkSheet.update_title(Title)
    time.sleep(1)
    print("Sleep Zzzz Worksheet_Title")
    WorkSheet = client.open('Знаменитости России').worksheet(Title)
    time.sleep(1)
    print("Sleep Zzzz WorkSheet")
    Worksheet_Cell_Title = WorkSheet.update_acell("B2", Title)
    time.sleep(1)
    print("Sleep Zzzz Worksheet_Cell_Title")

    # ЦИКЛ ИЗ ДОКУМЕНТАЦИИ https://docs.gspread.org
    # # Select a range
    # cell_list = worksheet.range('A1:C7')
    #
    # for cell in cell_list:
    #     cell.value = 'O_o'
    #
    # # Update in batch
    # worksheet.update_cells(cell_list)

    cell_list = WorkSheet.range('B3:B' + str(len(globals()["Data_Page_title" + str(i)]) + 2))

    # Счетчик ячейки ->
    h2 = 3
    # Счетчик каждого элемента списка ->
    i1 = 0

    Data_Page_title = globals()["Data_Page_title" + str(i)]

    for cell in cell_list:
        cell.value = Data_Page_title[i1]
        i1 += 1

    WorkSheet.update_cells(cell_list)
    time.sleep(1)
    print("Sleep Zzzz update_cells")

    # Для второго способа, где заменяется каждая ячейка ->

    cell_list = len(globals()["Data_heroes_title" + str(i)])

    h2 = 3
    i1 = 0
    Data_heroes_title = globals()["Data_heroes_title" + str(i)]
    URL_hero = globals()["URL_heroes" + str(i)]
    for cell in range(cell_list):
        print(Data_heroes_title[i1], "\n")
        WorkSheet.update_acell("C" + str(h2),
                               '= ГИПЕРССЫЛКА("' + URL_hero[i1] + '"' + "; " + '"' + Data_heroes_title[i1] + '")')
        i1 += 1
        h2 += 1
        time.sleep(1)
        print("Sleep Zzzz update_acell")

    h2 = 3
    i1 = 0

    Data_heroes_Image_URL_1 = globals()["Data_heroes_Image_URL" + str(i)]
    for cell in range(cell_list):
        print(Data_heroes_Image_URL_1[i1], "\n")
        if Data_heroes_Image_URL_1[i1] == "Нет картинки в таблице":
            WorkSheet.update_acell("D" + str(h2), "Нет картинки в таблице")
        else:
            WorkSheet.update_acell("D" + str(h2),
                                   '= IMAGE("' + Data_heroes_Image_URL_1[i1] + '")')
        i1 += 1
        h2 += 1
        time.sleep(1)
        print("Sleep Zzzz update_acell")

    cell_list = WorkSheet.range('E3:E' + str(len(globals()["Data_Page_title" + str(i)]) + 2))
    time.sleep(1)
    print("Sleep Zzzz ")
    i1 = 0

    Data_heroes_Description_Image = globals()["Data_heroes_Description_Image" + str(i)]
    for cell in cell_list:
        cell.value = Data_heroes_Description_Image[i1]
        i1 += 1

    WorkSheet.update_cells(cell_list)
    time.sleep(1)
    print("Sleep Zzzz update_cells")

    WorkSheet.format("B:E", {"wrapStrategy": "WRAP"})
    time.sleep(1)
    print("Sleep Zzzz format")

    i += 1

print("\n\nCompleted\n\n")
