from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        data = data.drop(labels=self.columns, axis='columns')
        data['OBJETIVO'] = data['OBJETIVO'].replace(['Aceptado','Sospechoso'],[1,0])
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data
