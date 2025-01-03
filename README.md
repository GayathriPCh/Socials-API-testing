## LinkedIn Integration with Flask Application

This project demonstrates how to integrate LinkedIn authentication and retrieve user profile information using a Flask application.

### Overview

This application allows users to authenticate via LinkedIn OAuth 2.0, retrieve their profile information, and perform actions such as posting on LinkedIn using their credentials.

### Prerequisites

Before getting started, ensure you have the following:

- LinkedIn Developer Account: Register your application on LinkedIn Developer Portal to obtain `CLIENT_ID` and `CLIENT_SECRET`.
- Python 3.x installed on your system.
- Basic knowledge of Flask and OAuth 2.0.

### Configuration

1. **LinkedIn App Credentials:**
   - Obtain `CLIENT_ID` and `CLIENT_SECRET` from LinkedIn Developer Portal.
   - Set `REDIRECT_URI` to match the callback URL configured in your LinkedIn app.

2. **Scopes:**
   - Defined the scopes required for the application. Example: `['openid', 'profile', 'w_member_social', 'email']`.

### Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```
### Usage
Run the Flask application:

```bash
python app.py
```
Open a web browser and navigate to http://127.0.0.1:5000.

Click on the "Login with LinkedIn" button.

### Endpoints
/login: Initiates the LinkedIn OAuth 2.0 flow.
/auth/linkedin/callback: Handles the LinkedIn OAuth 2.0 callback and retrieves access tokens.
/profile: Displays the user's LinkedIn profile information.
/post: Provides a form to create and post content to LinkedIn.

## Response Format
The profile endpoint (/profile) returns JSON data in the following format:

```json
{
    "sub": "782bbtaQ",
    "name": "John Doe",
    "given_name": "John",
    "family_name": "Doe",
    "picture": "https://media.licdn-ei.com/dms/image/C5F03AQHqK8v7tB1HCQ/profile-displayphoto-shrink_100_100/0/",
    "locale": "en-US",
    "email": "doe@email.com",
    "email_verified": true
}
```

### Conclusion

Configured Linkedin API to 
-Allow user to login with Linkedin
-Authorize Linkedin to fetch user profile
-Allow user to post to Linkedin

## Reddit Integration with Flask Application

This project demonstrates how to integrate Reddit authentication and retrieve user information using a Flask application.

### Overview

This application allows users to authenticate via Reddit OAuth 2.0, retrieve their profile information, and perform actions such as fetching their profile details and recent posts from Reddit.

### Prerequisites

Before getting started, ensure you have the following:

- Reddit Developer Account: Register your application on Reddit Developer Portal to obtain `CLIENT_ID` and `CLIENT_SECRET`.

### Configuration

1. **Reddit App Credentials:**
   - Obtain `CLIENT_ID` and `CLIENT_SECRET` from Reddit Developer Portal.
   - Set `REDDIT_REDIRECT_URI` to match the callback URL configured in your Reddit app.

2. **Scopes:**
   - Define the scopes required for the application. Example: `['identity', 'read', 'history']`.

Click on the "Login with Reddit" button.

## Endpoints

- /login/reddit: Initiates the Reddit OAuth 2.0 flow.
- /auth/reddit/callback: Handles the Reddit OAuth 2.0 callback and retrieves access tokens.
- /reddit_profile: Displays the user's Reddit profile information.
- /reddit_posts: Fetches the user's recent posts from Reddit.

## Youtube Integration with Flask Application

This project demonstrates how to integrate Youtube authentication and retrieve user information via Youtube Data API
### Overview

This application allows users to authenticate via Youtube Data API OAuth 2.0, retrieve their profile information, and perform actions such as fetching their profile details and videos from Youtube.

### Prerequisites

Before getting started, ensure you have the following:

- Enable Youtube Data API via the Google developer console: Register your application onthe console to obtain `CLIENT_ID` and `CLIENT_SECRET`.

### Configuration

1. **Youtube App Credentials:**
   - Obtain `CLIENT_ID` and `CLIENT_SECRET`.
   - Set `YOUTUBE_REDIRECT_URI` to match the callback URL configured in your Youtube app.

2. **Scopes:**
   - Define all the scopes available in the app  , and define the scopes you want in the code: YOUTUBE_SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube'
]

Click on the "Login with Youtube" button.


### Output: 
This is youtube channel profile: ![Screenshot 2024-06-13 163717](https://github.com/GayathriPCh/GayathriPCh/assets/132088009/be93a764-4fa1-40c1-8217-e642a4543a11)

And these are outputs after configuring :

![Screenshot 2024-06-13 162834](https://github.com/GayathriPCh/GayathriPCh/assets/132088009/4d03288e-8402-481f-b694-87cc281ed6b8)

![Screenshot 2024-06-13 162806](https://github.com/GayathriPCh/GayathriPCh/assets/132088009/0fb5f65c-6ada-4ee3-a1fb-7db2b498ac64)

![Screenshot 2024-06-13 162711](https://github.com/GayathriPCh/GayathriPCh/assets/132088009/a833185d-8543-4110-b45d-2f575f03d3d4)

![Screenshot 2024-06-13 162727](https://github.com/GayathriPCh/GayathriPCh/assets/132088009/860e875b-64d1-4222-9877-d0763e05af9f)

