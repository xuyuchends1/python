import pandas as pd

usernames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('source\\users.dat', sep='::', header=None, names=usernames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('source\\ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('source\\movies.dat', sep='::', header=None, names=mnames)

data=pd.merge(pd.merge(ratings,users),movies)
print (data)