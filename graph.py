from langgraph.graph import StateGraph, END

from state import FinancialState

from agents.supervisor import supervisor
from agents.financial_agent import financial_agent
from agents.news_agent import news_agent
from agents.market_agent import market_agent
from agents.sentiment_agent import sentiment_agent
from agents.risk_agent import risk_agent
from agents.recommendation_agent import recommendation_agent
from agents.report_agent import report_agent

workflow = StateGraph(FinancialState)

# Nodes

workflow.add_node(
    "supervisor",
    supervisor
)

workflow.add_node(
    "financial",
    financial_agent
)

workflow.add_node(
    "news",
    news_agent
)

workflow.add_node(
    "market",
    market_agent
)

workflow.add_node(
    "sentiment",
    sentiment_agent
)

workflow.add_node(
    "risk",
    risk_agent
)

workflow.add_node(
    "recommendation",
    recommendation_agent
)

workflow.add_node(
    "report",
    report_agent
)

# Entry

workflow.set_entry_point("supervisor")

# --------------------------------------------------
# Parallel Execution
# --------------------------------------------------

workflow.add_edge(
    "supervisor",
    "financial"
)

workflow.add_edge(
    "supervisor",
    "news"
)

workflow.add_edge(
    "supervisor",
    "market"
)

# --------------------------------------------------
# Fan-In
# Sentiment waits for ALL parallel branches
# --------------------------------------------------

workflow.add_edge(
    "financial",
    "sentiment"
)

workflow.add_edge(
    "news",
    "sentiment"
)

workflow.add_edge(
    "market",
    "sentiment"
)

# --------------------------------------------------

workflow.add_edge(
    "sentiment",
    "risk"
)

workflow.add_edge(
    "risk",
    "recommendation"
)

workflow.add_edge(
    "recommendation",
    "report"
)

workflow.add_edge(
    "report",
    END
)

graph = workflow.compile()