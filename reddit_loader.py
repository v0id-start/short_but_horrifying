"""
Ethan Price
Section AC
Uses the Reddit API PRAW to scrape metadata/content
from the top posts of all time in a subreddit
"""


import praw
import pandas as pd

# API Instance Information
CLIENT_ID = 'BI7m1CCdauRcf87m2fzt1w'
SECRET = 'N9cT733BnsEcbVlsNydU_5fTu8zbhQ'
AGENT_NAME = 'Short Horror Scraper'

# Subreddit Data
NUM_POSTS = 1000
FILE_NAME = "post_data.csv"
SUBREDDIT = "TwoSentenceHorror"
EXCLUDED_FLAIRS = ["⭐ANNOUNCEMENT⭐"]

def main():
    scrape_top_posts_from_sub(SUBREDDIT, NUM_POSTS, EXCLUDED_FLAIRS, FILE_NAME)


def scrape_top_posts_from_sub(sub_name, post_limit, excluded_flairs, file_name="post_data.csv"):
    """
    Scrapes the number of specified top posts
    of all time from the given subreddit with
    title and body text combined, writes the data to a csv file
    :param sub_name: name of subreddit to scrape
    :param post_limit: number of top posts to scrape
    :param excluded_flairs: list of flairs to ignore while scraping
    :param file_name: name of csv file to write to
    :return: pandas dataframe with top posts from subreddit
    """
    reddit_app = praw.Reddit(client_id=CLIENT_ID, client_secret=SECRET,
                             user_agent=AGENT_NAME)

    top_posts = reddit_app.subreddit(sub_name).top(time_filter="all",
                                                   limit=post_limit)

    post_data = []

    for post in top_posts:
        if post.link_flair_text not in excluded_flairs:
            story = post.title + " " + post.selftext
            post_data.append([story, post.score, post.id, post.num_comments])

    posts = pd.DataFrame(post_data, columns=['text', 'score', 'id', 'num_comments'])
    posts.to_csv(file_name)


if __name__ == '__main__':
    main()