class VectorTest(object):
    ls = []
    tiny_ls = []
    tp = ()
    tiny_tp = ()
    dt = {}
    tiny_dt = {}

    dt_struct = {'1': "List", '2': "Tuple", '3': "Dictionary"}

    struct = ''

    def set_list(self):
        self.ls = ['abcd', 786, 2.23, 'john', 70.2]
        self.tiny_ls = [123, 'john']
        self.tp = ('abcd', 786, 2.23, 'john', 70.2)
        self.tiny_tp = (123, 'john')
        self.dt = {'abcd': 786, 'john': 70.2}
        self.tiny_dt = {'홍': '30세'}

    def func_create(self):
        if self.struct == 'List':
            self.ls += [100]
            return self.ls
        elif self.struct == 'Tuple':
            self.tp += (100, )
            return self.tp
        elif self.struct == 'Dictionary':
            self.dt['tom'] = 100
            return self.dt

    def func_read(self):
        if self.struct == 'List':
            return self.ls
        elif self.struct == 'Tuple':
            return self.tp
        elif self.struct == 'Dictionary':
            return self.dt

    def func_update(self):
        if self.struct == 'List':
            self.ls += self.tiny_ls
            return self.ls
        elif self.struct == 'Tuple':
            self.tp += self.tiny_tp
            return self.tp
        elif self.struct == 'Dictionary':
            self.dt.update(self.tiny_dt)
            return self.dt

    def func_delete(self):
        if self.struct == 'List':
            self.ls.remove(786)
            return self.ls
        elif self.struct == 'Tuple':
            ls = list(self.tp)
            ls.remove(786)
            self.tp = tuple(ls)
            print('[!] 튜플 자체의 값을 직접 delete할 수는 없고, 리스트로 변환하고 다시 튜플로 바꾸는 식으로 해야 가능')
            # 튜플 자체의 값을 직접 delete 하는 건 불가능
            return self.tp
        elif self.struct == 'Dictionary':
            del self.dt['abcd']
            return self.dt

    def show_2nd_menu(self):
        while 1:
            crud = input(f'[{self.struct}의 CRUD] [(1).(C)reate] [(2).(R)ead] [(3).(U)pdate] [(4).(D)elete] [0.Go to Main] -> ')
            if crud == '0':
                break
            elif crud == '1' or crud == 'C' or crud == 'c':
                print(f'[{self.struct} Create] Result\n{self.func_create()}')  # 여기에 Create 기능
            elif crud == '2' or crud == 'R' or crud == 'r':
                print(f'[{self.struct} Read] Result\n{self.func_read()}')  # 여기에 Read 기능
            elif crud == '3' or crud == 'U' or crud == 'u':
                print(f'[{self.struct} Update] Result\n{self.func_update()}')  # 여기에 Update 기능
            elif crud == '4' or crud == 'D' or crud == 'd':
                print(f'[{self.struct} Delete] Result\n{self.func_delete()}')  # 여기에 Delete 기능
            else:
                print('[Error] 다시 입력하십시오')

    @staticmethod
    def main():
        vec = VectorTest()
        while 1:
            vec.struct = input('[Main Menu] [1 = List] [2 = Tuple] [3 = Dictionary] [0 = Exit]')
            if vec.struct == '0':
                print('[System] Program Off')
                break
            elif vec.struct == '1' or vec.struct == '2' or vec.struct == '3':
                vec.struct = vec.dt_struct[vec.struct]
                vec.show_2nd_menu()  # List의 CRUD
            else:
                print('[Error]')


VectorTest.main()

