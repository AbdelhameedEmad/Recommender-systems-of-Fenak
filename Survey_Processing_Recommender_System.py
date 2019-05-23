#Making recommendations from yelp dataset from ratings
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#importing the dataset and cleaning it from null value
df = pd.read_csv("yelp_business.csv")
data = df[["business_id", "name", "city", "categories","stars"]]
data = data.fillna("Giza")
data = data.sample(frac=0.06, replace=True)

# #printing all cities in the dataset
# print(pd.unique(data.city).tolist())

#preparing the values that will be inputed in the final list function
def recommendations(books, crafts, culture, food, outdoor,data):

    #Recommending the businesses which ratings is >= 3
    data = data[data['stars'] >= 3]

#     #Recommending the businesses that are in the city the user is in
#     data = data[data['city'] == city]

    # finding the first location that contains the inputed tag
    #needs the indexing to be numbers not name so use before (data = data.set_index('name'))
    def find_business(tag, data):
        wanted_business = data.iloc[0]
        #3 in data.iloc[0,3] is the number of the column of categories
        r = data.iloc[0,3]
        if r.find(tag) != -1:
            wanted_business = data.iloc[0]
            return (wanted_business['name'])
        else:
            i = 1
            while i < data.size:
                r = data.iloc[i,3]
                if r.find(tag) != -1:
                    wanted_business = data.iloc[i]
                    return (wanted_business['name'])
                    break
                if i == data.size - 1:
                    return ('N/a')
                i += 1

    #Creating the final list
    #creating the list of recommendations

    def final_list(list1,num1,list2,num2,list3,num3,list4,num4,list5,num5):
        def creating_clone(list1):
            z = 0
            clone = [0] * len(list1)
            for i in list1:
                clone[z] = i
                z += 1
            return clone

        final_list = []
        list_of_lists = [list1,list2,list3,list4,list5]
        numbers_of_lists = [num1,num2,num3,num4,num5]
        quarter_of_numbers_list = [round(i/4) for i in numbers_of_lists]

        j = 0
        for i in quarter_of_numbers_list:
            if i <= 4:
                quarter_of_numbers_list[j] = i * 2
            j += 1

        #getting the final list
        list_of_locations = []
        even_num_list = []
        even_list_of_lists = []
        j = 0
        c = 0

        for i in numbers_of_lists:
            if i > ((1/len(list_of_lists))*100):
                list_of_locations.append(j)
            j += 1


        for i in list_of_locations:
            num = quarter_of_numbers_list[i]
            even_num_list.append(num)


        for i in list_of_locations:
            l = list_of_lists[i]
            even_list_of_lists.append(l)

        while c < 4:
            clone_even_num_list = creating_clone(even_num_list)
            clone_quarter_of_numbers_list = creating_clone(quarter_of_numbers_list)
            if c % 2 == 0:
                flag = True
                while flag:
                    count = 0
                    flag_counter = 0
                    while count < len(clone_even_num_list):
                        if clone_even_num_list[count] == 0:
                            flag_counter += 1
                            count += 1
                        else:
                            flag_counter = 0
                            current_list = even_list_of_lists[count]
                            similarity_counter = 0
                            similarity_flag = True
                            while similarity_flag:
                                if current_list[similarity_counter] not in final_list:
                                    final_list.append(current_list.pop(similarity_counter))
                                    similarity_flag = False
                                else:
                                    similarity_counter += 1
                            even_list_of_lists[count] = current_list
                            clone_even_num_list[count] = clone_even_num_list[count] - 1
                            count += 1
                        if flag_counter >= len(clone_even_num_list):
                            flag = False
            else:
                flag = True
                while flag:
                    count = 0
                    flag_counter = 0
                    while count < len(clone_quarter_of_numbers_list):
                        if clone_quarter_of_numbers_list[count] == 0:
                            flag_counter += 1
                            count += 1
                        else:
                            flag_counter = 0
                            current_list = list_of_lists[count]
                            similarity_counter = 0
                            similarity_flag = True

                            while similarity_flag:
                                if current_list[similarity_counter] not in final_list:
                                    final_list.append(current_list.pop(similarity_counter))
                                    similarity_flag = False
                                else:
                                    similarity_counter += 1

                            list_of_lists[count] = current_list
                            clone_quarter_of_numbers_list[count] = clone_quarter_of_numbers_list[count] - 1
                            count += 1
                        if flag_counter >= len(clone_quarter_of_numbers_list):
                            flag = False
            c += 1

        return final_list

    #top 100 recommended locations similar to the inputed location
    #needs the indexing to be names (data = data.set_index('name'))

    def top100(title, data):
        count = CountVectorizer()
        count_matrix = count.fit_transform(data['categories'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        indices = pd.Series(data.index)
        recommended_places = []
        idx = indices[indices == title].index[0]
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
        top_100_indexes = list(score_series.iloc[0:100].index)
        for i in top_100_indexes:
            recommended_places.append(list(data.index)[i])
        return recommended_places

    final_recommendation = []
    tag1 = 'Books'
    tag2 = 'Crafts'
    tag3 = 'Arts'
    tag4 = 'Restaurant'
    tag5 = 'Active'
    book_store = find_business(tag1, data)
    crafts_store = find_business(tag2, data)
    cultural_center = find_business(tag3, data)
    restaurant = find_business(tag4, data)
    travel = find_business(tag5, data)
    data = data.set_index('name')
    book_stores_list = top100(book_store,data)
    crafts_stores_list = top100(crafts_store,data)
    cultural_centers_list = top100(cultural_center,data)
    restaurants_list = top100(restaurant,data)
    travel_list = top100(travel,data)
    total_ratings = books + crafts + culture + food + outdoor
    number_of_book_stores = round((books / total_ratings)*100)
    number_of_crafts = round((crafts / total_ratings)*100)
    number_of_cultural_center = round((culture / total_ratings)*100)
    number_of_restaurants = round((food / total_ratings)*100)
    number_of_activities = round((outdoor / total_ratings)*100)
    final_recommendation = final_list(book_stores_list,number_of_book_stores,crafts_stores_list,number_of_crafts,cultural_centers_list,number_of_cultural_center,restaurants_list,number_of_restaurants,travel_list,number_of_activities)
    return final_recommendation
