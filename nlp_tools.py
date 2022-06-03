from textblob import TextBlob

def append_sentiment_from_col(data, col):
    """
    Appends a new column 'sentiment' to a given dataframe
    with float sentiment values corresponding to the given col
    :param data: dataframe to append sentiment col to
    :param col: column name with text to analyze
    :return: None
    """
    data['sentiment'] = data[col].apply(get_sentiment)


def get_sentiment(text):
    """
    Returns the sentiment value for a given string of text
    :param text: string of text to analyze
    :return: sentiment value in interval [-1.0, 1.0] where
    -1.0 is most negative and 1.0 is most positive
    """
    return TextBlob(text).sentiment[0]


def get_part_of_speech(word):
    pass