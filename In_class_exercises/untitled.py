list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

l1_dif = set(list1).difference(set(list2))
l2_dif = set(list2).difference(set(list1))

print(l2_dif, l1_dif)