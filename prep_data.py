import pandas as pd
music_data = pd.read_csv('music.csv')

# drop specified labels from rows and columns
X = music_data.drop(columns=['genre'])
y = music_data['genre']
