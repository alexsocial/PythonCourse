"""
Alex Chaban
Due 02-09-2023
Prof. Ionut Cardei
COP4045
Problem 4
"""

import csv

"""
Early initialization of dictionaries and keeping the files open to read and use.
"""
rated = {}
grossings = {}

with open('imdb-top-rated.csv') as f: 
  rows=csv.DictReader(f, delimiter = ',')
  for row in rows:
    rated[row['Rank']] = row

with open('imdb-top-grossing.csv') as f:
    rows=csv.DictReader(f, delimiter = ',')
    for row in rows:
      grossings[row['Rank']] = row

"""
Part A: Top Collaborations
Displays all movies that an actor and a director have collaborated on.
Conditions: Two strings, a director and an actor. Case sensitive.
"""
def display_top_collaborations(director, actor):
    together_movies = []
    output = ""
    with open ('imdb-top-casts.csv', 'r', encoding = 'utf8') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            if director in row and actor in row:
                together_movies.append(row)
        values = list(rated.values())
        for i in together_movies:
            try:
                position = values.index(i[0])
            except ValueError:
                together_movies.remove(i)
    for i in range(len(together_movies)):
        output += together_movies[i][0]
        output += '\n'
    print(f"Movies that {director} and {actor} have worked on that are in the top 250:")
    print(output)
    f.close()

"""
Part B: Top Directors
Displays the highest grossing directors.
Conditions: The files exist in a local folder.
"""
def display_top_directors():
    directors = {}
    temp_director = []
    with open ('imdb-top-casts.csv', 'r', encoding = 'utf8') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            temp_director = list(row)
            money = 0
            try:
                key = str({i for i in grossings if grossings[i]['Title'] == temp_director[0]})
                new_key = ""
                for i in key:
                    if i.isdigit():
                        new_key = new_key + i
                money = grossings[new_key]['USA Box Office']
                if temp_director[2] in directors:
                    directors[temp_director[2]] += int(money)
                else:
                    temp_dict = {temp_director[2]: int(money)}
                    directors.update(temp_dict)
            except Exception as e:
                continue
    f.close()
    d_list = (sorted(directors.items(), key = lambda item: item[1],reverse = True))
    print ("List of top director's revenue: ")
    for i in range(len(d_list)):
        print(f"{i+1}: {d_list[i][0]}, ${d_list[i][1]}")
"""
algo:
get the directors and assure no duplicates
loop through the grossings list and update it based on director names
"""
def main():
    display_top_collaborations('Steven Spielberg', 'Harrison Ford')
    display_top_collaborations('Eric Darnell', 'Chris Rock')
    display_top_directors()




main()

    

