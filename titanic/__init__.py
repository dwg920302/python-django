from titanic.views.controller import Controller
from titanic.templates.plot import Plot

if __name__ == '__main__':
    controller = Controller()
    while 1:
        mn = input('[Menu] (0)Exit (1)Data Visualization (2)Data Modeling '
                   '(3)Machine Learning (4)Machine Release -> ')
        if mn == '0':
            break
        elif mn == '1':
            plot = Plot('train.csv')
            plot.draw_survived()
            plot.draw_pclass()
            plot.draw_sex()
            plot.draw_embarked()
        elif mn == '2':
            controller.modeling('train.csv', 'test.csv')
        elif mn == '3':
            pass
        elif mn == '4':
            pass
        else:
            print('error')
