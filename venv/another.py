var_t = 'naman'
print(list(var_t))
#Python Function
def func():
    print("This is Python "+var_t)

func()


#globalplay-off
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#some practise

string1 = "aieou dubey"
a = {}

for i in string1:
    if i not in a and i != " ":
        a[i] = "none"

print(a.keys())
lis1 = []
for b in a.keys():
    if b not in lis1:
        lis1.append(b)
print(lis1)

ad = " ".join(lis1)
print(ad)


#prime including factors mumber
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


#even0odd
for i in range(2,10):
    if i % 2 == 0:
        print("found an even number", i)
        continue
    print("Found a number")


def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_pos = None
    for num in in_list:
        if num > 0:
            # Note: we use a logical "or" in this solution to form
            # the conditional statement, although this was
            # not introduced above.
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None


e = [1,2,3]
f = sorted([4,1,2])
print(f)
if e == f:
    print("Got")
else:
    print("Not Got")

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)