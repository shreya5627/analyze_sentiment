# Importing the Requirements
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sys

arg_count = len(sys.argv)

# Check Command Line Arguments are sufficient to proceed
if arg_count!=2:
    raise Exception("Arguments provided are more or less than needed")


# Function to Predict the Sentiment
def predict_sentiment(clean_text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(clean_text)
    max_score = max(sentiment["pos"], sentiment["neg"], sentiment["neu"])
    if max_score==sentiment["pos"]:
        return "Positive Sentiment"
    elif max_score==sentiment["neg"]:
        return "Negative Sentiment"
    return "Neutral Sentiment"     


# To gather the words which are non-sentimental
stopwords = nltk.corpus.stopwords.words("english")

# Initialising the file to be analysed
file_name = sys.argv[1]
text_file = open(file_name, "r+", errors="ignore")
text= text_file.read()

# Cleaning the data received from file
words = [w.lower() for w in nltk.word_tokenize(text) if w.lower() not in stopwords]
clean_text = " ".join(words)

# Predicting the sentiment
print(predict_sentiment(clean_text))