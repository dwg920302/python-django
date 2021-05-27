from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import pandas as pd


# 이번 예제로 알게 된 것 : 벅스는 보안성이 취약함...


class MelonMusic(object):
    url = ''
    header = {'User-Agent': 'Mozilla/5.0'}  # 저는 봇이 아닙니다 준비과정 01
    soup = ''

    date = ''
    hour = ''

    class_dict = {1: "title", 2: "artist"}
    idx = 0

    t_lst = []
    a_lst = []
    common_dict = {}
    common_dfrm = None

    download_path = './data/melon.csv'

    RANKING_SIZE = 100

    def set_url(self):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={self.date}{self.hour}'
        modifier01 = urllib.request.Request(self.url, headers=self.header)  # 저는 봇이 아닙니다 준비과정 02
        print(f'입력한 URL = {self.url}')
        self.soup = BeautifulSoup(urlopen(modifier01), "lxml")

    def scrap_all(self):
        self.idx = 0
        for i in range(len(self.class_dict)):
            self.idx += 1
            self.scrap_ranking()

    def scrap_ranking(self):
        cnt = 0
        print(f'----------[{self.class_dict[self.idx]} RANKING]----------')
        for i in self.soup.find_all(name='div', attrs=({"class": f"ellipsis rank0{self.idx}"})):
            print(f'[{str(cnt+1)}위] : {i.find("a").text}')
            cnt += 1

    def create_t_list(self):
        for i in self.soup.find_all(name='div', attrs=({"class": "ellipsis rank01"})):
            self.t_lst.append(i.find("a").text)

    def create_a_list(self):
        for i in self.soup.find_all(name='div', attrs=({"class": "ellipsis rank02"})):
            self.a_lst.append(i.find("a").text)

    def make_dictionary(self):
        self.create_t_list()
        self.create_a_list()
        for i in range(len(self.t_lst)):
            self.common_dict[self.t_lst[i]] = self.a_lst[i]
        print(self.common_dict)
        print(len(self.common_dict))

    def get_list(self):
        for i in range(len(self.class_dict)):
            self.idx += 1

    def get_csv(self):  # Dictionary를 DataFrame화 + csv 파일 출력
        self.common_dfrm = pd.DataFrame.from_dict(self.common_dict, orient="index")
        self.common_dfrm.to_csv(self.download_path, sep=',', na_rep='NaN')
        print('[파일 생성됨]')




    @staticmethod
    def main():
        melon = MelonMusic()
        while 1:
            menu = input('[MENU]\n1 = get URL / 2 = get Ranking / 0 = Exit')
            if menu == '1':
                melon.date = input('날짜 입력 (ex) 20210525 -> ')
                melon.hour = input('몇 시의 차트를 가져올까요? (00, 01, 07~23) -> ')
                melon.set_url()
            elif menu == '2':
                melon.scrap_all()
            elif menu == '3':
                melon.make_dictionary()
            elif menu == '4':
                melon.get_csv()
            elif menu == '0':
                print('By2By2~')
                break
            else:
                print('Error')


MelonMusic.main()
