from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset: object = Dataset()
    service: object = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test):
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Train Type = {type(this.train)}')
        print(f'Train의 column = {this.train.columns}')
        print(f'Test Type = {type(this.test)}')
        print(f'Train의 column = {this.test.columns}')
        return this
