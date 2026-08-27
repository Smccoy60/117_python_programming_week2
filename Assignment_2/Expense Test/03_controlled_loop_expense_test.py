total = 0

expense = float(input("Enter an expense amount: (0 to end): "))

while expense != 0:
    print(f"Beginning total: ${total:.2f} + Added: ${expense:.2f} = ${total + expense:.2f}")
    total = total + expense
    print(f"New Total: ${total:.2f}")
    print()
    expense = float(input("Enter another expense amount (0 to end): "))
print()
print(f"Final Total Expense: ${total:.2f}")
