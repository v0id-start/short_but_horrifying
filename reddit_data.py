import pandas as pd
import nlp_tools
import matplotlib.pyplot as plt
import seaborn as sns


class RedditData:
    """
    Assumes a 'text' column exists
    """
    def __init__(self, csv_path):
        # self.csv_path = csv_path
        self._data = pd.read_csv(csv_path)
        nlp_tools.append_sentiment_from_col(self._data, 'text')

        self._avg_sentiment = self._data['sentiment'].mean()

    def avg_sentiment(self):
        return self._avg_sentiment

    def graph_score_vs_sentiment(self):
        plt = sns.relplot(data=self._data, kind="scatter", x="sentiment", y="score")
        plt.set(title="Post Score Vs Sentiment")
        plt.savefig("score_vs_sentiment.png")

    def create_word_cloud(self):
        pass