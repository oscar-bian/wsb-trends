# Stonksinsights 

This notebook utilises the Python Reddit wrapper to extract comments from the
hotest threads on the subreddit r/wallstreetbets, and a basic processing
to determine which stocks are the most discussed as well as whether or not they
are associated with a bullish or bearish sentiment. 

## instructions

````
pip -m venv wsb
source wsb/bin/activate
pip install -r requirements.txt
jupyter notebook wsb_comment_scrapper_v1.ipynb
````