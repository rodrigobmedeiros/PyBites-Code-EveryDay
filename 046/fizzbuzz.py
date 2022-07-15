from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    
    is_div_by_3 = not (num % 3)
    is_div_by_5 = not (num % 5)

    code = list()

    if is_div_by_3:
        code.append('Fizz')
    if is_div_by_5:
        code.append('Buzz')
    
    return ' '.join(code) if code else num
