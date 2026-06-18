#Financial Research Assistant using Multi-Agent Architecture
#Overview
The Financial Research Assistant is a Multi-Agent AI system built using LangGraph, LangChain, FastAPI, OpenRouter, Yahoo Finance, newsapi.org, and LangFuse.
The system performs end-to-end financial research on a company or stock by orchestrating multiple specialized AI agents. Each agent is responsible for a specific task such as collecting financial data, gathering news, analyzing sentiment, assessing risks, and generating investment recommendations.
This project demonstrates how Enterprise AI Agent Systems can be designed using specialized agents instead of a single monolithic AI agent.

#Business Problem
Financial analysts spend significant time gathering information from multiple sources before making investment recommendations.
Typical activities include:
Collecting financial statements
Reviewing market performance
Reading recent news
Assessing risks
Analyzing sentiment
Preparing investment reports
This process is repetitive, time-consuming, and difficult to scale.
The Financial Research Assistant automates this workflow using AI Agents.

#Objectives
The system should:
Collect company financial information
Collect latest company news
Analyze market information
Evaluate sentiment
Assess investment risks
Generate investment recommendations
Produce executive reports

#Technology Stack
Component -> Technology
Programming Language  ->  Python
API Framework  ->  FastAPI
Agent Framework  ->  LangGraph
LLM Framework  ->  LangChain
LLM Provider ->  OpenRouter
Financial Data -> Yahoo Finance
News Data -> newsapi.org
Observability -> LangFuse
Deployment -> Docker

