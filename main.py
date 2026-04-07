from groq import Groq
import wikipedia
from ddgs import DDGS
import math

client = Groq(api_key="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")

# ------------------ TOOLS ------------------ #

def calculator(input: str) -> str:
    try:
        return str(eval(input, {"__builtins__": {}}, {"math": math}))
    except:
        return "Error in calculation"

def search_wikipedia(query: str) -> str:
    print("[TOOL] Wikipedia:", query)
    try:
        return wikipedia.summary(query, sentences=3)
    except Exception as e:
        return f"Wikipedia error: {str(e)}"

def web_search(query: str) -> str:
    print("[TOOL] Web:", query)
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        if not results:
            return "No results found."
        return "\n".join([r.get('body', '') for r in results])
    except Exception as e:
        return f"Web search error: {str(e)}"

def decision_helper(situation: str) -> str:
    return "Use internship if you lack exposure, else build projects."

# ------------------ ROUTER ------------------ #

def router(query: str):
    q = query.lower()

    if any(op in q for op in ["+", "-", "*", "/", "%"]):
        return "math"
    elif any(word in q for word in ["who", "history", "tell me"]):
        return "wiki"
    elif any(word in q for word in ["news", "latest"]):
        return "web"
    elif any(word in q for word in ["career", "internship"]):
        return "decision"
    else:
        return "llm"

# ------------------ AGENT ------------------ #

def run_agent(user_input):
    route = router(user_input)
    print(f"[Route → {route}]")

    if route == "math":
        print("Agent:", calculator(user_input))

    elif route == "wiki":
        print("Agent:", search_wikipedia(user_input))

    elif route == "web":
        print("Agent:", web_search(user_input))

    elif route == "decision":
        print("Agent:", decision_helper(user_input))

    else:
        # fallback to LLM (no tools)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        print("Agent:", response.choices[0].message.content)

# ------------------ LOOP ------------------ #

print("Stable AI Agent Ready\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    run_agent(user_input)