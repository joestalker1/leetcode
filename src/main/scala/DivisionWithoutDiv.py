def divide(product, divisor):
    if product < divisor:
        return (0, product)
    if divisor == 1:
        return product

    current_product = divisor
    times = 1

    while current_product * current_product <= product:
        times *= current_product
        current_product *= current_product

    while current_product + divisor <= product:
        current_product += divisor
        times += 1

    return (times, product - current_product)



print(divide(1000, 3))