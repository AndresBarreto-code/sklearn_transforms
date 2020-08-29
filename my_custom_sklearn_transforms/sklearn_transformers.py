from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        y.replace(['Aceptado','Sospechoso'],[1,0])
        return self

    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        print('ok transform X')
        return data.drop(labels=self.columns, axis='columns')
    def fit_transform(self, X, y=None):
        self = self.fit(X, y)
        return self.transform(X, y.replace(['Aceptado','Sospechoso'],[1,0]))
