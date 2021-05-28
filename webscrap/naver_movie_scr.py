from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


class NaverMovieScr(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = ''
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    csv_path = './data/naver_movie.csv'
    dc = {}
    df = None

    # 영화 랭킹을 url, class , driver로

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all(name='div', attrs=({"class": "tit3"}))
        cnt = 0
        for i in all_div:
            cnt += 1
            self.dc[cnt] = [i.find('a').text]
        #   print([i.find('a').text for i in all_div])
        #   print(i)
        print(self.dc)
        driver.close()

    def create_csv(self):
        self.df = pd.DataFrame(self.dc)
        self.df.to_csv(self.csv_path, sep=',', na_rep='NaN')


if __name__ == '__main__':
    naver = NaverMovieScr()
    naver.scrap()
    naver.create_csv()
