# import libraries
import csv 
import statistics

# read in data as reviews
with open ('./userReviews.csv','r',encoding='utf-8-sig') as data:
    reader = csv.DictReader(data, delimiter=';')
    reviews = list(reader)
    
# state favorite movie and score Jesper
favmovie = 'baby-driver'
score_jesper = 9.0

# compute m (average Metascore_w of favmovie Jesper)
A = []
for row in reviews:
    if row['movieName'] == favmovie:
        A.append(row['Metascore_w'])
        
for i in range(0,len(A)):
    A[i] = int(A[i])
    
m = statistics.mean(A)
print('m is',m)

# compute relative and absolute difference between score Jesper and m
print('Score Jesper is', score_jesper)
print('Score Jesper is',((9-m)/m)*100,'%','higher than m')
print('Score Jesper is',9-m,'higher than m')

# create list (B) of authors that reviewed favmovie
B = []
for row in reviews:
    if row['movieName'] == 'baby-driver':
        B.append(row['Author'])
#print(B)
        
# create list (C) of movies that have an equal or higher grade than m, only reviews of authors in list B are used
C = []
for row in reviews:
    if row ['Author'] in B and row ['Metascore_w'] >= '7.104167':
        C.append(row['movieName'])
# print(C)

# export list C as recommended_movies.csv

recommendations = zip(C)
with open('recommended_movies.csv','w') as results:
    writer = csv.writer(results)
    for row in recommendations:
        writer.writerow(recommendations)
        