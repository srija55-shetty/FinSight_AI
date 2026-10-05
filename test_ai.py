from utils.ai_helper import get_ai_guidance


income = 30000
expenses = 21000
savings = 9000
budget = 30000

result = get_ai_guidance(
    income,
    expenses,
    savings,
    budget
)

print("\n===== FinSight AI Guidance =====\n")
print(result)