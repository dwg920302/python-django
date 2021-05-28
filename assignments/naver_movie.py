from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request


class NaverMovie(object):
    url = ''
    header = {'User-Agent': 'Mozilla/5.0'}
    dc = {}
    soup = None
    modifier = None

    def get_url(self):
        date = input('날짜 입력 (ex) 20210524 -> ')
        self.url = f'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date={date}'
        print(self.url)
        self.modifier = urllib.request.Request(self.url, headers=self.header)

    def get_ranking(self):
        self.soup = BeautifulSoup(urlopen(self.modifier), "lxml")
        cnt = 0
        all_div = self.soup.find_all(name='div', attrs=({"class": "tit3"}))  # 여기서 못 찾아왔음
        print(all_div)
        for i in all_div:
            cnt += 1
            print(i.find('a').text)
            self.dc[cnt] = i.find('a').text
        print(self.dc)

        # 이건 왜 아무것도 안담기는 거임???

    @staticmethod
    def main():
        naver = NaverMovie()
        while 1:
            menu = input('[0 = Exit] [1 = Get URL] [2 = Get RANKING]')
            if menu == '0':
                break
            elif menu == '1':
                naver.get_url()
            elif menu == '2':
                naver.get_ranking()
            else:
                print('[Error] 올바른 명령어를 입력해주십시오.')


NaverMovie.main()
