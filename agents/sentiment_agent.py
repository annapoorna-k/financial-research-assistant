from config import llm

def sentiment_agent(state):

    prompt = f"""
Analyze investor sentiment.

Financial Data:
{state['financial_data']}

News:
{state['news_data']}

Market:
{state['market_data']}
"""

    response = llm.invoke(prompt)

    return {
        "sentiment_analysis": response.content
    }