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
![image](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/cf8b448e-45ec-4523-b850-c0beea6b6da1)
![image](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/54332059-cc30-47f0-bd18-686910a4224b)

-Authorize Linkedin to fetch user profile
![image](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/243885df-6c18-40f1-aac8-a68578781671)

-Allow user to post to Linkedin
![image](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/28457fc9-b0da-4efc-a942-76e913bfdc33)

![image](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/0206eb8d-f3eb-4bd1-816c-5b3f870ed656)

![image](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/8b9be743-7198-473b-834e-e43a0ac78e96)



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

/login/reddit: Initiates the Reddit OAuth 2.0 flow.
/auth/reddit/callback: Handles the Reddit OAuth 2.0 callback and retrieves access tokens.
/reddit_profile: Displays the user's Reddit profile information.
/reddit_posts: Fetches the user's recent posts from Reddit.


### Output: 
This is y profile: ![Screenshot 2024-06-10 174612](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/db876361-40c3-41e1-98e5-759a8d48eb0b)
And these are outputs after configuring :
![Screenshot 2024-06-10 164326](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/e41010ce-ab36-4162-89fb-f0466185d217)
![Screenshot 2024-06-10 164336](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/a02d1e60-fd38-4ebc-b6bc-36346130df91)
![image](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/87b1de16-ef47-4d72-b31c-9526d956ed9a)
![Screenshot 2024-06-10 174553](https://github.com/Wallet-Hunter/social-posting-tool/assets/132088009/1a98044b-cf03-4cd8-b2e3-90d9cc133972)

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

