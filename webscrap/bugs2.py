from bs4 import BeautifulSoup
import requests
import pandas as pd


# lecturer's code


class BugsMusic2(object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'https://music.bugs.co.kr/chart/track/realtime/total?chartdate={detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        ls2 = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls1:
            self.title_ls.append(i.soup.find('a').text)
        for i in ls2:
            self.artist_ls.append(i.soup.find('a').text)

    def insert_title_dict(self):
        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
            '''
            for i, j in enumerate(self.title_ls):
            self.dict[self.title_ls[j]] = self.artist_ls[i]
            
            for i, j in zip(self.title_ls, self.artist_ls):
            self.title_dict[i] = j
            '''

    def dict_to_dataframe(self):
        dt = self.dict
        df = pd.DataFrame.from_dict(dt, orient='index')
        print(df)

    @staticmethod
    def main():
        bugs = BugsMusic2()
        while 1:
            menu = input('0-exit, 1-input time, 2-output, 3-print dict')
            if menu == '0':
                break
            elif menu == '1':
                date = input('date (ex) 20210525 -> ')
                hour = input('time (ex) 00, 01, 07, 23 -> ')
                bugs.set_url(f'{date}{hour}')
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_title_dict()
            elif menu == '4':
                bugs.dict_to_dataframe()
            else:
                print('Wrong Number')
                continue


BugsMusic2.main()
