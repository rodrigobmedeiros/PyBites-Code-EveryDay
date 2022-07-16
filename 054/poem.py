INDENTS = 4

def print_hanging_indents(poem:str):
    
    is_first = False

    for line in poem.splitlines():
        
        line = line.strip()

        if line == '':
            is_first = True
        else:
            if is_first:
                print(line)
                is_first = False
            else:
                print(' ' * INDENTS, end='')
                print(line)