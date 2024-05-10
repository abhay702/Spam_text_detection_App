import streamlit as st
import pickle
import sklearn
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize the stemmer
ps = PorterStemmer()


def transform_text(text):
    # converting the text into lower case
    text = text.lower()
    # Tokenizing words - sperating words
    text = nltk.word_tokenize(text)

    # Removing Special Character
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    # Removing stopwords
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    # Stemming of words done here
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button("Predict"):

    # 1.Preprocessing
    transformed_sms = transform_text(input_sms)
    # 2.Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3.Predict
    result = model.predict(vector_input)[0]
    # 4.Display
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')

