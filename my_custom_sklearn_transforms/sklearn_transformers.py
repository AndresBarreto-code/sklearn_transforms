from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X, y):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        datay = y.copy()
        print('ok4')
        return [data.drop(labels=self.columns, axis='columns'),datay.replace(['Aceptado','Sospechoso'],[1,0])]
    def transform2(self, y):
        data = y.copy()
        print('ok2')
        return data.replace(['Aceptado','Sospechoso'],[1,0])
