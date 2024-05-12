
# Spam Text Classification

It is a user-friendly application built with Python that utilizes machine learning to classify incoming messages as spam or legitimate. The deployed app analyzes the content of your messages and identifies suspicious patterns often associated with spam, such as promotional language, urgency tactics, or unusual formatting. It empowers you to take control of your inbox by filtering out unwanted messages and protecting yourself from potential phishing scams.


## Introduction
This project showcases a simple yet effective solution for classifying text messages and emails as spam or not spam. Leveraging Python, Streamlit, and scikit-learn, this classifier provides an interactive web interface for users to input text and receive real-time predictions. The core components include Streamlit for the user interface, Pickle for model serialization, scikit-learn for machine learning functionality, and NLTK for text preprocessing tasks. By utilizing a TF-IDF vectorizer and a pre-trained machine learning model, this classifier accurately predicts the nature of incoming messages. The README provides an overview of the project's components and encourages contributions for further enhancements. Feel free to explore the code, contribute, and deploy your own instance of the Spam Text Classifier!
## Features

1. **Real-time Classification**: Instantly classify text messages or emails as spam or not spam through an intuitive web interface.

2. **Interactive User Interface**: Streamlit-powered interface allows users to input text and receive predictions with a single click.

3. **Accurate Predictions**: Utilizes a pre-trained machine learning model trained on labeled text data to provide accurate classification results.

4. **Text Preprocessing**: Implements text preprocessing techniques such as tokenization, removal of stopwords, and stemming to enhance prediction accuracy.

5. **TF-IDF Vectorization**: Converts text input into numerical feature vectors using TF-IDF vectorization, enabling the model to make predictions based on numerical representations of text.

6. **Easy Deployment**: Simple setup and deployment process, allowing users to deploy their own instance of the classifier with minimal effort.

7. **Scalability**: Designed with scalability in mind, enabling easy integration with existing systems or deployment on cloud platforms for handling large volumes of text data.

8. **Contribution Friendly**: Welcomes contributions from the community for adding new features, improving existing functionality, or enhancing performance.

## Screenshots

![image](https://github.com/abhay702/Spam_text_detection_App/assets/106369018/20b982d5-2336-441a-ab14-a52ca4d5a807)

![image](https://github.com/abhay702/Spam_text_detection_App/assets/106369018/ec82583f-d63e-4659-a973-68970d360105)

![image](https://github.com/abhay702/Spam_text_detection_App/assets/106369018/a4436155-ddd9-41ec-97e5-e62a26a37166)

## Installation

How to clone this app :

```bash
 git clone https://github.com/abhay703/Spam_text_detection_App.git
```
Navigate to the Project directory :

```bash
 cd spam-text-classifier
```

Install all the dependencies using pip :

```bash
pip install -r requirements.txt

```
Run the Streamlit app:

```bash
streamlit run app.py

```


## Examples

Simply put in the text which you wish to find weather it is Spam or Not Spam 



