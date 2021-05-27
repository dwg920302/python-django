import pandas as pds


class Conversion(object):
    i = 0
    f = 0.0
    s = ''
    ls = []
    tp = ()
    dc = {}
    df = ''

    def new_tuple(self):
        self.tp = ()

    def make_tuple(self):
        self.new_tuple()
        for i in range(1, 10 + 1):
            self.tp += (i, )
        return self.tp

    def tuple_to_list(self):
        self.ls = list(self.tp)
        return self.ls

    def cvt_to_float(self):
        for i in self.ls:
            i = float(i)    # i가 for 내에서 끝나므로 i를 대입시켜줄 방법이 없음
        return self.ls

    def cvt_to_int(self):
        for i in self.ls:
            i = int(i)      # i가 for 내에서 끝나므로 i를 대입시켜줄 방법이 없음
        return self.ls

    def make_dict(self):
        for i in range(len(self.ls)):
            self.dc[str(i)] = self.ls[i]
        return self.dc

    def hello_tuple(self):
        self.new_tuple()
        self.tp = tuple("hello")    #string이 list 역할도 하므로 따로 list 컨버트를 거칠 필요가 없음
        return self.tp

    def dict_to_dataframe(self):
        self.df = pds.DataFrame(self.dc, index=[''])
        return self.df

    @staticmethod
    def main():
        c = Conversion()
        while 1:
            menu = input(' [0 = exit] \n [1=Create Tuple] [2=Convert Tuple to List]'
                         '\n [3=Convert List elements to float] [4=Convert List elements to Int]'
                         '\n [5=List Convert Dictionary] [6=Convert Str to Tuple]'
                         '\n [7=Convert Tuple to List] [8=Convert Dictionary to DataFrame]')
            if menu == '0':
                break
            elif menu == '1':  # 1부터 10까지 요소를 가진 튜플을 생성하시오
                print(c.make_tuple())
            elif menu == '2':  # 1번 튜플을 리스트로 전환하시오 (return)
                print(c.tuple_to_list())
            elif menu == '3':  # 2번 리스트를, 실수(float) 리스트 바꾸시오
                print(c.cvt_to_float())
            elif menu == '4':  # 3번 실수(float) 리스트를, 정수 리스트로 바꾸시오  (return)
                print(c.cvt_to_int())
            elif menu == '5':  # 4번 리스트를 딕셔너리로 전환하시오. 단, 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
                print(c.make_dict())
            elif menu == '6':  # 'hello' 를 튜플로 전환하시오 (return)
                print(c.hello_tuple())
            elif menu == '7':  # 6번 튜플을 리스트로 전환하시오 (return)
                print(c.tuple_to_list())
            elif menu == '8':  # 5번 딕셔너리를 데이터프레임(판다스) 으로 전환하시오
                print(c.dict_to_dataframe())
            else:
                print('err')


Conversion.main()
