if __name__ == '__main__':
    n = int(input('enter num: '))
    lst = [0] * n

    for pos in range(n):
        name, age, salary = input('enter: ').split()
        lst[pos] = name, int(age), int(salary)  #tuple

    lst.sort()
    for idx, (name, age, salary) in enumerate(lst): #deep unpacking
        print(idx, name, age, salary)

