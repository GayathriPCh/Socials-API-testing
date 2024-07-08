from flask import Flask, redirect, request, url_for, session, render_template
import os
import requests
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# LinkedIn App credentials
LINKEDIN_CLIENT_ID = 'your-linkedin-id'  # Replace with your LinkedIn app client ID
LINKEDIN_CLIENT_SECRET = 'your-linkedin-secret'  # Replace with your LinkedIn app client secret
LINKEDIN_REDIRECT_URI = 'http://127.0.0.1:5000/auth/linkedin/callback'  # Replace with your redirect URI configured in your LinkedIn app

# Reddit App credentials
REDDIT_CLIENT_ID = 'your-reddit-id'  # Replace with your Reddit app client ID
REDDIT_CLIENT_SECRET = 'your-reddit-secret'  # Replace with your Reddit app client secret
REDDIT_REDIRECT_URI = 'http://127.0.0.1:5000/auth/reddit/callback'  # Replace with your redirect URI configured in your Reddit app

# YouTube App credentials
YOUTUBE_CLIENT_ID = 'your-youtube-id'  # Replace with your YouTube app client ID
YOUTUBE_CLIENT_SECRET = 'your-youtube-secret'  # Replace with your YouTube app client secret
YOUTUBE_REDIRECT_URI = 'http://127.0.0.1:5000/auth/youtube/callback'  # Replace with your redirect URI configured in your YouTube app

# OAuth URLs for each service
LINKEDIN_AUTHORIZATION_URL = 'https://www.linkedin.com/oauth/v2/authorization'
LINKEDIN_ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
LINKEDIN_API_BASE_URL = 'https://api.linkedin.com/v2'

REDDIT_AUTHORIZATION_URL = 'https://www.reddit.com/api/v1/authorize'
REDDIT_ACCESS_TOKEN_URL = 'https://www.reddit.com/api/v1/access_token'
REDDIT_API_BASE_URL = 'https://oauth.reddit.com'

YOUTUBE_AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/auth'
YOUTUBE_ACCESS_TOKEN_URL = 'https://oauth2.googleapis.com/token'
YOUTUBE_API_BASE_URL = 'https://www.googleapis.com/youtube/v3'

# Scopes required for each service
LINKEDIN_SCOPES = ['openid', 'profile', 'w_member_social', 'email']
REDDIT_SCOPES = ['identity', 'read', 'history']
YOUTUBE_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube'
]

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to initiate LinkedIn OAuth login process
@app.route('/login')
def login():
    params = {
        'response_type': 'code',
        'client_id': LINKEDIN_CLIENT_ID,
        'redirect_uri': LINKEDIN_REDIRECT_URI,
        'scope': ' '.join(LINKEDIN_SCOPES)
    }
    auth_url = f"{LINKEDIN_AUTHORIZATION_URL}?{urlencode(params)}"
    return redirect(auth_url)

# Route to initiate Reddit OAuth login process
@app.route('/login/reddit')
def login_reddit():
    params = {
        'client_id': REDDIT_CLIENT_ID,
        'response_type': 'code',
        'state': 'random_string',
        'redirect_uri': REDDIT_REDIRECT_URI,
        'duration': 'temporary',
        'scope': ' '.join(REDDIT_SCOPES)
    }
    auth_url = f"{REDDIT_AUTHORIZATION_URL}?{urlencode(params)}"
    return redirect(auth_url)

# Route to initiate YouTube OAuth login process
@app.route('/login/youtube')
def login_youtube():
    params = {
        'client_id': YOUTUBE_CLIENT_ID,
        'redirect_uri': YOUTUBE_REDIRECT_URI,
        'response_type': 'code',
        'scope': ' '.join(YOUTUBE_SCOPES),
        'access_type': 'offline',
        'include_granted_scopes': 'true',
    }
    auth_url = f"{YOUTUBE_AUTHORIZATION_URL}?{urlencode(params)}"
    return redirect(auth_url)

# Callback route for LinkedIn OAuth authorization
@app.route('/auth/linkedin/callback')
def linkedin_callback():
    code = request.args.get('code')
    if code:
        access_token = get_linkedin_access_token(code)
        if access_token:
            session['access_token'] = access_token
            profile_data = fetch_linkedin_profile_data(access_token)
            if profile_data:
                session['profile'] = profile_data
                return redirect(url_for('profile'))
            else:
                return 'Failed to fetch profile data'
        else:
            return 'Failed to retrieve access token'
    else:
        return 'Authorization code not received'

