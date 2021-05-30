from bs4 import BeautifulSoup
import pandas as pd
import requests


# 코드가 너무 스파게티라 정리 필요
# 종목명 이름 TITLE(title)을 일부러 TLTLE(tltle)로 오타낸거 실화냐 ㅡㅡ


class NaverFinance(object):

    url = 'https://finance.naver.com/sise/lastsearch2.nhn'   # URL이 고정값이라 따로 입력받지 않음
    header = {'User-Agent': 'Mozilla/5.0'}
    path = './csv_data/naver_finance.csv'
    soup = None

    doc = ''

    ls_keys = []
    ls_values = []
    ls_values2 = []
    ls_elements = []

    ls_indexes = []

    common_dict = {}
    common_dframe = None

    def set_soup(self):
        pass

    # 네이버 금융서버에서 http 패킷 헤더의 웹 브라우저 정보(User-agent)를 체크
    # 웹 브라우저 정보를 함께 전송해야 한다.

    def get_stock_info(self):
        print(self.url)

        with requests.get(self.url, self.header) as doc:
            html = BeautifulSoup(doc.text, "html.parser")
            for i in html.find_all(name='tr', attrs=({"class": "type1"})):
                try:
                    self.ls_indexes.append(i.find(name='th').text)
                except AttributeError:  # None 처리
                    continue
        print(self.ls_indexes)

        with requests.get(self.url, self.header) as doc:    # 이렇게 되어야만 동작함
            html = BeautifulSoup(doc.text, "html.parser")
            for i in html.find_all(name="tr"):
                try:
                    self.ls_keys.append(i.find(name='td', attrs=({"class": "no"})).text)
                    self.ls_values.append(i.find(name='a', attrs=({"class": "tltle"})).text)
                    self.ls_values2.append(i.select('a')[0]['href'])
                except AttributeError:  # None-type 가져올 때 Error를 무시시킴
                    continue
        print(self.ls_keys)
        print(self.ls_values)
        print(self.ls_values2)
        self.re_value2()
        for i in range(len(self.ls_keys)):
            self.common_dict[self.ls_keys[i]] = [self.ls_values[i], self.ls_values2[i]]
        print(self.common_dict)

    def re_value2(self):
        cnt = 0
        for i in self.ls_values2:
            self.url = 'https://finance.naver.com'+i
            print(self.url)
            with requests.get(self.url, self.header) as doc:
                dat = BeautifulSoup(doc.text, "html.parser")
                for html in dat.find_all(name='div', attrs=({'class': 'description'})):
                    self.ls_values2[cnt] = html.find(name='span', attrs=({'class': 'code'})).text
                    cnt += 1
        print(self.ls_values2)

    def slicing(self):
        pass

    def get_csv(self):
        self.common_dframe = pd.DataFrame(self.common_dict)
        self.common_dframe.to_csv(self.path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        naver = NaverFinance()
        while 1:
            menu = input('[Menu] \n[1 = get Stocks] [2 = create csv] [0 = Exit]')
            if menu == '0':
                break
            elif menu == '1':
                naver.get_stock_info()
            elif menu == '2':
                naver.get_csv()
            elif menu == '3':
                naver.re_value2()
            else:
                pass


NaverFinance.main()
