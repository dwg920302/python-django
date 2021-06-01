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
        #   초기 모델 생성
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        #   불필요한 feature (Cabin, Ticket) 제거
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        #   nominal,ordinal로 정형화
        this = service.drop_feature(this, 'Name')
        #   불필요한 feature (Name) 제거
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('-'*44+'<type check>'+'-'*44)
        print(f'Train Type = {type(this.train)}')
        print(f'Train의 column = {this.train.columns}')
        print(f'Train의 상위 5개 데이터 = {this.train.head(20)}')
        print(f'Test Type = {type(this.test)}')
        print(f'Test의 column = {this.test.columns}')
        print(f'Test의 상위 5개 데이터 = {this.test.head(20)}')
        print('-' * 100)
