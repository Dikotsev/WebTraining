def price_validator(price):
    if price <= 0:
        raise ValueError('Price can not be negative')
    return price_validator()