from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen


# 이번 예제로 알게 된 것 : 벅스는 보안성이 취약함...


class MelonMusic(object):
    url = ''
    header = {'User-Agent': 'Mozilla/5.0'}  # 저는 봇이 아닙니다 준비과정 01

    def set_url(self):
        pass

    def scrap_ranking(self, category, ct_number):
        modifier01 = urllib.request.Request(self.url, headers=self.header)  # 저는 봇이 아닙니다 준비과정 02
        soup = BeautifulSoup(urlopen(modifier01), "lxml")
        cnt = 0
        print(f'----------[{category} RANKING]----------')
        for i in soup.find_all(name='div', attrs=({"class": f"ellipsis rank0{ct_number}"})):
            cnt += 1
            print(f'[{str(cnt)}위] : {i.find("a").text}')

    @staticmethod
    def main():
        melon = MelonMusic()
        while 1:
            menu = input('[MENU]\n1 = get Ranking / 2 = ??? / 0 = Exit')
            if menu == '1':
                melon.set_url()
            elif menu == '2':
                melon.scrap_ranking("SONG", 1)
                melon.scrap_ranking("ARTIST", 2)
            elif menu == '0':
                print('By2By2~')
                break
            else:
                print('Error')


MelonMusic.main()
