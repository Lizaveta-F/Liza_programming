# Города и страны
# Заданы N стран, включающие в себя города. Заданы Q запросов. Каждый запрос - название города,
# на который нужно вывести страну, к которому он относится (если относится).
# Формат ввода:
# В первой строки число N - количество стран
# Далее по порядку задаются страны одна за другой, каждая в следующем формате:
# В отдельной строке число K - количество городов в стране.
# В следующих K строках по одному городу (город может состоять из нескольких слов)
# После ввода городов задаётся Q - число запросов.
# В следующих Q строках задаются города (их может и не существовать).

# dict1={}
amount_countries = int(input("Enter the amount of countries: "))
dict_cc = {}
query = []
for _ in range(amount_countries):
    country = input("Enter a country: ")
    amount_cities = int(input("Enter the amount of cities: "))
    cities = []
    for _ in range(amount_cities):
        cities.append(input("Enter a city: "))
        dct_cc = {country: cities}
    dict_cc.update(dct_cc)
amount_queries = int(input("Enter the amount of queries: "))
for _ in range(amount_queries):
    query.append(input("Enter the query: "))
for i in query:
    print(", ".join([country for country in dict_cc if i in dict_cc[country]]))
