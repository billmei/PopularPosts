# Popular Posts
Scrape the most popular posts from any WordPress blog

Demo: [http://popularposts.herokuapp.com/](http://popularposts.herokuapp.com/)

## TODO
- Quickly find the most popular posts of any blog (you happen upon a new blog and want a quick summary of it instead of scrolling chronologically)
- Enter a WordPress URL here, or enter an RSS feed here. (make sure you capture data about: timestamp, link to body text, and link to headline text)
- Also make sure you capture most popular (most common) URLs people are typing into the URL box.
- Return a list of posts ordered by "most popular"
- "Popular" determined by:
	- Linkbacks
	- Number of comments
	- Views (if there is a counter)
	- Shares on Facebook graph API
	- Retweets on Twitter API
- Later: Scrape a ton of blogs to collect data on what time you should post. ML project: Scrape WordPress blogs to see how the day of the week something is posted affects the popularity of the article. "What's the best day of the week to post something? Best time? How does the article's content/topic affect this?"
- Setting up an HTTPS website https://news.ycombinator.com/item?id=8472901

## Installation Instructions

Python Version 3.3.1

Flask Version 0.10.1

### Step 1

	$ git clone git@github.com:Kortaggio/PopularPosts.git
	$ cd PopularPosts

### Step 2

Install `virtualenv` and app requirements (use the `--no-site-packages` flag for Ubuntu versions):

	$ pip install virtualenv
	$ virtualenv -p python3 venv --no-site-packages
	$ source venv/bin/activate
	$ pip install -r requirements.txt

Generate a secret key and stick it into `/secret.txt`

### Step 3

Run with

	$ python run.py
