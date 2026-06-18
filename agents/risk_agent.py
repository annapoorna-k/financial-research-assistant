from config import llm

def risk_agent(state):

    prompt = f"""
Analyze investment risks.

Financial:
{state['financial_data']}

News:
{state['news_data']}

Sentiment:
{state['sentiment_analysis']}
"""

    response = llm.invoke(prompt)

    return {
        "risk_analysis": response.content
    }