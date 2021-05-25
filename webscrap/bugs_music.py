from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    url = ''
    class_name = []

    RANKING_SIZE = 100

    def get_url(self):
        date = input('날짜 입력 (ex) 20210525 -> ')
        hour = input('몇 시의 차트를 가져올까요? (00, 01, 07~23) -> ')
        self.url = f'https://music.bugs.co.kr/chart/track/realtime/total?chartdate={date}&charthour={hour}'
        print(f'입력한 URL = {self.url}')

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        cnt = 0
        print(f'---------------[title RANKING]---------------')
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[0]})):
            cnt += 1
            print(f'[{str(cnt)}위] {self.class_name[0]} : {i.find("a").text}')
        cnt = 0
        print(f'---------------[artist RANKING]---------------')
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[1]})):
            cnt += 1
            print(f'[{str(cnt)}위] {self.class_name[1]} : {i.find("a").text}')

    def get_ranking_single(self, class_name):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        cnt = 0
        print(f'---------------[{class_name} RANKING]---------------')
        for i in soup.find_all(name='p', attrs=({"class": class_name})):
            cnt += 1
            print(f'[{str(cnt)}위] {class_name} : {i.find("a").text}')

    def get_ranking(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
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

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('[MENU]\n1 = get URL / 2 = get Ranking / 3 = get Ranking? / 4 = get Ranking_all / 0 = Exit')
            if menu == '1':
                bugs.get_url()
            elif menu == '2':
                bugs.class_name.append("title")
                bugs.class_name.append("artist")
                bugs.scrap()
            elif menu == '3':
                bugs.get_ranking_single("title")
                bugs.get_ranking_single("artist")
            elif menu == '4':
                bugs.get_ranking()
            elif menu == '0':
                print('By2By2~')
                break
            else:
                print('Error')


BugsMusic.main()
