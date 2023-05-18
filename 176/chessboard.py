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


# Solution
# The solution creates two loops, mine creates only one
# I decided to create a line and reverse this line when needed.
# I really have to think better about O(n)
# But I think is a good solution.


# def create_chessboard(size=8):
#     """Create a chessboard with of the size passed in.
#     Don't return anything, print the output to stdout"""
#     board = ''

#     for i in range(size):
#         for j in range(size):
#             if (i + j) % 2 == 0:
#                 board += ' '
#             else:
#                 board += '#'
#         board += '\n'

#     print(board)