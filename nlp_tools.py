"""
Ethan Price
Section AC
Contains functions to analyze text using
natural language processing techniques
as well as generating word cloud visuals
"""


from textblob import TextBlob
from wordcloud import STOPWORDS
from wordcloud import WordCloud


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


def create_word_cloud(file_name, text, pos, exclusions=None, bg_color="black"):
    """
    Generates and saves a word cloud visual
    image from the given text with the given
    word exclusions.
    :param file_name: name of new saved file
    :param text: text to generate word cloud from
    :param pos: part of speech to generate word cloud of,
    options are 'any', 'noun'. 'adjective', 'verb'.
    :param exclusions: list of strings to exclude from
    word cloud
    :param bg_color: background color of word cloud
    :return: None
    """
    if exclusions is None:
        exclusions = [""]

    pos_to_tag = {
        "noun": "NN",
        "adjective": "JJ",
        "verb": "VB"
    }

    wc_text = text

    if pos != "any":
        try:
            all_text = TextBlob(str(wc_text))

            parts = [word for (word, tag) in all_text.tags
                     if tag == pos_to_tag[pos]]

            wc_text = " ".join(parts)
        except Exception:
            print("Invalid Part of Speech")
            return

    excluded_words = exclusions + list(STOPWORDS)
    all_text_wordcloud = WordCloud(stopwords=excluded_words,
                                   background_color=bg_color,
                                   width=1200,
                                   height=600).generate(str(wc_text))

    all_text_wordcloud.to_file(file_name)