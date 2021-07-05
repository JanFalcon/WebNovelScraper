import requests
from bs4 import BeautifulSoup

current_url = "https://m.wuxiaworld.co/I-am-the-Monarch/1032696.html"

with open("D:\\Novels\\HTMLDATA.txt", 'r') as reader:
    current_url = reader.readline()
    url = reader.readline()
    path_directory = reader.readline()
    novel_name = reader.readline()

# meow

current_url = current_url.replace("\n", "")
url = url.replace("\n", "")
path_directory = path_directory.replace("\n", "")
novel_name = novel_name.replace("\n", "")

print(current_url)
print(url)
print(path_directory)
print(novel_name)

chapter_number = 1
previous_file = ""
next_file = ""

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.134 Safari/537.36 Viv/2.5.1525.40"}
condition = True
end = False

while condition:
    try:
        page = requests.get(current_url, headers=headers)

        if page.status_code == 200:
            print("Scraping Chapter :" + str(chapter_number))

            soup = BeautifulSoup(page.content, 'html.parser')

            chapter = soup.find("div", {"id": "chaptercontent"})

            for link in soup.find_all('a'):
                href_link = str(link)
                if "Readpage_down js_page_down" in href_link:
                    if ".html" in href_link:
                        new_link = href_link.split("href=\"")
                        new_link1 = new_link[-1].split("\"")
                        next_url = new_link1[0]
                        print("current URL : " + current_url)
                        break
                    else:
                        condition = False
                        end = True

            with open(path_directory + novel_name + "_" + str(chapter_number) + ".txt", "w") as file:
                novel = str(chapter)
                previous_file = path_directory + novel_name + "_" + str(chapter_number - 1) + ".txt"
                next_file = path_directory + novel_name + "_" + str(chapter_number + 1) + ".txt"
                file.write(previous_file + "<split>\n" + next_file + "<split>\n" + current_url + "\n\n" + str(novel.encode()))
                # file.write(current_url + "\n\n" + str(novel.encode(encoding="ascii", errors="ignore")))

            current_url = url + next_url
            print("new URL : " + current_url)
            print(novel_name + " Chapter : " + str(chapter_number) + " DONE!")
            chapter_number += 1

            if end:
                print("END")

    except requests.exceptions.RequestException as err:

        print("OOps: Something Else", err)

    except requests.exceptions.HTTPError as errh:

        print("Http Error:", errh)

    except requests.exceptions.ConnectionError as errc:

        print("Error Connecting:", errc)

    except requests.exceptions.Timeout as errt:

        print("Timeout Error:", errt)
