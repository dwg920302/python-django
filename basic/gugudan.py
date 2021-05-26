'''
구구단 프로그램은 단을 입력받아서, 입력받은 단의 1 ~ 9의 곱을 출력하는 어플이다.
단, 단은 정수이다.
'''


class Gugudan(object):
    dan = 0  # 정수로 초기화
    dict = {}

    def print_one_dan(self):
        for i in range(1, 9 + 1):
            print(f'{self.dan} * {i} = {self.dan * i}')

    def print_all_dan(self):
        for i in range(2, 9 + 1):
            self.dan = i
            self.print_one_dan()

    def print_dict_dan(self):
        d = self.dict
        for i in range(1, 9 + 1):
            d[i] = i * self.dan  # dictionary[(key)] = (value)
        print(d)
        for j in d.keys():
            print(f'{self.dan} * {j} = {d.get(j)}')
        # key는 유니크(유일)하기 때문에 단으로 Key값을 쓸 수 없음 (단의 수는 계속 반복되므로)

    @staticmethod
    def main():
        print('[구구단 프로그램]')
        gugudan = Gugudan()
        while 1:
            menu = input('[0-exit] [1-input dan] [2-all dan] [3-input dan with dict]')
            if menu == '0':
                break
            elif menu == '1':
                gugudan.dan = int(input('몇 단을 출력하시겠습니까?'))
                gugudan.print_one_dan()
            elif menu == '2':
                gugudan.print_all_dan()
            elif menu == '3':
                gugudan.dan = int(input('몇 단을 출력하시겠습니까?'))
                gugudan.print_dict_dan()
            else:
                print('Error')


Gugudan.main()
