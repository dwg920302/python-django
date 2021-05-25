from bs4 import BeautifulSoup
import requests

# Hwang Chae Youn 님의 코드


class MelonA(object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

    @staticmethod
    def ranking(soup, value, type):
        count = 0
        for i in soup.find_all("div", {"class": value}):
            count += 1
            print(f'{str(count)} 위')
            print(f' {type}: {i.find("a").text}')

    @staticmethod
    def main():
        melon = MelonA()
        while 1:
            menu = int(input('0. Exit\n  1. Input URL\n 2.Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                melon.url = requests.get(input('url을 입력하세요'), headers=melon.headers).text
            elif menu == 2:
                soup = BeautifulSoup(melon.url, 'lxml')
                print("<<Artist Ranking>>")
                melon.ranking(soup, "ellipsis rank01", "title")
                print("<<Title Ranking>>")
                melon.ranking(soup, "ellipsis rank02", "artist")
            else:
                print('다시 입력하세요')
                continue
                # https://www.melon.com/chart/index.htm


MelonA.main()
