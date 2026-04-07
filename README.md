**📌 Project Description**


_**🔹 Overview**_

This project implements a tool-based AI agent in Python that processes user queries and routes them to appropriate services such as a calculator, Wikipedia, web search, or decision support.
Instead of relying on unstable model-driven tool calling, the system uses a deterministic routing mechanism to ensure consistent and reliable execution.

_**🎯 Objectives**___
Build a stable AI agent that avoids unreliable function-calling behavior
Enable multi-functional query handling (math, knowledge, search, decisions)
Design a modular architecture for easy extension of tools
Ensure predictable and fast execution using rule-based routing
Provide a practical understanding of agent systems without over-dependence on LLMs

_**⚙️ Execution Flow**__
User enters a query via command-line interface
The system preprocesses and normalizes the input
A router module analyzes keywords and intent
Based on classification, the query is forwarded to the appropriate tool:
Calculator → evaluates mathematical expressions
Wikipedia → fetches summarized knowledge
Web Search → retrieves recent information
Decision Helper → provides structured recommendations
The selected tool executes and returns the result
The agent displays the final output to the user

**_🧠 Algorithm (High-Level)_**
Start
│
├── Accept user input
│
├── Convert input to lowercase
│
├── IF input contains math operators
│       → call calculator
│
├── ELSE IF input contains knowledge-based keywords
│       → call Wikipedia API
│
├── ELSE IF input contains recent/trending keywords
│       → call web search
│
├── ELSE IF input relates to decision-making
│       → call decision helper
│
├── ELSE
│       → fallback to LLM response
│
└── Display result
End


_**🧩 System Architecture**_
Agent (Controller): Manages query processing and execution flow
Router: Determines which tool to invoke based on input
Tools: Independent modules performing specific tasks
Fallback LLM: Handles general queries outside predefined rules

_**✨ Key Features**_
Deterministic routing (no unreliable AI tool calls)
Modular and extensible design
Handles multiple query types in a single system
Improved stability compared to model-driven agents
Lightweight and easy to run locally

_**🚀 Conclusion**_

This project demonstrates how a rule-based agent system can outperform unstable AI-driven tool calling in terms of reliability and control. It serves as a strong foundation for building more advanced systems such as hybrid agents, multi-agent architectures, or intelligent assistants.
