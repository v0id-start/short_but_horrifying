## Utilizes NLP tools to analyze characteristics of stories from the r/TwoSentenceHorror subreddit.
### TwoSentenceHorror is an open source community where users contribute stories that invoke feelings of horror in two sentences.

<br>

# Setup Instructions for Anaconda:
1. Create a new Anaconda environment with Python version 3.8 (Anaconda version 4.8.3)
2. Run the following commands in the anaconda environment to install the required packages

- conda install -c conda-forge praw
- conda install pandas
- conda install -c conda-forge textblob
- conda install matplotlib
- conda install seaborn
- conda install -c conda-forge wordcloud
- python -m textblob.download_corpora

To run reddit_loader.py to scrape posts:
1. Create a reddit account if you do not already have one, sign in
2. Go to https://www.reddit.com/prefs/apps
3. Click the 'Create another app' button
4. Give the app a name
5. For the redirect uri you should choose http://localhost:8080
6. Enter your app information in the following fields in reddit_loader.py
- CLIENT_ID = ''
- SECRET = ''
- AGENT_NAME = ''
- where your CLIENT_ID is under 'personal use script',
- SECRET is by 'secret',
- and AGENT_NAME is the name of your app

## Frequent Nouns
![Alt text](/noun_wordcloud.png?raw=true "")


## Frequent Verbs
![Alt text](/verb_wordcloud.png?raw=true "")

## Frequent Adjectives
![Alt text](/adj_wordcloud.png?raw=true "")

## Post Score vs Number of Words
![Alt text](/score_vs_num_words.png?raw=true "")

## Post Score vs Story Sentiment
![Alt text](/score_vs_sentiment.png?raw=true "")




