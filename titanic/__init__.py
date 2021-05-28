from titanic.views.controller import Controller


if __name__ == '__main__':
    controller = Controller()
    while 1:
        mn = input('[Menu] (0)Exit (1)Pre-Process Model')
        if mn == '0':
            break
        elif mn == '1':
            controller.preprocess('train.csv')
        elif mn == '8':
            controller.preprocess_2(input('파일명 입력(data에 있음)'))
        else:
            print('error')
