import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):
    url = ''
    header = {'User-Agent': 'Mozilla/5.0'}

    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'
        print(self.url)

    def get_ranking(self):
        modifier = urllib.request.Request(self.url, headers=self.header)  # 나는 봇이 아닙니다
        soup = BeautifulSoup(urlopen(modifier), "lxml")
        cnt = 0
        res_01 = soup.find_all(name='div', attrs=({"class": "ellipsis rank01"}))
        res_02 = soup.find_all(name='div', attrs=({"class": "ellipsis rank02"}))
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
                melon.set_url(input('순위를 가져올 시간대 입력 (ex)2021052512 -> '))
            elif menu == '2':
                melon.get_ranking()
            else:
                print('Error')


Melon.main()
