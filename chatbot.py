import cohere
import streamlit as st

def get_budget_insights(user_query, transaction_text):
    api_key = st.secrets["COHERE_API_KEY"]
    co = cohere.ClientV2(api_key)

    prompt = f"""You are SpendWise AI, a smart and friendly personal finance assistant.
You help users understand their spending habits, save money, and make better financial decisions.

Here are the user's current transactions:
{transaction_text}

User's question: {user_query}

Important rules:
- Only answer finance related questions
- If asked non-finance questions, politely say you only handle financial advice
- Keep answers short, clear and practical
- Give advice relevant to Indian context (INR, Indian expenses)
- Be friendly and encouraging"""

    response = co.chat(
        model="command-a-03-2025",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.message.content[0].text.strip()
