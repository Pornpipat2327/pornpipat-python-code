"""Personal Finance Calculator
Student: Pornpipat
Date: 23 July 2025
Purpose: Calculate monthly budget and savings
"""

def calculate_monthly_budget():
    """
    ฟังก์ชันสำหรับคำนวณงบประมาณรายเดือนและเงินออม
    """
    print("=== Monthly expense calculator program ===")

    # 2. ขอข้อมูลจากผู้ใช้
    try:
        # รายได้ต่อเดือน
        monthly_income = float(input("Please enter your monthly income (THB): "))
        # ค่าเช่า
        rent_cost = float(input("Enter your monthly rent cost (THB): "))
        # ค่ากิน
        food_budget = int(input("Enter your monthly food budget (THB): "))
        # ค่าเดินทาง
        transportation_cost = float(input("Enter your monthly transportation cost (THB): "))
        # ค่าพักผ่อน
        entertainment_budget = int(input("Enter your monthly entertainment budget (THB): "))
        # เผื่อสำหรับฉุกเฉิน
        emergency_fund_percent = float(input("Enter percentage for emergency fund (such as 10.5): "))
        # เงินลงทุน
        investment_percent = float(input("Enter percentage for investment (such as 15.0): "))
    except ValueError:
        print("Error: Please enter a number")
        return

    # 3. คำนวณข้อมูล
    # ค่าใช้จ่ายคงที่
    total_fixed_expenses = rent_cost + transportation_cost
    # ค่าใช้จ่ายไม่คงที่
    total_variable_expenses = food_budget + entertainment_budget
    # ค่าใช้จ่ายทั้งหมด
    total_expenses = total_fixed_expenses + total_variable_expenses
    # รายได้คงเหลือ
    remaining_income = monthly_income - total_expenses

    # เงินฉุกเฉิน
    emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
    # เงินลงทุน
    investment_amount = monthly_income * (investment_percent / 100)
    # เงินเหลือสำหรับออม
    available_for_savings = remaining_income - emergency_fund_amount - investment_amount

    # สัดส่วนค่าใช้จ่ายต่อรายได้
    expense_ratio = (total_expenses / monthly_income) * 100 if monthly_income > 0 else 0

    # 4. แสดงข้อมูลออกทางหน้าจอ
    print("\n" + "="*29)
    print("=== MONTHLY BUDGET REPORT ===")
    print(f"Income: {monthly_income:.2f} THB")
    print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
    print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
    print(f"Total Expenses: {total_expenses:.2f} THB")
    print(f"Remaining: {remaining_income:.2f} THB")

    print("\n" + "="*29)
    print("=== SAVINGS BREAKDOWN ===")
    print(f"Emergency Fund ({emergency_fund_percent:.0f}%): {emergency_fund_amount:.2f} THB")
    print(f"Investment ({investment_percent:.0f}%): {investment_amount:.2f} THB")
    print(f"Available for Savings: {available_for_savings:.2f} THB")

    print("\n" + "="*29)
    print("=== ANALYSIS ===")
    print(f"Expense Ratio: {expense_ratio:.2f}%")
    print("="*29 + "\n")

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    calculate_monthly_budget()