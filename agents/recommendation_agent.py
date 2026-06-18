from config import llm

def recommendation_agent(state):

    prompt = f"""
Provide recommendation.

Financial:
{state['financial_data']}

Sentiment:
{state['sentiment_analysis']}

Risk:
{state['risk_analysis']}

Return:

BUY
HOLD
SELL

with justification.
"""

    response = llm.invoke(prompt)

    return {
        "recommendation": response.content
    }