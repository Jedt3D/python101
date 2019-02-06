def inc_vat(price):
    return price + (price * 7 / 100)

def exc_vat(price):
    return price - (price * 7 / 100)


if __name__ == '__main__':
    my_product_price = 100
    print("Price with VAT will be " + str(inc_vat(my_product_price)))
    print("Price without VAT will be " + str(exc_vat(my_product_price)))
