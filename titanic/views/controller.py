from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service

    def preprocess(self, train) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        print(f'Train Type = {type(this.train)}')
        print(f'Train의 column = {this.train.columns}')
        print(f'Train의 상위 5개 데이터 = {this.train.head()}')
        print(f'Train의 하위 5개 데이터 = {this.train.tail()}')

    def preprocess_2(self, file) -> object:
        service = self.service
        this = self.dataset
        this.file = service.new_model(file)
        print(f'Train Type = {type(this.file)}')
        print(f'Train의 column = {this.file.columns}')
        print(f'Train의 상위 5개 데이터 = {this.file.head()}')
        print(f'Train의 하위 5개 데이터 = {this.file.tail()}')

