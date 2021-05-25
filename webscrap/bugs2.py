class Bugs2(object):

    url = ''
    class_name = []

    def set_url(self, url):
        pass

    def get_ranking(self):
        pass

    @staticmethod
    def main():
        b = Bugs2()
        while 1:
            menu = input('0, 1-input, 2-output')
            if menu == '1':
                b.set_url(input('url -> '))
            elif menu == '2':
                b.get_ranking()


Bugs2.main()
