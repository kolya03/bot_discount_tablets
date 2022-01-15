import requests
from bs4 import BeautifulSoup

old_url = "https://anc.ua/ru/catalog/medikamenty-1/prostuda-i-gripp-2/preparaty-ot-prostudy-3?pages=1"
url = ""

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


def first_method():
    new_url = "https://anc.ua/ru/catalog/medikamenty-1/prostuda-i-gripp-2/preparaty-ot-prostudy-3?pages="
    q = requests.get(old_url)
    res = q.content

    soup = BeautifulSoup(res, "lxml")

    number = soup.find("span", class_="manufacturer--count")
    num_page = int(number.text) / 15
    num = round(num_page)
    num_page = num + 2

    for i in range(1, num_page):
        if i == num_page:
            new_url += f"{i}"
            break
        new_url += f"{i},"
    return new_url

def second_method(url):
    q = requests.get(url)
    res = q.content

    soup = BeautifulSoup(res, "lxml")

    tabletki_url = []
    items = soup.find_all(class_="products-item-img")

    for i in items:
        url_tablet = i.get("href")
        full_url = f"https://anc.ua{url_tablet}"
        tabletki_url.append(full_url)


    with open("all_url_tabletki.txt", "a") as file:
        for line in tabletki_url:
            file.write(f"{line}\n")



def collect_data():
    urll = first_method() #обработка ссылки

    second_method(urll)

    with open("all_url_tabletki.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        pass






def main():
    collect_data()

if __name__ == '__main__':
    main()
