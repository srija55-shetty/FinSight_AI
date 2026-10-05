import streamlit as st
import pandas as pd
from utils.ai_helper import get_ai_guidance

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="FinSight AI",
    page_icon="💰",
    layout="wide"
)

# ============================================================
# TITLE
# ============================================================

st.title("💰 FinSight AI")
st.subheader("AI-Powered Financial Guidance System")

st.write(
    "Track your income, expenses, savings, and budget "
    "to understand your financial situation."
)

st.divider()

# ============================================================
# MONTHLY FINANCIAL DETAILS
# ============================================================

st.header("💵 Enter Your Monthly Financial Details")

col1, col2 = st.columns(2)

with col1:
    income = st.number_input(
        "Monthly Income (₹)",
        min_value=0.0,
        value=30000.0,
        step=1000.0
    )

with col2:
    budget = st.number_input(
        "Monthly Budget (₹)",
        min_value=0.0,
        value=30000.0,
        step=1000.0
    )

# ============================================================
# EXPENSE CATEGORIES
# ============================================================

st.divider()

st.header("💸 Expense Categories")

st.write(
    "Enter how much you spend in each category every month."
)

col1, col2 = st.columns(2)

with col1:

    food = st.number_input(
        "🍔 Food",
        min_value=0.0,
        value=5000.0,
        step=500.0
    )

    rent = st.number_input(
        "🏠 Rent",
        min_value=0.0,
        value=7000.0,
        step=500.0
    )

    travel = st.number_input(
        "🚍 Travel",
        min_value=0.0,
        value=2000.0,
        step=500.0
    )

    education = st.number_input(
        "📚 Education",
        min_value=0.0,
        value=2000.0,
        step=500.0
    )

with col2:

    shopping = st.number_input(
        "🛍️ Shopping",
        min_value=0.0,
        value=1500.0,
        step=500.0
    )

    bills = st.number_input(
        "💡 Bills",
        min_value=0.0,
        value=1500.0,
        step=500.0
    )

    entertainment = st.number_input(
        "🎮 Entertainment",
        min_value=0.0,
        value=1000.0,
        step=500.0
    )

    other = st.number_input(
        "📦 Other",
        min_value=0.0,
        value=1000.0,
        step=500.0
    )

# ============================================================
# CREATE EXPENSE DATA
# ============================================================

expense_data = pd.DataFrame(
    {
        "Category": [
            "Food",
            "Rent",
            "Travel",
            "Education",
            "Shopping",
            "Bills",
            "Entertainment",
            "Other"
        ],
        "Amount": [
            food,
            rent,
            travel,
            education,
            shopping,
            bills,
            entertainment,
            other
        ]
    }
)

# Calculate total expenses

expenses = expense_data["Amount"].sum()

# ============================================================
# FINANCIAL CALCULATIONS
# ============================================================

savings = income - expenses

if income > 0:
    savings_percentage = (savings / income) * 100
else:
    savings_percentage = 0

# ============================================================
# FINANCIAL OVERVIEW
# ============================================================

st.divider()

st.header("📊 Financial Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Income",
        f"₹{income:,.0f}"
    )

with col2:
    st.metric(
        "💸 Expenses",
        f"₹{expenses:,.0f}"
    )

with col3:
    st.metric(
        "💵 Savings",
        f"₹{savings:,.0f}"
    )

with col4:
    st.metric(
        "📈 Savings Rate",
        f"{savings_percentage:.1f}%"
    )

# ============================================================
# INCOME VS EXPENSES CHART
# ============================================================

st.divider()

st.header("📈 Income vs Expenses")

chart_data = pd.DataFrame(
    {
        "Amount": [
            income,
            expenses,
            max(savings, 0)
        ]
    },
    index=[
        "Income",
        "Expenses",
        "Savings"
    ]
)

st.bar_chart(chart_data)

# ============================================================
# CATEGORY-WISE EXPENSES
# ============================================================

st.divider()

st.header("📊 Category-wise Expenses")

st.dataframe(
    expense_data,
    use_container_width=True,
    hide_index=True
)

st.write(
    f"### Total Expenses: ₹{expenses:,.0f}"
)

st.subheader("📈 Where Is Your Money Going?")

category_chart = expense_data.set_index("Category")

st.bar_chart(category_chart)

# ============================================================
# BUDGET PLANNER
# ============================================================

st.divider()

st.header("🎯 Monthly Budget Planner")

st.write(
    "Compare your monthly expenses with your planned budget."
)

if budget > 0:

    budget_used_percentage = (expenses / budget) * 100

else:

    budget_used_percentage = 0

remaining_budget = budget - expenses

# Budget metrics

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🎯 Monthly Budget",
        f"₹{budget:,.0f}"
    )

with col2:
    st.metric(
        "💸 Amount Spent",
        f"₹{expenses:,.0f}"
    )

with col3:
    st.metric(
        "💰 Remaining Budget",
        f"₹{remaining_budget:,.0f}"
    )

# ============================================================
# BUDGET PROGRESS
# ============================================================

st.subheader("📊 Budget Usage")

progress = min(budget_used_percentage / 100, 1.0)

st.progress(progress)

st.write(
    f"You have used **{budget_used_percentage:.1f}%** "
    "of your monthly budget."
)

# ============================================================
# BUDGET STATUS
# ============================================================

if expenses > budget:

    st.error(
        "🚨 You have exceeded your monthly budget. "
        "Consider reducing unnecessary expenses."
    )

elif budget_used_percentage >= 80:

    st.warning(
        "⚠️ You have used more than 80% of your budget. "
        "Try to control your remaining expenses."
    )

else:

    st.success(
        "✅ You are currently within your monthly budget."
    )

# ============================================================
# FINANCIAL STATUS
# ============================================================

st.divider()

st.header("🤖 Financial Status")

if savings < 0:

    st.error(
        "⚠️ Your expenses are higher than your income. "
        "Try reducing unnecessary expenses."
    )

elif savings_percentage < 10:

    st.warning(
        "⚠️ Your savings rate is currently low. "
        "Consider creating a simple monthly budget."
    )

elif savings_percentage < 30:

    st.info(
        "👍 Your finances look reasonable. "
        "You can try increasing your savings gradually."
    )

else:

    st.success(
        "🎉 Great! You are maintaining a healthy savings rate."
    )
# ============================================================
# AI FINANCIAL GUIDANCE
# ============================================================

st.divider()

st.header("🤖 AI Financial Guidance")

st.write(
    "Get simple financial guidance based on your monthly "
    "income, expenses, savings, and budget."
)

if st.button("🤖 Get AI Guidance"):

    with st.spinner("FinSight AI is analyzing your finances..."):

        guidance = get_ai_guidance(
            income,
            expenses,
            savings,
            budget
        )

    st.success("AI analysis completed!")

    st.write(guidance)

# ============================================================
# DISCLAIMER
# ============================================================

st.divider()

st.caption(
    "FinSight AI provides general financial education and "
    "guidance, not professional financial advice."
)