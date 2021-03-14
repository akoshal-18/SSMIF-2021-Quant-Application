# This is Arjun Koshal's SSMIF Quant 21 Application
# 3.1 Divisible

def divisible(s, x):

    string = s
    integer = x

    new_string = string.replace(str(integer), "_")

    nums = list(map(int, ''.join([y if y.isdigit() else ' ' for y in new_string]).split()))

    empty = []
    for i in range(len(nums)):
        f = str(nums[i])
        l = len(f)
        list1 = [int(f[n:j + 1]) for n in range(l) for j in range(n, l)]
        empty.extend(list1)
    try:
        divisible_list = [k for k in empty if k % x == 0] if x != 0 else print("[]")
        divisible_list.sort()
        final_divisible_list = [i for n, i in enumerate(divisible_list) if i not in divisible_list[:n]]
        print(final_divisible_list)
    except AttributeError:
        pass

divisible("a465839485739b102988c30jklol4",7)