# Callback route for Reddit OAuth authorization
@app.route('/auth/reddit/callback')
def reddit_callback():
    code = request.args.get('code')
    if code:
        access_token = get_reddit_access_token(code)
        if access_token:
            session['reddit_access_token'] = access_token
            return redirect(url_for('reddit_profile'))
        else:
            return 'Failed to retrieve access token'
    else:
        return 'Authorization code not received'

# Callback route for YouTube OAuth authorization
@app.route('/auth/youtube/callback')
def youtube_callback():
    code = request.args.get('code')
    if code:
        access_token = get_youtube_access_token(code)
        if access_token:
            session['youtube_access_token'] = access_token
            return redirect(url_for('youtube_profile'))
        else:
            return 'Failed to retrieve access token'
    else:
        return 'Authorization code not received'

# Route to display LinkedIn profile
@app.route('/profile')
def profile():
    if 'access_token' in session:
        profile_data = fetch_linkedin_profile_data(session['access_token'])
        if profile_data:
            return render_template('profile.html', profile=profile_data)
        else:
            return 'Failed to fetch profile data'
    else:
        return redirect(url_for('login'))

# Route to display Reddit profile
@app.route('/reddit_profile')
def reddit_profile():
    if 'reddit_access_token' in session:
        profile_data = fetch_reddit_profile_data(session['reddit_access_token'])
        if profile_data:
            return render_template('reddit_profile.html', profile=profile_data)
        else:
            return 'Failed to fetch profile data'
    else:
        return redirect(url_for('login_reddit'))

# Route to display Reddit posts
@app.route('/reddit_posts')
def reddit_posts():
    if 'reddit_access_token' in session:
        posts = fetch_reddit_posts(session['reddit_access_token'])
        if posts:
            return render_template('reddit_posts.html', posts=posts)
        else:
            return 'Failed to fetch posts'
    else:
        return redirect(url_for('login_reddit'))

# Route to display YouTube profile
@app.route('/youtube_profile')
def youtube_profile():
    if 'youtube_access_token' in session:
        profile_data = fetch_youtube_profile_data(session['youtube_access_token'])
        if profile_data:
            return render_template('youtube_profile.html', profile=profile_data)
        else:
            return 'Failed to fetch profile data'
    else:
        return redirect(url_for('login_youtube'))

# Function to retrieve YouTube access token
def get_youtube_access_token(code):
    data = {
        'code': code,
        'client_id': YOUTUBE_CLIENT_ID,
        'client_secret': YOUTUBE_CLIENT_SECRET,
        'redirect_uri': YOUTUBE_REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    response = requests.post(YOUTUBE_ACCESS_TOKEN_URL, data=data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(response.json())
        return None

# Function to fetch YouTube profile data
def fetch_youtube_profile_data(access_token):
    profile_url = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(profile_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch profile data: {response.json()}")
        return None

# Function to retrieve LinkedIn access token
def get_linkedin_access_token(code):
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': LINKEDIN_REDIRECT_URI,
        'client_id': LINKEDIN_CLIENT_ID,
        'client_secret': LINKEDIN_CLIENT_SECRET,
    }
    response = requests.post(LINKEDIN_ACCESS_TOKEN_URL, data=data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(response.json())
        return None

# Function to retrieve Reddit access token
def get_reddit_access_token(code):
    auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET)
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDDIT_REDIRECT_URI,
    }
    headers = {'User-Agent': 'YourApp/0.0.1'}
    response = requests.post(REDDIT_ACCESS_TOKEN_URL, auth=auth, data=data, headers=headers)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(response.json())
        return None

# Function to fetch LinkedIn profile data
def fetch_linkedin_profile_data(access_token):
    profile_url = f"{LINKEDIN_API_BASE_URL}/userinfo"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
    }
    response = requests.get(profile_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to fetch Reddit profile data
def fetch_reddit_profile_data(access_token):
    profile_url = f"{REDDIT_API_BASE_URL}/api/v1/me"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'User-Agent': 'YourApp/0.0.1'
    }
    response = requests.get(profile_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to fetch Reddit posts
def fetch_reddit_posts(access_token):
    profile_data = fetch_reddit_profile_data(access_token)
    if not profile_data:
        return None
    username = profile_data.get('name')
    if not username:
        return None
    posts_url = f"{REDDIT_API_BASE_URL}/user/{username}/submitted"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'User-Agent': 'YourApp/0.0.1'
    }
    response = requests.get(posts_url, headers=headers)
    if response.status_code == 200:
        posts = []
        data = response.json()
        for item in data.get('data', {}).get('children', []):
            post_data = item.get('data')
            if post_data:
                posts.append(post_data)
        return posts
    else:
        print(response.json())
        return None

