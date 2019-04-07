import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# finding the first location that contains the inputed tag
def find_business(tag, data):
    wanted_business = data.iloc[0]
    r = data.at[0, 'categories']
    if r.find(tag) != -1:
        wanted_business = data.iloc[0]
        return wanted_business['name']
    else:
        i = 1
        while i < data.size:
            r = data.at[i, 'categories']
            if r.find(tag) != -1:
                wanted_business = data.iloc[i]
                return wanted_business['name']
                break
            if i == data.size - 1:
                return 'N/a'
            i += 1

#top 100 recommended locations similar to the inputed location
def top100(title, data):
    count = CountVectorizer()
    count_matrix = count.fit_transform(data['categories'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    indices = pd.Series(data.index)
    recommended_places = []
    idx = indices[indices == title].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
    top_100_indexes = list(score_series.iloc[1:100].index)
    for i in top_100_indexes:
        recommended_places.append(list(data.index)[i])
    return recommended_places

#Creating the final list
def final_list(list1,num1,list2,num2,list3,num3,list4,num4,list5,num5):
    final_list = []
    list_of_lists = [list1,list2,list3,list4,list5]
    numbers_of_lists = [num1,num2,num3,num4,num5]
    top3_lists_locations = []
    #getting top 3 favorite lists locations
    i = 0
    while i < 3:
        j = 0
        max = numbers_of_lists[0]
        max_location = 0
        while j < len(numbers_of_lists):
            if max < numbers_of_lists[j]:
                max = numbers_of_lists[j]
                max_location = j
            if j == (len(numbers_of_lists) - 1):
                numbers_of_lists[max_location] = -1
                top3_lists_locations.append(max_location)
            j += 1
        i += 1
    #getting the final list
    c = 0
    while c < 4:
        if c % 2 == 0:
            flag = True

    return final_list

#importing the dataset and cleaning it from null value
df = pd.read_csv("yelp_business.csv")
data = df[["business_id", "name", "city", "categories"]]
data = data.fillna("Giza")
data = data.sample(frac=0.01, replace=True)
data = data.set_index('name')

#preparing the values that will be inputed in the final list function
def recommendations(books, crafts, culture, food, outdoor,data = data):
    final_recommendation = []
    tag1 = 'Books'
    tag2 = 'Crafts'
    tag3 = 'Arts'
    tag4 = 'Restaurant'
    tag5 = 'Active life'
    book_store = find_business(tag1, data)
    crafts_store = find_business(tag2, data)
    cultural_center = find_business(tag3, data)
    restaurant = find_business(tag4, data)
    travel = find_business(tag5, data)
    book_stores_list = top100(book_store)
    crafts_stores_list = top100(crafts_store)
    cultural_centers_list = top100(cultural_center)
    restaurants_list = top100(restaurant)
    travel_list = top100(travel)
    total_ratings = books + crafts + culture + food + outdoor
    number_of_book_stores = round((books / total_ratings)*100)
    number_of_crafts = round((crafts / total_ratings)*100)
    number_of_cultural_center = round((culture / total_ratings)*100)
    number_of_restaurants = round((food / total_ratings)*100)
    number_of_activities = round((travel / total_ratings)*100)



