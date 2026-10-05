import requests


def get_ai_guidance(income, expenses, savings, budget):
    """
    Get general financial guidance from the local Ollama AI model.
    """

    prompt = f"""
You are FinSight AI, a financial education assistant.

Analyze this monthly financial information:

Monthly Income: ₹{income:,.0f}
Monthly Expenses: ₹{expenses:,.0f}
Monthly Savings: ₹{savings:,.0f}
Monthly Budget: ₹{budget:,.0f}

Give simple and practical financial guidance.

Include:
1. A short analysis of the financial situation.
2. Two or three suggestions for improving savings.
3. One suggestion for controlling expenses.
4. A simple budgeting suggestion.

Keep the answer beginner-friendly and concise.

Do not provide investment recommendations or professional financial advice.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:latest",
                "prompt": prompt,
                "stream": False
            }
        )

        if response.status_code == 200:
            result = response.json()
            return result["response"]

        return "Unable to connect to the AI model."

    except Exception as e:
        return f"AI connection error: {e}"