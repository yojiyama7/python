n = int(input())

def digit_sum_simple(n):
    
    max_sum = -1

    for i in range(10**(len(str(n))-1)-1, n+1):
        
        i_parts = []
        for i_part in str(i):
            i_parts.append(int(i_part))

        this_sum = sum(i_parts)
        
        if max_sum < this_sum:
            max_sum = this_sum
            max_sum_i = i

    return max_sum, max_sum_i

def digit_sum_temp(n):
    max_sum_i = int(str(int(str(n+1)[0])-1) + "9"*(len(str(n+1))-1))
    max_sum = sum([int(j) for j in str(max_sum_i)])
    return max_sum

print(digit_sum_temp(n))

print(sum([int(j) for j in str(int(str(n+1)[0])-1) + "9"*(len(str(n+1))-1)]))