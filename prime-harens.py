def is_prime(num):
    if num > 1:
        for prime_counter in range(2, (num // 2) + 1):
            if num / prime_counter == num // prime_counter:
                return False
        return True
    return False

def factors(num):
    factor_list = []
    if is_prime(num):
        if num < 2:
            factor_list.append(num)
            return factor_list
        # TODO: Append Multiple Values
        factor_list.append(1)
        factor_list.append(num)
        return factor_list
    list_position = 0
    for list_counter in range(1, num // 2):
        if num / list_counter == num // list_counter and factor_list.count(list_counter) == 0:
            factor_list.insert(list_position, list_counter)
            factor_list.insert(list_position + 1, int(num / list_counter))
            list_position += 1
    return factor_list

print(factors(12))
