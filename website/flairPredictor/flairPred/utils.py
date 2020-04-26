import sys
import sklearn
import pickle
import praw
import re
from bs4 import BeautifulSoup
import nltk
# nltk.download('all')
from nltk.corpus import stopwords
import os
reddit = praw.Reddit(client_id='#', client_secret='#',
                     user_agent='#')

dirname = os.path.dirname(__file__)

model = pickle.load(
    open(os.path.join(dirname, 'model_2.sav'), 'rb'))

# open('E:\\MIDAS\\Flair-Detection\\model\\model_logreg_71.sav', 'rb'))

replace_with_space = re.compile('[/(){}\[\]\|@,;]')
deleteSymbol = re.compile('[^0-9a-z #+_]')
stopwords = set(stopwords.words('english'))


def cleanText(text):
    text = BeautifulSoup(text, "lxml").text  # HTML decoding
    text = text.lower()  # lowercase text
    # replace certain symbols by space in text
    text = replace_with_space.sub(' ', text)
    text = deleteSymbol.sub('', text)  # delete symbols from text
    # remove stopwords from text
    text = ' '.join(word for word in text.split() if word not in stopwords)
    return text


def predictFlair(url):
    submission = reddit.submission(url=url)

    post = {
        "title": str(submission.title),
        "body": str(submission.selftext),
    }
    comments = ""
    for comment in submission.comments:
        comments = comments + ' ' + comment.body
    post["comments"] = comments
    data = post['title'] + ' ' + post['comments'] + ' ' + post['body']

    return model.predict([data])


def predictutil(filename):
    result = {}
    with open(filename, 'r') as file:
        count = 0
        for link in file:
            result[link.strip()] = str(predictFlair(link.strip())[0])
            count += 1
        if count == 0:
            return None
    return result


if __name__ == "__main__":
    inputFile = sys.argv[1]
    predictutil(inputFile)
