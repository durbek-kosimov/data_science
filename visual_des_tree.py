# Export the model in visual format
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data = pd.read_csv('music.csv')  # import data set
X = music_data.drop(columns=['genre']) # create input set
y = music_data['genre']                # create output set

model = DecisionTreeClassifier()       # create a model   
model.fit(X, y)                        # Train the model

tree.export_graphviz(model, out_file='music-recommender.dot',
                    feature_names=['age', 'gender'],
                    class_names=sorted(y.unique()), # displays the class for each note
                    label='all',                    # every not has been labeled that we can read
                    rounded=True,                   # rounded coners
                    filled=True)                    # each note or each box filled with color
