from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'
    # parameter가 없으면 이렇게 생성자를 따로 정의하지 않아도 가능

    RANKING_SIZE = 100

    def __init__(self):
        pass
        # url = urlopen(self.url)

    def __str__(self):
        return self.url

    def scrap(self, url):
        soup = BeautifulSoup(url, '')

    @staticmethod
    def get_ranking_single(attr):
        soup = BeautifulSoup(urlopen(BugsMusic.url), 'lxml')
        cnt = 0
        print(f'---------------[{attr} RANKING]---------------')
        for i in soup.find_all(name='p', attrs=({"class": attr})):
            cnt += 1
            print(f'[{str(cnt)}위] {attr} : {i.find("a").text}')

    @staticmethod
    def get_ranking():
        soup = BeautifulSoup(urlopen(BugsMusic.url), 'lxml')
        cnt = 0
        title_lst = []
        artist_lst = []
        for i in soup.find_all(name='p', attrs=({"class": "title"})):
            title_lst.append(i.find('a').text)
        for i in soup.find_all(name='p', attrs=({"class": "artist"})):
            artist_lst.append(i.find('a').text)
        while cnt < BugsMusic.RANKING_SIZE:
            print(f'{cnt+1} / {title_lst[cnt]} / {artist_lst[cnt]}')
            cnt += 1

# 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('[MENU]\n1 = get URL / 2 = get Ranking / 3 = get Ranking? / 0 = Exit')
            if menu == '1':
                bugs.url = input('URL 입력 -> ')
            elif menu == '2':
                print(f'URL = {bugs}')
                BugsMusic.get_ranking_single("title")
                BugsMusic.get_ranking_single("artist")
            elif menu == '3':
                BugsMusic.get_ranking()
            elif menu == '0':
                print('By2By2~')
                break
            else:
                print('Error')


BugsMusic.main()
