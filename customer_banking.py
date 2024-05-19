# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Enter your savings account balance: "))
    savings_interest = float(input("Enter your savings account interest rate: "))
    savings_maturity = int(input("Enter your savings account maturity: "))  # wrong by is using float 
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("interest earned:", interest_earned)
    print("updated balance:", updated_savings_balance)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Enter your CD account balance: "))
    cd_interest = float(input("Enter your CD account interest rate: "))
    cd_maturity = int(input("Enter your CD account maturity: "))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("interest earned:", interest_earned)
    print("updated balance:", updated_cd_balance)
    
if __name__ == "__main__":
    main()
    # Call the main function.