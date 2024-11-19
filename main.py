import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure the lexicon is downloaded
nltk.download('vader_lexicon')


# Function to analyze sentiment
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)

    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


# Main function to test the sentiment analysis
if __name__ == "__main__":
    test_texts = [
        "I love this product, it's amazing!",
        "This is the worst experience ever!",
        "It's an okay product, nothing special."
    ]

    for text in test_texts:
        result = analyze_sentiment(text)
        print(f"Text: {text}\nSentiment: {result}\n")