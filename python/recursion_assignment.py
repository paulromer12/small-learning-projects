# Create a program with a recursive function that accepts an integer argument, n, and prints the number of 1 up to and including n. Then, write a non-recursive method that takes an integer argument, n, and prints the number of 1 up to and including n.
# 1. In your code documentation include an explanation of each functions approach to solving the problem.
# 2. Include test code that will not allow a negative or 0 value.
# 3. In your display, include which function is being invoked at both the start and end of the output.
# Test your program until it works, and the output looks readable and understandable. Add the necessary documentation as described in Documentation Requirements, and then attach your .py file(s) to this assignment.

import sys

class NumberPrinter():
    def __init__(self):
        '''
        init function with recursion_limit variable
        '''
        self.recursion_limit = sys.getrecursionlimit()

    def print_numbers_recursive(self, n):
        """
        Prints numbers from 1 to n using recursion
        - Base case: If n is 1, print 1.
        - Recursive case: Call the function with n-1 and print n.
        """
        if n == 1:
            print(1)
        else:
            self.print_numbers_recursive(n-1)
            print(n)

    def print_numbers_iterative(self, n):
        """
        Prints numbers from 1 to n using iteration.
        """
        for i in range(1, n + 1):
            print(i)

    def get_positive_int_within_depth_limit(self):
        '''
        Function to prompt the user for a positive integer that is within the recursion depth limit and returns that integer
        '''
        while True:
            try:
                n = int(input("Enter a positive integer: "))
                if n > 0 and n < self.recursion_limit:
                    return n
                elif n >= self.recursion_limit:
                    print(f"The current recursion depth limit is: {self.recursion_limit}")
                else:
                    print(f"Please enter a positive integer greater than 0 and less than {self.recursion_limit}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    

def main():
    """
    Main function
    - Initializes the NumberPrinter class as variable number_printer.
    - Prompts the user to enter a valid positive integer as variable n by calling the get_positive_int_within_depth_limit method.
    - Calls both the recursive and non-recursive methods to print numbers 1 to n with print statements to lable output.
    """
    number_printer = NumberPrinter()
    n = number_printer.get_positive_int_within_depth_limit()
    
    print(f"\nPrinting 1 to {n} with a recursive function:")
    number_printer.print_numbers_recursive(n)
    print("End of the recursive function.\n")

    print(f"\nPrinting 1 to {n} with a iterative function:")
    number_printer.print_numbers_iterative(n)
    print("End of the iterative function.\n")


if __name__ == "__main__":
    main()