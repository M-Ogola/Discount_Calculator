# Discount_Calculator
Control Flows
This Python script is designed to handle a simple task: calculating a discounted price, but with a specific condition. It's a great example of using a function to modularize your code and conditional logic to control program flow.

The calculate_discount Function

The function calculate_discount(price, discount_percent) is the heart of this program. It's a reusable block of code that takes two arguments:

price: A number representing the original cost of an item.

discount_percent: A number representing the discount to be applied.

Inside the function, an if statement checks if the discount_percent is greater than or equal to 20.

If the condition is true (the discount is 20% or more), the function calculates the final price. It first determines the discount_amount by multiplying the price by the discount_percent converted to a decimal (e.g., 25% becomes 0.25). Then, it subtracts this amount from the original price and returns the final value.

If the condition is false (the discount is less than 20%), the code inside the if block is skipped. The else statement is executed, and the function simply returns the original price without any changes.

The Main Program Logic

The code outside the function is responsible for getting input from the user and running the calculation.

User Input: The input() function is used to prompt the user to enter the original price and the discount percentage. Since input() returns a string, the float() function is used to convert the user's input into a floating-point number (a number with a decimal). This is crucial for performing mathematical operations.

Function Call: The program then calls the calculate_discount function, passing the two values provided by the user. The value returned by the function is stored in the final_price variable.

Output: Finally, an if statement checks the discount_percentage again (the same one the user entered) to determine which message to print. It either prints the new, discounted price or a message stating that no discount was applied. The f-string formatting (:.2f) ensures the prices are displayed with two decimal places, which is standard for currency.
