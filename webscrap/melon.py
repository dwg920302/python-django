import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    date = ''
    hour = ''
    header = {'User-Agent': 'Mozilla/5.0'}
    soup = ''

    def set_url(self):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={self.date}{self.hour}'
        print(f'입력한 URL = {self.url}')
        modifier = urllib.request.Request(self.url, headers=self.header)  # 나는 봇이 아닙니다
        self.soup = BeautifulSoup(urlopen(modifier), "lxml")

    def get_ranking(self):
        cnt = 0
        res_01 = self.soup.find_all(name='div', attrs=({"class": "ellipsis rank01"}))
        res_02 = self.soup.find_all(name='div', attrs=({"class": "ellipsis rank02"}))
        while cnt < 100:
            print(f'[{cnt+1}위] {res_01[cnt].find("a").text} / {res_02[cnt].find("a").text}')
            cnt += 1

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('[0 = Exit] ')
            if menu == '0':
                break
            elif menu == '1':
                melon.date = input('날짜 입력 (ex) 20210525 -> ')
                melon.hour = input('몇 시의 차트를 가져올까요? (00, 01, 07~23) -> ')
                melon.set_url()
            elif menu == '2':
                melon.get_ranking()
            else:
                print('Error')


Melon.main()
