"""
Ethan Price
Section AC
Driver file to analyze top posts
from the r/TwoSentenceHorror subreddit using NLP
techniques and generate figures
"""


from reddit_data import RedditData


def main():
    # Load CSVs
    short_horror = RedditData("post_data_top_1000.csv")
    controversial = RedditData("post_data_controversial_1000.csv")

    # Sentiment Analysis
    print("Top Posts Average Sentiment:", short_horror.avg_sentiment())
    print("Controversial Posts Average Sentiment:",
          controversial.avg_sentiment())

    short_horror.graph_score_vs_sentiment("score_vs_sentiment.png")

    # Word Frequency Analysis
    short_horror.create_word_cloud("all_wordcloud.png", "any")
    short_horror.create_word_cloud("noun_wordcloud.png", "noun")
    short_horror.create_word_cloud("adj_wordcloud.png", "adjective")
    short_horror.create_word_cloud("verb_wordcloud.png", "verb")

    # Word Count Analysis
    short_horror.graph_score_vs_num_words("score_vs_num_words")

    print("Top Posts Average Word Count:", short_horror.get_avg_word_len())
    print("Controversial Posts Average Word Count:",
          controversial.get_avg_word_len())


if __name__ == "__main__":
    main()