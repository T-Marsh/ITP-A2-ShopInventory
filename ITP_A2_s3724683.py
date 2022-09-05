#!/usr/bin/python3

# COSC1519 Introduction to Programming
# A2 Programming Project 
# Student name: Thomas Marsh
# Student number: s3724683

from operator import index


customer_names = ["Linda", "Jack", "Zoran"]
product_names = ["apple", "banana", "cake"]
product_prices = [134, 52, 5] # in whole number dollars ($)
product_stock_amounts = [9, 25, 2]

# Products their price and available stock are stored in lists (product_names, product_prices, product_stock_amounts).
# Each product_name has a corresponding product_price and product_stock_amount in the same position in those lists.
# For example, if the product 'apple' had a position of [0] in the list of product_names. Then to find the price
# and the number of stock available we need only check position [0] in the producet_prices and product_stock_amounts lists.
# we would see that an apple costs $134 and there are currently 9 available.

discount = 10 # in percentage (%)

repeat_customer = False

def customer_name():
    input_name = input("Please enter the name of the customer: ")
    return input_name

def is_repeat_customer(customer):
    if customer in customer_names:
        print("Repeat customer!")
        repeat_customer = True
    else:
        print("New customer!")
        repeat_customer = False
    return repeat_customer

def product_name():
    input_product = input("Please enter the name of the product: ")
    if input_product not in product_names:
        print("The product you have entered is not valid.")
        exit()
    else:
        return input_product

def get_product_index(product):
    product_index = int(product_names.index(product))
    return product_index

def product_quantity(customer, product, product_index):
    input_quantity = int(input("Please enter the product quantity: "))

    if input_quantity < product_stock_amounts[product_index]:
        print(customer)
        print(f"{customer} purchased {input_quantity} x {product}.")
    else:
        print("There aren't enough of that product to purchase.")
        exit()

# input_product = input("Please enter the name of the product: ")
# if input_product not in product_names:
#     print("The product you have entered is not valid.")
# else:
#     input_quantity = int(input("Please enter the product quantity: "))
#     if input_quantity < 10:
#         print(f"{input_name} purchased {input_quantity} x {input_product}.")
#     else:
#         print("There aren't enough of that product to purchase.")

def main():
    customer = customer_name()
    repeat_customer = is_repeat_customer(customer)
    product = product_name()
    product_index = get_product_index(product)
    product_quantity(customer, product, product_index)

if __name__ == "__main__":
    main()
