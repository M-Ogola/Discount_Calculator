def calculate_discount(price, discount_percent): 
    """
    Calculates the final price after a discount, but only if the
    discount percentage is 20% or higher.

    Args: 
        price (float): The original price of the item. 
        discount_percent (float): The discount percentage.

    Returns: 
        float: The final price after the discount, or the original
               price if the discount is less than 20%.
    """
    if discount_percent >= 20: 
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price
        final_price = price - discount_amount 
        return final_price
    else:
        # If the discount is too low, return the original price
        return price 

# --- Main part of the script ---
if __name__ == "__main__": 
    try:
        # Prompt the user for the original price and discount percentage
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        # Call the function to calculate the final price
        final_price = calculate_discount(original_price, discount_percentage)

        # Print the result
        if discount_percentage >= 20:
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. Original price: ${final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers for the price and discount.")