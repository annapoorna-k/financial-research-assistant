from tools.yahoo_finance_tool import get_financial_data

def financial_agent(state):

    result = get_financial_data(
        state["company"]
    )

    return {
        "financial_data": str(result)
    }