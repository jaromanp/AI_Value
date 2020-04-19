# Pandas is used for data manipulation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

LABELS = ["Bad","Good"]

#Confusion Matrix
def mostrar_resultados(y_test, pred_y):
    conf_matrix = confusion_matrix(y_test, pred_y)
    plt.figure(figsize=(8, 8))
    sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d");
    plt.title("Confusion matrix")
    plt.ylabel('True class')
    plt.xlabel('Predicted class')
    plt.show()
    print (classification_report(y_test, pred_y))


# Read in data as pandas dataframe and display first 5 rows
features = pd.read_csv("Dataset-de-empresas.csv")
print(features.head(5))
#print('The shape of our features is:', features.shape)
print(pd.value_counts(features['Clase'], sort = True))

# Descriptive statistics for each column
# print(features.describe())

# Labels are the values we want to predict
labels = np.array(features['Clase'])

# Remove the labels from the features
# axis 1 refers to the columns
features= features.drop('Clase', axis = 1)


# Saving feature names for later use
feature_list = list(features.columns)

# Convert to numpy array
features = np.array(features)

# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.3,random_state = 42)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

# Crear el modelo con 100 arboles
model = RandomForestClassifier(n_estimators=100, 
                               bootstrap = True,verbose=2,
                               max_features = 'sqrt')

# Train the model on training data
model.fit(train_features, train_labels)

# Use the forest's predict method on the test data
predictions = model.predict(test_features)

# Probabilities for each class
rf_probs = model.predict_proba(test_features)[:, 1]
print(rf_probs)

#Confusion Matrix
mostrar_resultados(test_labels, predictions)

# Calculate roc auc
roc_value = roc_auc_score(test_labels, rf_probs)

print(roc_value)




