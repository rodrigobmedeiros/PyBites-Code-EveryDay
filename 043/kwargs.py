def get_profile(*args, name: str='julian', profession: str='programmer'):
    
    if len(args) != 0:
        raise TypeError

    return f'{name} is a {profession}'