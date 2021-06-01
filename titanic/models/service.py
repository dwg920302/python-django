from titanic.models.dataset import Dataset
import pandas as pd


class Service(object):

    dataset = Dataset()

    #   Dataframe(train, test)

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)  # 0 = 가로 1 = 세로

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        dict_em = {'S': '1', 'C': '2', 'Q': '3'}
        this.train['Embarked'] = this.train['Embarked'].map(dict_em)
        this.test['Embarked'] = this.test['Embarked'].map(dict_em)
        #   map 함수를 사용하여, S : 1, C : 2, Q : 3
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        return this

    @staticmethod
    def fare_band_fill_na(this) -> object:
        this.train['Fare'].fillna({'Embarked': 'S'})
        #   N/A 값들 채우기 (fill)   fare, band?
        return this

    @staticmethod
    def title_nominal(this) -> object:
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
            # 칼럼 추가방법. extract 내에 있는 건 정규표현식
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], "Rare")
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
        for dataset in combine:
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
            #fillna(0) 0은 호칭이 없는 극빈, 노예
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        mapping = {'male': 0, 'female': 1}
        combine = [this.train, this.test]
        for dataset in combine:
            dataset.rename(columns={'Sex': 'Gender'}, inplace=True)
            dataset['Gender'] = dataset['Gender'].map(mapping)
            # 만약 inplace=True가 없다면 바뀐 내용이 적용되지 않음
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Age'] = dataset['Age'].fillna(0.0)
            dataset['Age'] = dataset['Age'].map(lambda x: int(x))
        return this

    @staticmethod
    def create_k_fold(this) -> object:
        return this  # 이건 매우 어려울 거 같은데 ㄷㄷㄷ
