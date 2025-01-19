# Program to calculate customer's due amount

def calculate_due_amount(bill_amount, payment):
    """
    Calculates the due amount after a payment.

    Parameters:
        bill_amount (float): Total bill amount.
        payment (float): Payment made by the customer.

    Returns:
        float: The remaining due amount (if any) or 0 if payment is sufficient.
    """
    if payment >= bill_amount:
        return 0  # No due amount if payment covers the bill
    else:
        return bill_amount - payment  # Remaining due amount

# Input from the user
try:
    bill_amount = float(input("Enter the total bill amount: "))
    payment = float(input("Enter the payment made by the customer: "))

    if bill_amount < 0 or payment < 0:
        print("Amounts cannot be negative.")
    else:
        due_amount = calculate_due_amount(bill_amount, payment)

        if due_amount == 0:
            print("The bill is fully paid. No due amount.")
        else:
            print(f"The remaining due amount is: ${due_amount:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
