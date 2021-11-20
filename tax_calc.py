'''Tax Calculator - Asks the user to enter a cost and either a country or state tax.\
It then returns the tax plus the total cost with tax'''

def ask_amount():
    try:
        amount = int(input("Enter the amount: "))
    except:
        print("Inavlid Amount")
        ask_amount()
    return amount

amount = ask_amount()

while True:
    print("Do you want to calculate Country or state tax?")
    choice = input("Enter 'C' for country and 'S' for state: ").lower()

    if choice == 'c':
        tax_c = float(input("Enter the country tax rate(in %): "))
        tax_c_amount = ((tax_c)/100)*amount
        total_C = amount+tax_c_amount
        print(f"Your final amount after Central tax is: {total_C}")
        break

    elif choice == 's':
        tax_s = float(input("Enter the state tax rate(in %): "))
        tax_s_amount = ((tax_s)/100)*amount
        total_S = amount+tax_s_amount
        print(f"Your final amount after State tax is: {total_S}")
        break
    else:
        print("Invalid Choice!!")

