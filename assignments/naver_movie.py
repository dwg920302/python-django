from bs4 import BeautifulSoup
from urllib.request import urlopen


class NaverMovie(object):
    url = ''

    def get_url(self):
        date = input('날짜 입력 (ex) 20210524 -> ')
        self.url = f'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date={date}'
        print(self.url)

    def get_ranking(self):
        soup = BeautifulSoup(urlopen(self.url), "lxml")
        cnt = 0
        for i in soup.find_all(name='td', attrs=({"class": "title"})):
            cnt += 1
            print(f"{cnt}위 : {i.find('a').text}")

    @staticmethod
    def main():
        naver = NaverMovie()
        while 1:
            menu = input('[0 = Exit]')
            if menu == '0':
                break
            elif menu == '1':
                naver.get_url()
            elif menu == '2':
                naver.get_ranking()
            else:
                print('[Error] 올바른 명령어를 입력해주십시오.')


NaverMovie.main()
