from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


class BugsMusic(object):
    url = ''
    header = {'User-Agent': 'Mozilla/5.0'}
    soup = ''

    date = ''
    hour = ''

    class_name = []
    idx = 0

    t_lst = []
    a_lst = []
    common_dict = {}

    df = None

    RANKING_SIZE = 100

    def set_class_name(self):
        self.class_name = []
        self.class_name.append("title")
        self.class_name.append("artist")

    def init_lists(self):
        self.common_dict = {}
        self.a_lst = []
        self.t_lst = []

    def get_url(self):
        self.url = f'https://music.bugs.co.kr/chart/track/realtime/total?chartdate={self.date}&charthour={self.hour}'
        print(f'입력한 URL = {self.url}')
        self.soup = BeautifulSoup(urlopen(self.url), 'lxml')

    def scrap(self):
        self.set_class_name()
        cnt = 0
        print(f'---------------[title RANKING]---------------')
        for i in self.soup.find_all(name='p', attrs=({"class": self.class_name[0]})):
            cnt += 1
            print(f'[{str(cnt)}위] {self.class_name[0]} : {i.find("a").text}')
        cnt = 0
        print(f'---------------[artist RANKING]---------------')
        for i in self.soup.find_all(name='p', attrs=({"class": self.class_name[1]})):
            cnt += 1
            print(f'[{str(cnt)}위] {self.class_name[1]} : {i.find("a").text}')

    def scrap2(self):
        self.set_class_name()
        for i in range(len(self.class_name)):
            self.get_ranking_single()
            self.idx += 1
        self.idx = 0

    def get_ranking_single(self):
        self.init_lists()
        print(f'---------------[{self.class_name[self.idx]} RANKING]---------------')
        cname = self.class_name[self.idx]
        cnt = 0
        for i in self.soup.find_all(name='p', attrs=({"class": cname})):
            cnt += 1
            print(f'[{str(cnt)}위] {cname} name : {i.find("a").text}')

    def create_t_list(self):
        for i in self.soup.find_all(name='p', attrs=({"class", "title"})):
            self.t_lst.append(i.find('a').text)

    def create_a_list(self):
        for i in self.soup.find_all(name='p', attrs=({"class", "artist"})):
            self.a_lst.append(i.find('a').text)

    def get_ranking(self):
        self.init_lists()
        self.create_t_list()
        self.create_a_list()
        for i in range(len(self.t_lst)):
            print(f'{i+1} / {self.t_lst[i]} / {self.a_lst[i]}')

    def get_title_dict(self):
        self.init_lists()
        self.create_t_list()
        for i in range(len(self.t_lst)):
            self.common_dict[i+1] = self.t_lst[i]
        print(self.common_dict)

    def get_artist_dict(self):
        self.init_lists()
        self.create_a_list()
        for i in range(len(self.a_lst)):
            self.common_dict[i+1] = self.a_lst[i]
        print(self.common_dict)

    def get_rank_dict(self):
        self.init_lists()
        self.create_t_list()
        self.create_a_list()
        for i in range(len(self.t_lst)):
            self.common_dict[self.t_lst[i]] = self.a_lst[i]
        print(self.common_dict)

    def get_dataframe(self):
        dt = self.common_dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/bugs.csv'  # 뒤로 한 경로 가서 data 폴더
        self.df.to_csv(path, sep=',', na_rep='NaN')
        print('[파일 생성됨]')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('[MENU]\n1 = get URL / 2 = get Ranking / 3 = get title dict / 4 = get artist dict / 5 = get t+a dict / 0 = Exit')
            if menu == '1':
                bugs.date = input('날짜 입력 (ex) 20210525 -> ')
                bugs.hour = input('몇 시의 차트를 가져올까요? (00, 01, 07~23) -> ')
                bugs.get_url()
            elif menu == '2':
                bugs.scrap()
            elif menu == '3':
                bugs.get_title_dict()
            elif menu == '4':
                bugs.get_artist_dict()
            elif menu == '5':
                bugs.get_rank_dict()
            elif menu == '6':
                bugs.scrap2()
            elif menu == '7':
                bugs.get_ranking()
            elif menu == '8':
                bugs.get_dataframe()
            elif menu == '9':
                bugs.df_to_csv()
            elif menu == '0':
                print('By2By2~')
                break
            else:
                print('Error')


BugsMusic.main()