# Route to render post creation form for LinkedIn
@app.route('/post')
def post_form():
    if 'access_token' in session:
        return render_template('post.html')
    else:
        return redirect(url_for('login'))

# Route to handle LinkedIn post creation
@app.route('/post', methods=['POST'])
def create_post():
    if 'access_token' in session:
        text = request.form.get('text')
        if text:
            if 'profile' not in session:
                return 'Profile data not found. Please log in again.'
            response = post_on_linkedin(session['access_token'], text)
            if response:
                return 'Post successfully created on LinkedIn!'
            else:
                return 'Failed to create post on LinkedIn'
        else:
            return 'No text provided for the post'
    else:
        return redirect(url_for('login'))

# Function to create a post on LinkedIn
def post_on_linkedin(access_token, text):
    profile = session.get('profile')
    if not profile:
        return False
    member_id = profile.get('sub')
    post_url = f"{LINKEDIN_API_BASE_URL}/ugcPosts"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0',
    }
    payload = {
        'author': f'urn:li:person:{member_id}',
        'lifecycleState': 'PUBLISHED',
        'specificContent': {
            'com.linkedin.ugc.ShareContent': {
                'shareCommentary': {
                    'text': text
                },
                'shareMediaCategory': 'NONE'
            }
        },
        'visibility': {
            'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
        }
    }
    response = requests.post(post_url, headers=headers, json=payload)
    if response.status_code == 201:
        return True
    else:
        print(response.json())
        return False

# Route to fetch YouTube videos
@app.route('/youtube_videos')
def youtube_videos():
    if 'youtube_access_token' in session:
        videos = fetch_youtube_videos(session['youtube_access_token'])
        if videos:
            return render_template('youtube_videos.html', videos=videos)
        else:
            return 'Failed to fetch videos'
    else:
        return redirect(url_for('login_youtube'))

