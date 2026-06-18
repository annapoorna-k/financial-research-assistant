from tools.news_tool import get_company_news

def news_agent(state):

    result = get_company_news(
        state["company"]
    )

    return {
        "news_data": str(result)
    }