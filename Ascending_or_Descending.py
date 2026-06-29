# Input the size of the array
n = int(input("Enter the size of the array: "))

# Input array elements
arr = []

print("Enter the array elements:")
for i in range(n):
    arr.append(int(input()))

# Menu
while True:
    print("\n----- MENU -----")
    print("1. Sort in Ascending Order")
    print("2. Sort in Descending Order")
    print("3. Display Array")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr.sort()
        print("Ascending Order:", arr)

    elif choice == 2:
        arr.sort(reverse=True)
        print("Descending Order:", arr)

    elif choice == 3:
        print("Current Array:", arr)

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice! Please try again.")