# Function to fetch YouTube videos
def fetch_youtube_videos(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    # Step 1: Retrieve the playlist ID for the channel's uploaded videos
    channel_params = {
        'part': 'contentDetails',
        'mine': 'true'
    }
    
    channel_response = requests.get(f"{YOUTUBE_API_BASE_URL}/channels", params=channel_params, headers=headers)
    if channel_response.status_code != 200:
        print(f"Failed to fetch channel details: {channel_response.json()}")
        return None
    
    channels_data = channel_response.json()
    if not channels_data.get('items'):
        print("No channels found for the authenticated user.")
        return None
    
    uploads_playlist_id = channels_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    # Step 2: Retrieve the list of uploaded videos using the playlist ID
    playlist_params = {
        'part': 'snippet,contentDetails,status',
        'playlistId': uploads_playlist_id,
        'maxResults': 10  # Adjust as needed
    }
    
    playlist_response = requests.get(f"{YOUTUBE_API_BASE_URL}/playlistItems", params=playlist_params, headers=headers)
    if playlist_response.status_code != 200:
        print(f"Failed to fetch playlist items: {playlist_response.json()}")
        return None
    
    videos = playlist_response.json().get('items', [])
    return videos

# Route to fetch Medium posts
@app.route('/medium_posts', methods=['GET', 'POST'])
def medium_posts():
    content = None
    if request.method == 'POST':
        username = request.form['username']
        try:
            post_url = get_latest_medium_post_url(username)
            if post_url:
                content = get_medium_post_content(post_url)
        except Exception as e:
            content = f"An error occurred: {e}"
    return render_template('medium_posts.html', content=content)

# Function to retrieve the URL of the latest Medium post
def get_latest_medium_post_url(username):
    url = f"https://medium.com/@{username}/latest"
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or provide the path to it
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Find the latest article link
    article_link = driver.find_element(By.XPATH, '//h2/ancestor::a')
    post_url = article_link.get_attribute('href')
    
    driver.quit()
    return post_url

# Function to retrieve the content of a Medium post
def get_medium_post_content(post_url):
    response = requests.get(post_url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve Medium post. Status code: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Medium article content is usually within <article> tags
    article_content = soup.find('article')
    if not article_content:
        return "No content found."

    paragraphs = article_content.find_all('p')
    content = "\n\n".join(paragraph.get_text() for paragraph in paragraphs)

    return content

# Route to fetch Quora posts
@app.route('/quora_posts', methods=['GET', 'POST'])
def quora_posts():
    content = None
    if request.method == 'POST':
        username = request.form['username']
        try:
            post_url = get_latest_quora_post_url(username)
            if post_url:
                content = extract_content_from_url(post_url)
        except Exception as e:
            content = f"An error occurred: {e}"
    return render_template('quora_posts.html', content=content)

# Function to retrieve the URL of the latest Quora post
def get_latest_quora_post_url(username):
    url = f"https://www.quora.com/profile/{username}/posts"
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or provide the path to it
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Find the latest post link
    post_link = driver.find_element(By.XPATH, '//div[@class="q-box qu-mb--tiny"]//a')
    post_url = post_link.get_attribute('href')
    
    driver.quit()
    return post_url

# Function to extract content from a Quora post URL
def extract_content_from_url(post_url):
    # Extract the content from the URL assuming it's part of the URL path
    content_start = post_url.find("profile/") + len("profile/") + post_url[post_url.find("profile/"):].find("/")
    content = post_url[content_start:].replace("-", " ")
    return content

# Run the Flask application in debug mode
if __name__ == "__main__":
    app.run(debug=True)



#Flask (import Flask):
# Flask is a lightweight web framework for Python that allows you to build web applications quickly and with minimal boilerplate code.
# Usage: Flask is used to create instances of the Flask application (app) and define routes for handling different URLs.
# requests (import requests):

# Requests is a simple HTTP library for Python that allows you to send HTTP requests easily.
# Usage: Used extensively for making OAuth requests to authorization and token endpoints of LinkedIn, Reddit, and YouTube. Also used to make API requests to fetch profile data and posts from these platforms.
# os (import os):

# The os module provides functions for interacting with the operating system, such as handling environment variables.
# Usage: Used to generate a secret key (os.urandom(24)) for Flask session management (app.secret_key) and for accessing environment variables like client IDs and secrets securely.
# urlencode (from urllib.parse import urlencode):

# urlencode is a function from Python's urllib.parse module that converts a dictionary or sequence of two-element tuples into a URL-encoded query string.
# Usage: Used to construct OAuth authorization URLs with query parameters (params) for LinkedIn, Reddit, and YouTube.
# selenium (from selenium import webdriver):

# Selenium is a web automation tool that provides APIs for browser automation.
# Usage: Used specifically in functions (get_latest_medium_post_url and get_latest_quora_post_url) to scrape and retrieve URLs of the latest posts from Medium and Quora, respectively. It interacts with web elements on these sites to extract data.
# BeautifulSoup (from bs4 import BeautifulSoup):

# BeautifulSoup is a library for parsing HTML and XML documents, providing easy ways to navigate, search, and modify the parse tree.
# Usage: Used in conjunction with Selenium to parse HTML content fetched from Medium (get_medium_post_content) and Quora (extract_content_from_url) to extract specific post content after retrieving the URLs.
# time (import time):

# The time module provides various time-related functions, including sleep(), which pauses the execution for a specified number of seconds.
# Usage: Used in conjunction with Selenium to pause execution (time.sleep(5)) to allow web pages to load fully before scraping content, ensuring reliability in web scraping operations.
# These libraries collectively enable the Flask application to handle OAuth authentication flows for LinkedIn, Reddit, and YouTube, fetch user profile data and posts from these platforms, and also scrape and extract content from Medium and Quora posts. Each library plays a crucial role in different aspects of the application, from web scraping and HTTP request handling to session management and environment variable access.