def is_valid_amount(amount):
    try:
        float(amount)
        return True
    except:
        return False
