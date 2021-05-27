class MyDataFrame(object):

    def __init__(self, columns, index):  # columns, index
        self.columns = columns  # Dictionary의 Key 값에 해당함
        self.index = index

    @staticmethod
    def main():
        df = MyDataFrame(10, 3)


MyDataFrame.main()