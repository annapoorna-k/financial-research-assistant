from tools.market_tool import get_market_data


def market_agent(state):

    data = get_market_data(
        state["company"]
    )

    return {
        "market_data": str(data)
    }