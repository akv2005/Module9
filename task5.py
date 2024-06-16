def is_prime(func):
    def wrapper(*sum):
        result = func(*sum)
        if result > 1:
            for i in range(2, (result // 2) + 1):
                if (result % i) == 0:
                    print("Состовное")
                    break
            else:
                print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(*numbers):
    sum = 0
    for namber in numbers:
        sum += namber
    return sum


result = sum_three(2, 3, 6)
print(result)

