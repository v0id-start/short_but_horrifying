from reddit_loader import scrape_top_posts_from_sub
from reddit_data import RedditData


"""
TODO:
- Graph relationship between upvotes and sentiment
- Calculate top word frequencies
- Average number of words for top vs controversial?
- Generate overall word cloud
- Calculate most frequent part of speech
- Word cloud of adjectives to show what's considered good horror adjectives
- More unit tests :(
- Tone angry, sad ?
- Adjectives
"""


def main():
    short_horror = RedditData("post_data_top_1000.csv")
    print(short_horror.avg_sentiment())

    #short_horror.graph_score_vs_sentiment()

    short_horror.show_word_cloud()

    # short_horror.part_of_speech()
    # short_horror.top_adjectives()
    # short_horror.adjectives_word_cloud()

# 0.03665471503182279 top
# 0.014906574114416501 controversial


if __name__ == "__main__":
    main()