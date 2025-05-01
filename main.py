import praw

reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YourUserAgent'
)
import json
import os
import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string if soup.title else ""
    except:
        return ""

def crawl_subreddit(subreddit_name, output_dir, target_size_mb=500):
    subreddit = reddit.subreddit(subreddit_name)
    posts_data = []
    file_index = 0
    current_size = 0
    max_size = 10 * 1024 * 1024  # 10MB

    for post in subreddit.hot(limit=None):
        post_data = {
            'id': post.id,
            'title': post.title,
            'author': str(post.author),
            'score': post.score,
            'url': post.url,
            'selftext': post.selftext,
            'created_utc': post.created_utc,
        }

        # Add title of linked page if it's an HTML link
        if post.url.startswith('http') and not post.url.endswith(('.jpg', '.png', '.gif')):
            post_data['linked_title'] = get_page_title(post.url)

        json_line = json.dumps(post_data) + '\n'
        posts_data.append(json_line)
        current_size += len(json_line.encode('utf-8'))

        # Save file when reaching 10MB
        if current_size >= max_size:
            with open(os.path.join(output_dir, f"posts_{file_index}.json"), 'w') as f:
                f.writelines(posts_data)
            posts_data = []
            file_index += 1
            current_size = 0

        # Stop when reaching 500MB
        if file_index * 10 >= target_size_mb:
            break

    # Write remaining data
    if posts_data:
        with open(os.path.join(output_dir, f"posts_{file_index}.json"), 'w') as f:
            f.writelines(posts_data)
