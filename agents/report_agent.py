from config import llm

def report_agent(state):

    prompt = f"""
Generate executive report.

Financial:
{state['financial_data']}

News:
{state['news_data']}

Sentiment:
{state['sentiment_analysis']}

Risk:
{state['risk_analysis']}

Recommendation:
{state['recommendation']}
"""

    response = llm.invoke(prompt)

    return {
        "report": response.content
    }