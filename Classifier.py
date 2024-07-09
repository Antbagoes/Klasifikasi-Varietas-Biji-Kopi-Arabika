import pandas as pd

pd.set_option('display.max_columns', 15)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from scipy.stats import entropy
from sklearn.metrics import confusion_matrix


class Classifier:
    def __init__(self):
        self.default_url = 'DataSet/arabica_data_cleaned.csv'
        self.all_column_name = ['ID', 'Species', 'Owner', 'Country.of.Origin', 'Farm.Name', 'Lot.Number', 'Mill',
                                'ICO.Number', 'Company', 'Altitude', 'Region', 'Producer', 'Number.of.Bags',
                                'Bag.Weight',
                                'In.Country.Partner', 'Harvest.Year', 'Grading.Date', 'Owner.1', 'Variety',
                                'Processing.Method',
                                'Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity',
                                'Clean.Cup',
                                'Sweetness', 'Cupper.Points', 'Total.Cup.Points', 'Moisture', 'Category.One.Defects',
                                'Quakers', 'Color', 'Category.Two.Defects', 'Expiration', 'Certification.Body',
                                'Certification.Address', 'Certification.Contact', 'unit_of_measurement',
                                'altitude_low_meters',
                                'altitude_high_meters', 'altitude_mean_meters']
        self.use_column = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Uniformity',
                           'Balance', 'Clean.Cup', 'Sweetness', 'Cupper.Points', 'Variety']
        self.x_column = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Uniformity',
                         'Balance', 'Clean.Cup', 'Sweetness', 'Cupper.Points']
        self.y_column = 'Variety'

    def GetDataSet(self):
        df = pd.read_csv(self.default_url, skiprows=[0], names=self.all_column_name)
        return df
    def PrepData(self, df):
        # --------------------------------------------------------Data Cleaning -------------------------------------------------------------------

        df = df[(df[self.use_column] != 0).all(axis=1)]
        df = df[self.use_column].dropna()

        # --------------------------------------------------------Selection Data -------------------------------------------------------------------

        df = df[self.use_column]

        # Label Class Selection
        select_label_class = ['Bourbon', 'Caturra', 'Typica']
        df = pd.DataFrame(df[df['Variety'].isin(select_label_class)])

        # --------------------------------------------------------Data Transformation -------------------------------------------------------------------

        replace = [1, 2, 3]
        df['Variety'] = df['Variety'].replace(select_label_class, replace)

        # Min-Max normalization
        for column in df.columns:
            df[self.x_column] = (df[self.x_column] - df[self.x_column].min()) / (
                    df[self.x_column].max() - df[self.x_column].min())

        return df

    def NormalizeTestingData(self, df):
        df = (df - 0) / (10 - 0)
        return df

    def Predict(self, x_pred):
        # Import CSV File
        df = pd.read_csv(self.default_url, skiprows=[0], names=self.all_column_name)
        df = self.PrepData(df)

        x = df[self.x_column]
        y = df[self.y_column]
        model_knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='euclidean')
        model_knn.fit(x, y)
        predict_result = model_knn.predict(x_pred)
        return predict_result

    def CalculateAcuracy(self, df, knn, cv, attribut):
        x = df[self.x_column]
        y = df[self.y_column]

        information_gain = self.InformationGain(x, y)
        attribut_information_gain = information_gain.index

        attribute_for_classification = []
        for element in range (attribut):
            attribute_for_classification.append(attribut_information_gain[element])
        x = df[attribute_for_classification]

        model_knn = KNeighborsClassifier(n_neighbors=knn, p=2, metric='euclidean')
        model_knn.fit(x, y)
        cv_result = cross_val_score(model_knn, x, y, cv=cv, scoring='accuracy')

        y_train_pred = cross_val_predict(model_knn, x, y, cv=3)
        cm = confusion_matrix(y, y_train_pred)

        return_value = [cv_result.mean(), cm]
        return return_value

    def InformationGain(self, x, y):
        igResult = []
        columnName = x.columns
        count = 0
        for element in columnName:
            columnValue = x[columnName[count]]
            entropy_before = entropy(columnValue.value_counts(normalize=True))
            y.name = 'split'
            columnValue.name = 'members'
            grouped_distrib = columnValue.groupby(y).value_counts(normalize=True).reset_index(name='count').pivot_table(
                index='split', columns='members', values='count').fillna(0)
            entropy_after = entropy(grouped_distrib, axis=1)
            entropy_after *= y.value_counts(sort=False, normalize=True)
            ig = entropy_before - entropy_after.sum()
            igResult.append(ig)
            count += 1
        InformartionGain = pd.Series(igResult)
        InformartionGain.index = columnName
        return InformartionGain.sort_values(ascending=False)

    def ZeroCounter(self, df):
        count_zore = (df == 0).sum()
        print("--------   Jumlah Data 0   --------")
        print(count_zore)
        print("-----------------------------------\n")

    def NanCounter(self, df):
        count_nan = df.isnull().sum()
        print("-----   Jumlah Data Kosong   ------")
        print(count_nan)
        print("-----------------------------------\n")

    def FrequencyTable(self, df):
        distribution_freq = df.value_counts()
        print("-----   Tabel Frekuensi   ------")
        print(distribution_freq)
        print("---------------------------------\n")


'''
def main():
    df = pd.read_csv(default_url, skiprows=[0], names=all_column_name)
    df = PrepData(df)
    #print(df.head())
    #print("\n")


    for button predict
    testing = {'Aroma' : [9.76608],
               'Flavor' : [10],
               'Aftertaste' : [10],
               'Acidity' : [10],
               'Body' : [10],
               'Uniformity' : [10],
               'Balance' : [9.36],
               'Clean.Cup' : [10],
               'Sweetness' : [10],
               'Cupper.Points' : [10]}
    testing_df = pd.DataFrame(testing)
    testing_df = NormalizeTestingData(testing_df)
    print(testing_df)
    print(Predict(testing_df))
    

if __name__ == '__main__':
    main()
    
    '''
