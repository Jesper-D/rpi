# First we import the csv library and the dataset 

import csv

with open ('/home/pi/RSL/userReviews.csv') as data:
    readdata = csv.reader(data)
    header = next(readdata)
    data = list(readdata)
    
movies = data[:][0]
for i in range(0,1000):
    movies = [data[i][0].split(';') for i in range (0,1000)]

#1 The new variable X is a list of all authors. I used a range (0-1000) since the dataset has >200000 reviews. Nevertheless, the code indicates that I know how to create this new list.

X = []
for i in range(0,1000):
    X += [movies[i][2]]
print('Authors first 1000 reviews:', X)

#2 The new variable Y is a list of all reviews of my favourite movie Aquarius. I use a range, and here I filter and append the reviews that have aquarius as their value to list Y. 

Y = []
favmovie = 'aquarius'
for i in range(0,1000):
    if movies[i][0] == favmovie:
        Y += [movies[i][2]]
print('All reviews of favourite movie:', Y)

#3 The final new variable is Z, and it is a list of all movies watched by the reviewers of Aquarius. This could be interesting to me since the reviewers might have a similar taste in movies as me.
# I filter and append the movies to list Z. But, since there are duplicates in the list, I create list Z2 based on Z and filter out the duplicate values. 

Z = []
for j in range (0, len(Y)):
    watched = Y[j]
    for i in range (0,1000):
        if movies[i][2] == watched:
            Z += [movies[i][0]]

Z2 = set()
for x in Z:
    Z2.add(x)
print ('Movies watched by Aquarius reviewers:', Z2)