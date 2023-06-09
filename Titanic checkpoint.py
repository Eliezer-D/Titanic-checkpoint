import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Importer l'ensemble de données
data = pd.read_csv('titanic-passengers.csv', sep =';')
data.shape
# Afficher l'en-tête de l'ensemble de données
data.head()

# Afficher les informations générales sur les colonnes et les valeurs
data.info()

# Identifier les valeurs manquantes
data.isna()

# Remplacer les valeurs manquantes par la moyenne des colonnes numériques
data["Age"] = data["Age"].fillna(data["Age"].mean())
data

# Appliquer un encodage à chaud (One hot encoding) sur les colonnes catégorielles

encoded_data = pd.get_dummies(data, columns=['Survived','Name','Sex','Ticket','Cabin','Embarked'])

# Afficher l'en-tête de l'ensemble de données prétraitées
encoded_data.head()

# Afficher les informations générales sur les colonnes et les valeurs prétraitées
encoded_data.info()


