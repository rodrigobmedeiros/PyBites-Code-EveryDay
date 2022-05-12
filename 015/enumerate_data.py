from typing import List

names: List[str] = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries: List[str] = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    
    for idx in range(len(names)):
       print(f'{idx + 1}. {names[idx].ljust(11)}{countries[idx]}')


enumerate_names_countries()