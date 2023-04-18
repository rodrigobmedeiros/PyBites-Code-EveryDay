def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """

    positive_factor_to_add = 1 if up else 0

    return [
        int(number) + positive_factor_to_add
        if int(number) >= 0
        else int(number) + positive_factor_to_add - 1
        for number in transactions
    ]
