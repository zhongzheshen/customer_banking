# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import create_cd_account
import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    init_savings_balance = input("What is your initial savings balance? ")
    interest_rate = input("Please enter the interest rate. ")
    months = input("Please enter months. ")
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    savings_maturity = init_savings_balance * (1 + savings_interest) ** months
    interest_earned = savings_maturity - init_savings_balance
    updated_savings_balance = init_savings_balance + savings_maturity
    print(interest_earned, updated_savings_balance)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    init_cd_balance = input("What is your initial cd balance? ")
    interest_rate = input("Please enter the interest rate. ")
    months = input("Please enter months. ")
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    cd_maturity = init_savings_balance * (1 + cd_interest) ** months
    interest_earned = cd_maturity - init_cd_balance
    updated_cd_balance = init_cd_balance + cd_maturity    
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(interest_earned, updated_cd_balance)
    if __name__ == "__main__":
    # Call the main function.
    main()