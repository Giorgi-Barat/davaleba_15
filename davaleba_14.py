
def quicksort(arr):

    if len(arr) <= 1:

        return arr

    else:

        pivot = arr[0]

        left = [x for x in arr[1:] if x < pivot]

        right = [x for x in arr[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)

while True:
    user_input = input("Enter the array elements separated by spaces and please use only numbers: ")

    try:
        list = [int(x) for x in user_input.split()]
    except ValueError:
        continue

    list2 = [int(x) for x in user_input.split()]

    if len(list2) < 3 or len(list2) % 2 == 1:
        print("Len list must be more then 3, and must be even amounts")
        continue

    break

arr = [int(x) for x in user_input.split()]

sorted_arr = quicksort(arr)

n = 1
differance = []
for i in range(len(sorted_arr) -1):
    differance.append(sorted_arr[n-1] - sorted_arr[n])
    n +=1

print("Sorted array:", sorted_arr)
print(min(differance))

print("buy buy")

print("just for practice")