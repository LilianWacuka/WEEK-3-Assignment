def calculate_discount(price, discount_percent):
    # calculate the final price after applying the discount
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price
    
 # Define price and discount outside the function
price = 100
discount = 25
# Call the function
print(calculate_discount(price, discount)) 
# Output: 75.0
# The function calculates the final price after applying a discount if the discount is 20% or more.

# If the discount is less than 20%, it returns the original price.
price = 100
discount = 15
# Call the function
print(calculate_discount(price, discount))
# Output: 100

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price == price:
    print(f"No discount applied. The original price is: ${price:.2f}")
else:
    print(f"Discount applied! The final price after {discount_percent}% discount is: ${final_price:.2f}")
