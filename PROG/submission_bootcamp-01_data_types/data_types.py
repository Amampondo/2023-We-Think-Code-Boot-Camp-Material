def boolean():
    """
    Question 1 - Boolean

    Using the variable below, give it the value 'True', then print it.
    """
    # enter your code here
    staying_alive = None

    staying_alive = True

    print(staying_alive)


def integer():
    """
    Question 2 - Integer

    Create a program to accept two numbers from a user and multiply them, then print the product.
    """

    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))

    # enter your code here
    mult = num1*num2
    print("The product is",mult)

def string():
    """
    Question 3 - String

    Assign a name to the variable below and print it.
    """

    # enter your code here

    your_name = None

    your_name="Mluleki"
    
    print(your_name)


def convert_to_float():
    """
    Question 4 - Float

    Convert the following integer to a float then print it.
    """

    int_num = 60
    
    #enter your code here
    int_num=float(int_num)

    print(int_num)

def all_data_types():
    """
    Question 5 - All Data Types

    Output the following sentence using the given variables.

    Welcome to the 2023 WeThinkCode_ bootcamp where True learning costs R0.00
    """

    string_one = "Welcome to the "
    string_two = " WeThinkCode_ bootcamp where "
    string_3 = " learning costs R"
    bool_condition = True
    int_year = 2023
    float_cost = 0.00

    #enter your code here

    print(string_one + str(int_year)+ string_two+ str(bool_condition)+ string_3 + str(format(float_cost,'.2f')))

