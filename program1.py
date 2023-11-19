def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2
result = multiplication_or_sum(20, 30)
print("The result is", result)
result = multiplication_or_sum(40, 30)
print("The result is", result)
