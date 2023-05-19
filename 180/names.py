from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    
    # The pyBites solution uses data.splitlies()[1:]
    # splitline()
    # Return a list of the lines in the string, breaking at line boundaries.
    # Line breaks are not included in the resulting list unless keepends is given and true.


    for idx, line in enumerate(data.split('\n')):
        
        if idx != 0:
            surname, first_name, country_code = line.split(',')
            countries[country_code].append(f'{first_name} {surname}')

    return countries

data.splitlines()