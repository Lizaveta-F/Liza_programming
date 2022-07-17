from pathlib import Path
import matplotlib.pyplot as plt
import json
path_to_file = 'ratings.list'
path = Path(path_to_file)

if path.is_file():
    fh1 = open('ratings.list', 'r')
    top250 = [line.strip() for line in fh1.readlines()]
    columns = (top250[27:278][0]).split()
    columns1 = (top250[28:278])
    alldata = [column.split('  ') for column in columns1]
    films = [film[3] for film in alldata]
    ratings = [rating[2] for rating in alldata]
    years = [year[year.find('(')+1:year.find(')')] for year in films]
    years_ratings = dict(zip(years, ratings))

    # In case top250 films are note rated( extracted from the original data with all the films)
    # all=(top250[296:789452])
    # alldata1=[column.split('   ') for column in all]
    # films1=[film[-1] for film in alldata1]
    # films2=[film[film.find('"')+1:] for film in films1]
    # years1=[year[year.find('(')+1:year.find(')')] for year in films1]
    # ratings1=[rat[:3].replace('!@#%^&*()-+=_?:/\';№" ',"") for rat in films1]
    # films_ratings1=dict(zip(films2,ratings1))
    # films_ratings2=dict(sorted(films_ratings1.items(),key=lambda x:x[1],reverse=True)[:251])

    with open('top250_movies.txt', 'w') as finp:
        # to write films' names in file top250_movies.txt
        finp.writelines("\n".join(films))
    with open('ratings.txt', 'w') as fr:
        # to write ratings in file ratings.txt
        plt.xlabel('rating')
        plt.hist(sorted(ratings), bins=20, histtype='stepfilled', color='blue')
        plt.show()
        fr.writelines("\n".join(ratings))
    with open('years.txt', 'w') as fw:
        # to write years and ratings in file years.txt
        plt.xlabel('years')
        plt.xticks(rotation=90)
        plt.hist(sorted(years), bins=20, histtype='stepfilled', color='orange')
        plt.show()
        json.dump(years_ratings, fw, indent='\t')

        # In case top250 films are note rated( extracted from the original data with all the films)
        # with open('gistograma_years.txt','w') as newly:
        #     json.dump(films_ratings2, newly, indent='\t')

    print(*columns, sep='\n')  # extracted columns' names
    fh1.close()
else:
    print(f'The file {path_to_file} does not exist')
