from titanic.models.dataset import Dataset
from titanic.models.service import Service
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class Controller(object):

    dataset: object = Dataset()
    service: object = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def learning(self, train, test):
        this = self.modeling(train, test)
        print(f'사이킷런의 SVC 알고리즘 정확도 {self.service.accuracy_by_svm(this)} %')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)

    def preprocess(self, train, test):
        service = self.service
        this = self.dataset
        # 이 부분이랑 서비스의 해당 부분을 고치면 됨

        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        this = service.drop_feature(this, 'Fare', 'Cabin', 'Ticket', 'Name', 'Gender', 'Age')
        self.print_this(this)
        return this

    def preprocess_origin(self, train, test):
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        this = service.drop_feature(this, 'Fare', 'Cabin', 'Ticket', 'Name', 'Gender', 'Age')
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        reveal_val = 10
        print('-'*44+'<type check>'+'-'*44)
        print(f'Train Type = {type(this.train)}')
        print(f'Train의 column = {this.train.columns}')
        print(f'Train의 상위 3개 데이터 = {this.train.head(reveal_val)}')
        print(f'Train의 null 갯수 = {this.train.isnull().sum()}')
        print(f'Test Type = {type(this.test)}')
        print(f'Test의 column = {this.test.columns}')
        print(f'Test의 상위 3개 데이터 = {this.test.head(reveal_val)}')
        print(f'Test의 null 갯수 = {this.test.isnull().sum()}')
        print('-' * 100)

