# Day 3
# Part One
gamma_str = ''
epsilon_str = ''

read_file = open('input.txt', 'r', encoding='utf-8')
diagnostics = list(map(str,read_file.read().split('\n')))
diag_len = len(diagnostics[0])
for i in range(0, diag_len):
    count_one, count_zero = 0, 0
    for diag in diagnostics:
        if '1' in diag[i]: count_one += 1
        else: count_zero += 1
    if count_one > count_zero:
        gamma_str += '1'
        epsilon_str += '0'
    else:
        gamma_str += '0'
        epsilon_str += '1'
print(int(gamma_str, 2) * int(epsilon_str, 2))

# Part Two
def count_bits(a_list, idx, ch):
    return [char for char in a_list if char[idx] == ch]

def count_ones(a_list, idx, ch):
    count = 0
    for x in a_list:
        if x[idx] == ch:
            count += 1
    return count

read_file = open('input.txt', 'r', encoding='utf-8')
diagnostics = list(map(str,read_file.read().split('\n')))
indexes = len(diagnostics[0])

# oxygen generator rating:
oxy = diagnostics.copy()
for i in range(indexes):
    list_length = len(oxy)
    if list_length == 1: break
    ones = count_ones(oxy, i, '1')
    most_ones = (ones > (list_length - ones)) or (ones == (list_length - ones))
    match most_ones:
        case True: oxy = count_bits(oxy, i, '1')
        case False: oxy = count_bits(oxy, i, '0')

# CO2 scrubber rating
co2 = diagnostics.copy()
for i in range(indexes):
    list_length = len(co2)
    if list_length == 1: break
    zeros = count_ones(co2, i, '0')
    least_ones = (zeros < (list_length - zeros)) or (zeros == (list_length - zeros))
    match least_ones:
        case True: co2 = count_bits(co2, i, '0')
        case False: co2 = count_bits(co2, i, '1')

print(int(oxy[0], 2) * int(co2[0], 2))

