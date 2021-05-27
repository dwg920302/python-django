import pandas as pd


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
        return dict(zip(ls, ls))
        #   return {str(i): ls[i] for i in range(len(ls))}

    @staticmethod
    def make_better_dict(ls) -> {}:
        ls_2 = []
        for i in ls:
            ls_2.append([i])
        return dict(zip(ls, ls_2))

    @staticmethod
    def str_to_tuple(param) -> ():
        return tuple(param)

    @staticmethod
    def dict_to_dataframe(dc) -> pd.DataFrame:
        return pd.DataFrame(dc, index=[''])

    @staticmethod
    def dic_to_df(dc) -> object:
        return pd.DataFrame(dc)
        # DC만 넣어서 데이터 프레임 작성 SSAP가능. 단, 다음 두 조건을 만족해야 함
        # 1. 형태가 무조건 key(단일) : value(다중(list, ...)) 이어야 함
        # 2. Value값이 전부 같은 크기여야 함 (리스트 크기가 1이어도 OK)
        # 자동 완성이라 편리하다는 장점, idx를 자동으로 잡아버린다는 단점

    @staticmethod
    def dict_to_dataframe_other(dc) -> object:
        return pd.DataFrame.from_dict(dc, orient='index')
        # orient는 index와 columns만 받음. column이 default고, index는 x,y를 반대로 정렬함

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
                dc = c.make_dict(ls)
                df = c.dict_to_dataframe(dc)
                print(df)
                dc = c.make_better_dict(ls)
                df = c.dic_to_df(dc)
                print(df)
            elif menu == '9':  #
                dc = c.make_dict(ls)
                df = c.dict_to_dataframe_other(dc)
                print(df)
            else:
                print('err')


ConversionA.main()
