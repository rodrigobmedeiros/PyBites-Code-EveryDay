WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
    Don't return anything, print the output to stdout"""
    
    factor = size / 2
    line = ''.join(int(factor) * [f'{WHITE}{BLACK}'])
    is_reverse = False
    
    for _ in range(size):
        
        if not is_reverse:
            print(line)
            is_reverse = True
        else:
            print(line[::-1])
            is_reverse = False
    
create_chessboard(size=8)