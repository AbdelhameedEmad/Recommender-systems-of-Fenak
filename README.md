# Fenak Mobile application

- Fenak is a mobile app which helps tourists by showing personalized recommendations to improve their tourism experience in Egypt.
- Help small businesses by recommending them to tourists.

![alt text](https://github.com/AbdelhameedEmad/Recommender-systems-of-Fenak/blob/master/Images/Fenak.png)

# Fenak Recommender systems

The Recommender systems are "Similar_Locations_Recommender" which is a content based recommender system which uses cosine similarity to recommend locations similar to the inputed location (which is the location liked by the user) and "Survey_Processing_Recommender_System" which is analysis the answer of new users to a simple survey as they rate the categories from 1-5 and use these ratings to give them intial recommendations.

![alt text](https://github.com/AbdelhameedEmad/Recommender-systems-of-Fenak/blob/master/Images/Content%20based%20recommender.png)

# Used Similarity Metric

I am using Cosine similarity to determine similarity between businesses, by trying to find cosine of the angle between the two businesses using their categories.

![alt text](https://github.com/AbdelhameedEmad/Recommender-systems-of-Fenak/blob/master/Images/soft-cosine.png)

# Used dataset

I am using yelp open dataset

![alt text](https://github.com/AbdelhameedEmad/Recommender-systems-of-Fenak/blob/master/Images/yelp-open-dataset.png)
