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
        data[self.columns] = data[self.columns].replace(['Aceptado','Sospechoso'],[1,0])
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data
