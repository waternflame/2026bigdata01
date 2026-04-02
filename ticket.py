def entrance_fee(ages: list) -> int:
    """
    Calculates the total admission fee for a group based on their ages.

    Args:
        ages (list): A list of ages for the visitors.

    Returns:
        int: The total calculated entry fee for the amusement park.
    """

    kid, adult, senior = 5000, 10000, 7000
    total_fee = 0
    for age in ages:
        if age >= 65:
            total_fee = total_fee + senior
        elif age >= 19:
            total_fee = total_fee + adult
        else:
            total_fee = total_fee + kid
    return total_fee