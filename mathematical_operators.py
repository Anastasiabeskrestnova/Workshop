# The idea of this task was to create mathematical operators without using the minus sign as a binary operator.

def minus_a(lho, rho):

    return lho + int("-" + str(rho))


def add(lho,rho):

    return lho + rho


def multiply_a(lho, rho):
    if rho >= 3:
        lho_sum = lho + lho
        for _ in range(rho):
            lho_sum = lho_sum + lho

    elif rho == 0:
        lho_sum = 0

    elif rho == 1: 
        lho_sum = lho

    elif rho == 2:
        lho_sum = lho + lho

    return lho_sum


def multiply_b(lho, rho):
    lho_rho_times = 0

    for _ in range(rho):
        lho_rho_times += lho

    return lho_rho_times


def power(lho, rho):
    multiple = 1

    for _ in range(rho):
        multiple = multiply_b(multiple, lho)

    return multiple


def factorial(operand):
    factorial = 1

    for element in range(1, operand + 1):
        factorial = multiply_b(factorial, element)

    return factorial


def divide(lho, rho):
    sum = 0
    quotient  = 0

    if(lho >= 0 and rho >= 0) or (lho <= 0 and rho <= 0):
        sign = 1
    else:
        sign = -1

    if lho < 0:lho = -lho
    if rho < 0:rho = -rho

    while not sum >= lho:
        sum += rho
        quotient += 1

    quotient = quotient*sign

    return quotient