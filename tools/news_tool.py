# tools/news_tool.py

import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()

from newsapi import NewsApiClient

newsapi = NewsApiClient(
    api_key=os.getenv("NEWS_API_KEY")
)

def get_company_news(company):

    articles = newsapi.get_everything(
        q=company,
        language="en",
        page_size=5
    )

    news = []

    for article in articles["articles"]:

        news.append(
            {
                "title": article["title"],
                "description": article["description"]
            }
        )

    return news