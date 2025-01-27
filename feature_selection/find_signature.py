#!/usr/bin/python
import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../your_word_data.pkl" 
authors_file = "../your_email_authors.pkl"
word_data = pickle.load( open(words_file, "rb"))
authors = pickle.load( open(authors_file, "rb") )


### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

# print(features_train)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()



### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

# print(features_train)

# ct = 0
# for w in features_train:
#     if w == 'sara':
#         ct = ct + 1
# print("Ct Sara::", ct)

# ctt = 0
# for w in features_train:
#     if w == 'chris':
#         ctt = ctt + 1
# print("Ct Chris::", ctt)

### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

acc = accuracy_score(pred, labels_test)
print("len:", len(features_train))
print("acc:", acc)

fis = clf.feature_importances_
maxi = 0
mi = None
for (i, n) in enumerate(fis):
    if n > maxi:
        maxi = n
        mi = i
print(mi, maxi)
print()

fn = vectorizer.get_feature_names()
print("==================")
print(fn[mi])

