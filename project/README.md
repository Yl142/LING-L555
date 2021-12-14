# Movie Review Sentiments Prediction
By Yuxuan Liu

We often leave our comments to movies based on our preference and feelings about the movie itself. The comment page is often composed with the sentiment (“Like/Dislike”) section and a textbox to leaving reviews. Some words in the textbox also indicates the sentiment of the audience that can be comprehended by only looking at the reviews not the sentimental check marks. This project will predict the sentiments of the audience by the text review part.

To accomplish those goals, I decided to use the skilearn package in Python. The designed application would be processing a dataset from [Kaggle](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data?select=train.tsv.zip) with movie reviews. I will clean the data to make it easy to be comprehended. I will split the data to a training set and a test set to train the model. And last step make predictions based on the original text reviews and see how well the predicted results fits the real result by looking at the fitting score. 

(I changed the project topic since I think the former topic Palindrome Finder for Documents is kind of trivial, so I decided to try this one as the topic. )
