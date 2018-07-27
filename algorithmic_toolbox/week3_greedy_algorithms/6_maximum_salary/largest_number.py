#Uses python3


def largest_number(a):
    a.sort(key=cmp_to_key(my_cmp), reverse=True)
    return int(''.join([str(x) for x in a]))


def my_cmp(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)):
        return 1
    elif int(str(a) + str(b)) < int(str(b) + str(a)):
        return -1
    if int(str(a) + str(b)) == int(str(b) + str(a)):
        return 0


def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


# a, b = [int(x) for x in input().split()]
# print(my_cmp(a, b))


n = int(input())
nums = [int(x) for x in input().split()]
print(largest_number(nums))
