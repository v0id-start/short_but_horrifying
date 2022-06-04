"""
Ethan Price
Section AC
RedditData represents data collected
from a subreddit as a pandas dataframe.
Contains functionality to inspect characteristics
of the text data using NLP and generate figures.
"""


import pandas as pd
import nlp_tools
import seaborn as sns


class RedditData:
    """
    Represents data from reddit posts,
    contains functionality to calculate text
    features and generate visualizations
    """
    def __init__(self, csv_path):
        """
        Initializes reddit data from the given
        csv file, expects columns 'text' and 'sentiment'
        :param csv_path: path of csv containing reddit data
        """
        self._data = pd.read_csv(csv_path)
        # Append the sentiment value of the text for each entry
        nlp_tools.append_sentiment_from_col(self._data, 'text')
        # Append the word count for each entry
        self._data['num words'] =\
            self._data['text'].apply(lambda x: len(x.split()))

    def avg_sentiment(self):
        """
        :return: The average sentiment value of
        the text from the current data
        """
        return self._data['sentiment'].mean()

    def get_avg_word_len(self):
        """
        :return: The average number of words
        per entry from the text of the current data
        """
        return self._data['num words'].mean()

    def graph_score_vs_sentiment(self, file_name):
        """
        Generates and saves a scatter plot of
        score (upvotes) vs text sentiment
        of the current data to the given file name
        :param file_name: name of new saved file
        :return: None
        """
        scatter_plt = sns.relplot(data=self._data,
                                  kind="scatter", x="sentiment", y="score")
        scatter_plt.set(title="Post Score Vs Sentiment")
        scatter_plt.savefig(file_name)

    def graph_score_vs_num_words(self, file_name):
        """
        Generates and saves a scatter plot of
        score (upvotes) vs number of words
        of the current data to the given file name
        :param file_name: name of new saved file
        :return: None
        """
        scatter_plt = sns.relplot(data=self._data,
                                  kind="scatter", x="num words", y="score")
        scatter_plt.set(title="Post Score Vs Num Words")
        scatter_plt.savefig(file_name)

    def create_word_cloud(self, file_name, part_of_speech="any"):
        """
        Generates and saves a word cloud visual
        image from all story text within the current data
        with specific word exclusions.
        :param file_name: name of new saved file
        :param part_of_speech: part of speech to generate word cloud of
        :return: None
        """
        wc_text = self._data['text'].values
        exclusions = ["s", "t"]
        nlp_tools.create_word_cloud(file_name, wc_text,
                                    part_of_speech, exclusions, "black")