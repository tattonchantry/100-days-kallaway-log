# %% Challenge 1


def simpleArraySum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar = [1, 2, 3, 4, 10, 11]

    result = simpleArraySum(ar)

# %% Challenge 2


def compareTriplets(a, b):
    Bob = 0
    Alice = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            Bob += 1
        elif a[i] < b[i]:
            Alice += 1
    return [Bob, Alice]


a = [5, 6, 7]
b = [3, 6, 10]
r = compareTriplets(a, b)

# %% Cahllenge 3
a = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
b = sum(a)
print(b)

# %% Cahllenge 4
arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]
n = len(arr)
rightD = sum(arr[i][i] for i in range(n))
leftD = sum(arr[i][n-i-1] for i in range(n))
adddd = abs(leftD - rightD)

# %% Challenge 5
arr = [-4, 3, -9, 0, 4, 1]
positiveS = round(sum(arr[i] > 0 for i in range(len(arr)))/len(arr), 4)
print(positiveS)
negativeS = round(sum(arr[i] < 0 for i in range(len(arr)))/len(arr), 4)
print(negativeS)
zeroS = round(sum(arr[i] == 0 for i in range(len(arr)))/len(arr), 4)
print(zeroS)


# %% Challenge 6
def staircase(n):
    for i in range(n):
        print(str(' ' * (n - i - 1)) + str('#' * (i+1)))


n = 6
staircase(n)


# %% Challenge 6 again
n = 6
for i in range(1, n+1):
    print(('#'*i).rjust(n, ' '))

# %% Challenge 7
a = [1, 2, 3, 4, 5]


def minSum(a):
    print(str(sum(a) - max(a)) + ' ' + str(sum(a) - min(a)))


minSum(a)

# %% Challenge 8


def birthdayCakeCandles(ar):
    ma = max(ar)
    cnt = len(ar) - 1
    cntr = 0
    while cnt >= 0:
        if (ar[cnt] == ma):
            cntr += 1
        cnt -= 1
    print(cntr)


ar = [3, 2, 1, 3]
birthdayCakeCandles(ar)


# %%

def ConvertToMil(ti):
    hrs, mins, secsAP = ti.split(':')
    secs = secsAP[:2]
    me = secsAP[-2:]
    if me == 'PM':
        new_hrs = hrs
        if hrs != '12':
            new_hrs = int(hrs) + 12
    elif me == 'AM' and hrs == '12':
        new_hrs = '00'
    else:
        new_hrs = hrs
    new_time = f'{new_hrs}:{mins}:{secs}'
    return new_time


times = ['06:05:39AM', '12:15:39AM', '12:05:39PM', '01:05:39AM', '01:05:39PM']
for ti in times:
    print(ConvertToMil(ti))

# %%
"""
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
"""
def Prntr(n):
    if n%2 > 0 or (n >= 6 and n <= 20):
        print('Weird')
    elif (n >= 2 and n <= 5) or n > 20:
        print('Not Weird')

n = 3

# %%
"""
The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
 while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT
"""
def is_leap(year):
    leap = False
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            leap = False
            if year%400 == 0:
                leap = True
    # Write your logic here

    return leap

year = 2400
print(is_leap(year))

# %%
"""
Read an integer N
Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between.
Input Format
3
The first line contains an integer N
Output Format
123
Output the answer as explained in the task.
"""
def printer(n):
    for i in range(n):
        print(i+1, end='')


n = 5
printer(n)


