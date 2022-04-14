import pandas as pd
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

dataset = pd.read_csv('/home/marcelo/Downloads/Python_Data_Science/Pandas/data/db.csv'
                      ,sep = ';')

print (dataset)

print(dataset.dtypes)

print (dataset[['Quilometragem', 'Valor']].describe())

print (dataset.info())