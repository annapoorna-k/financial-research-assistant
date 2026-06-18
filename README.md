# Financial Research Assistant using Multi-Agent Architecture

## Overview
The **Financial Research Assistant** is an advanced Multi-Agent AI system built using LangGraph, LangChain, FastAPI, OpenRouter, Yahoo Finance, newsapi.org, and LangFuse.

The system performs end-to-end financial research on a company or stock by orchestrating multiple specialized AI agents. Each agent is responsible for a specific task such as collecting financial data, gathering news, analyzing sentiment, assessing risks, and generating investment recommendations.

This project demonstrates how **Enterprise AI Agent Systems** can be designed using specialized, modular agents instead of a single monolithic AI agent.

---

## Business Problem
Financial analysts spend a significant amount of time gathering and synthesizing information from multiple sources before making investment recommendations. 

Typical day-to-day activities include:
* Collecting financial statements
* Reviewing market performance
* Reading recent news and press releases
* Assessing corporate and market risks
* Analyzing overall market sentiment
* Preparing comprehensive investment reports

This manual workflow is highly repetitive, time-consuming, and difficult to scale. The Financial Research Assistant automates this entire pipeline using a collaborative network of AI Agents.

---

## Objectives
The system is engineered to automatically execute the following workflow:
* **Data Collection:** Retrieve comprehensive company financial information and the latest company news.
* **Market Analysis:** Analyze real-time market data and performance trends.
* **Sentiment Evaluation:** Gauge market and media sentiment surrounding the target asset.
* **Risk Assessment:** Identify and evaluate potential investment risks.
* **Insight Generation:** Formulate strategic investment recommendations and produce final executive reports.

---

## Technology Stack

| Component | Technology |
| :--- | :--- |
| **Programming Language** | Python |
| **API Framework** | FastAPI |
| **Agent Framework** | LangGraph |
| **LLM Framework** | LangChain |
| **LLM Provider** | OpenRouter |
| **Financial Data** | Yahoo Finance |
| **News Data** | newsapi.org |
| **Observability** | LangFuse |
| **Deployment** | Docker (Optional) |
