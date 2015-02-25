# Popular Posts
Scrape the most popular posts from any WordPress blog

Demo: [http://popularposts.herokuapp.com/](http://popularposts.herokuapp.com/)

## Installation Instructions

Python Version 3.3.1

Flask Version 0.10.1

## Step 1

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
