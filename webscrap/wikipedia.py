class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        wiki = Wikipedia
        while 1:
            menu = input('[MENU]\n1 = get URL / 2 = show URL / 0 = Exit')
            if menu == '0':
                break
            elif menu == '1':
                wiki = Wikipedia(input('URL 입력 ->'))
            elif menu == '2':
                print(f'URL = {wiki}')
            else:
                print('Error')


Wikipedia.main()
