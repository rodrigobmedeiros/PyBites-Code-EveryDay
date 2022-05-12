from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    
    factor = 1
    
    while True:
        
        yield PYBITES_BORN + timedelta(days=factor * 100)
        
        factor += 1