import pandas as pd
#Read file
df = pd.read_csv("train.tsv", sep = "\t")
df = df.sample(frac = 0.5)
#Keep only positive phrase and negative phrase
df = df.drop(df[df.Sentiment == 1].index)
df = df.drop(df[df.Sentiment == 2].index)
df = df.drop(df[df.Sentiment == 3].index)
#Change positive phrase sentiment rate into 1
df.loc[df.Sentiment == 4, “Sentiment”] = 1
#Some Sentence have integers in it, map all phrase make sure they converted into string so we can make CountVector
df.Phrase = df.Phrase.map(str)
#Split data into features and targets
x = df.Phrase
y = df.Sentiment
#Split datainto train and test by 1/5 ratio
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=24)
#Vectorizing the text data
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
ctmTr = cv.fit_transform(X_train)
#Use CountVector we get from train data, apply it to test data
X_test_dtm = cv.transform(X_test)
from sklearn.linear_model import LogisticRegression
#Training the model with simple Logistic Regression
lr = LogisticRegression()
lr.fit(ctmTr, y_train)
#Accuracy score
lr_score = lr.score(X_test_dtm, y_test)
print(“Results for Logistic Regression with CountVectorizer”)
print(lr_score)
#Show each sentence and its prediction.
predictions = lr.predict(X_test_dtm)
print(pd.DataFrame({“sentence”: X_test, “predictions”: predictions}))