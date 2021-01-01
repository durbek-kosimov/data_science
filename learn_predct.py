import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

# Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y)
music_data

# Prediction
predictions = model.predict([[21, 1], [22, 0]])
predictions
