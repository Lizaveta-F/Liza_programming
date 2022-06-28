from pathlib import Path
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
    years = [year[-5:-1] for year in films]
    years_ratings = dict(zip(years, ratings))
    with open('top250_movies.txt', 'w') as finp:
    # to write films' names in file top250_movies.txt
        finp.writelines("\n".join(films))        
    with open('ratings.txt', 'w') as fr:
        # to write ratings in file ratings.txt
        fr.writelines("\n".join(ratings))
    with open('years.txt', 'w') as fw:
        # to write years and ratings in file years.txt
        json.dump(years_ratings, fw, indent='\t')        
    print(*columns, sep='\n')  # extracted columns' names    
    fh1.close()
else:
    print(f'The file {path_to_file} does not exist')
