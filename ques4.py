def print_rangoli(size):
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        
        left = alpha[size-1:i:-1]
        right = alpha[i:size]
        row = '-'.join(left + right)
        lines.append(row.center(4*size - 3, '-'))

    full_rangoli = lines[::-1] + lines[1:]

    print('\n'.join(full_rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)