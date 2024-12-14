# PollPulse 
## WebApp for 2020 Federal Election Tweet Insights and Analysis

PollPulse is a social media analysis platform for tracking and visualizing engagement trends, candidate comparisons, and social media influence during elections. It leverages Python (Flask), SQLAlchemy, and advanced SQL to provide meaningful metrics. On the Frontend, we have used React JS and Chart JS for interactive visualizations

#### Hosted Site: https://presidentialelection2020-tweet-analysis-goi9.onrender.com/

### How to Run the App Locally
Follow these steps to set up and run the application on your local machine: -
##### Prerequisites
* Python 3.8 or higher installed on your machine
* CLI
* reactjs (or Node.js required for frontend setup)

#### BACKEND Setup Steps
 1.  Clone the Repository:
 2.  Navigate to the Backend:
```
cd path_to_project/tweet-analysis-app/backend
```
 3.  Create a Virtual Environment:
```
python -m venv venv
```
 4.  Activate the Virtual Environment
```
source venv/bin/activate
```
 5.  Install Dependencies
```
pip install -r requirements.txt
```
6. Setup .env File in the backend folder
```
POSTGRES_DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>
```
7. Start the Backend Server
```
python -m flask run --debug
```
8. Check the API specification for testing using Swagger - default on http://127.0.0.1:5000/docs


#### FRONTEND Setup Steps
1. Navigate to the Frontend folder:
```
cd path_to_project/tweet-analysis-app/frontend/election_tweet_analysis_app
```
2. Install dependencies
```
npm install
```
3. Add the API URL in the config.json file
```
e.g. "api_url": "http://127.0.0.1:5000/api"
```
4. Start the Frontend Server
```
npm start
```
