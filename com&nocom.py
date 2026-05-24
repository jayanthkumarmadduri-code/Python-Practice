list1 = list(map(int, input("Enter first list elements separated by space: ").split()))
list2 = list(map(int, input("Enter second list elements separated by space: ").split()))
set1 = set(list1)
set2 = set(list2)
if set1.isdisjoint(set2):
    print("The lists share NO common elements")
else:
    print("The lists share common elements")