import pandas as pd
import numpy as numpy
import csv

with open('DF_PNDXFolha21 - DF_PNDXFolha21.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print(', '.join(row))

# Lendo o arquivo CSV e criando um DataFrame
df = pd.read_csv('DF_PNDXFolha21 - DF_PNDXFolha21.csv')

# Exibindo o DataFrame
print(df.head())


