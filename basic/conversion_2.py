import pandas as pds


class ConversionA(object):
    @staticmethod
    def make_tuple() -> ():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    @staticmethod
    def tuple_to_list(tp) -> []:
        return list(tp)

    @staticmethod
    def cvt_to_float(ls) -> []:
        return [float(i) for i in ls]
    # return is map(float(ls)) ??

    @staticmethod
    def cvt_to_int(ls) -> []:
        return [int(i) for i in ls]

    @staticmethod
    def make_dict(ls) -> {}:
        return {str(i): ls[i] for i in range(len(ls))}

    @staticmethod
    def str_to_tuple(param) -> ():
        return tuple(param)

    @staticmethod
    def dict_to_dataframe(dc) -> pds.DataFrame:
        return pds.DataFrame(dc, index=[''])

    @staticmethod
    def main():
        ls = []
        tp = ()
        dc = {}
        df = ''
        c = ConversionA()
        while 1:
            menu = input(' [0 = exit] \n [1=Create Tuple] [2=Convert Tuple to List]'
                         '\n [3=Convert List elements to float] [4=Convert List elements to Int]'
                         '\n [5=List Convert Dictionary] [6=Convert Str to Tuple]'
                         '\n [7=Convert Tuple to List] [8=Convert Dictionary to DataFrame]')
            if menu == '0':
                break
            elif menu == '1':  # 1부터 10까지 요소를 가진 튜플을 생성하시오
                tp = c.make_tuple()
                print(tp)
            elif menu == '2':  # 1번 튜플을 리스트로 전환하시오 (return)
                ls = c.tuple_to_list(tp)
                print(ls)
            elif menu == '3':  # 2번 리스트를, 실수(float) 리스트 바꾸시오
                ls = c.cvt_to_float(ls)
                print(ls)
            elif menu == '4':  # 3번 실수(float) 리스트를, 정수 리스트로 바꾸시오  (return)
                ls = c.cvt_to_int(ls)
                print(ls)
            elif menu == '5':  # 4번 리스트를 딕셔너리로 전환하시오. 단, 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
                dc = c.make_dict(ls)
                print(dc)
            elif menu == '6':  # 'hello' 를 튜플로 전환하시오 (return)
                tp = c.str_to_tuple('hello')
                print(tp)
            elif menu == '7':  # 6번 튜플을 리스트로 전환하시오 (return) (2번이랑 명령어가 겹쳐서 합칠 예정)
                ls = c.tuple_to_list(tp)
                print(ls)
            elif menu == '8':  # 5번 딕셔너리를 데이터프레임(판다스) 으로 전환하시오
                df = c.dict_to_dataframe(dc)
                print(df)
            else:
                print('err')


ConversionA.main()
