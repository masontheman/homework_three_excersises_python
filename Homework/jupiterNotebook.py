def cubedNumbers():
    print([pow(x,3) for x in range(0,11)])
def primeNumbers():
    print([x for x in range(2, 101) if x not in set(j for i in range(2, 8) for j in range(i*2, 101, i))])
def AgeInputs(age):
    print('sorry not a number') if type(age) == str else print('adult') if age > 17 else print('kid') if age <= 17 else print('sorry not a number')