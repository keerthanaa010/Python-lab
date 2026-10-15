def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    print("--- School Portal: Exam Registration Verification ---")
    
    
    n = int(input("Enter the total number of registered students: "))
    registered_students = []
    
    print(f"Enter the roll numbers of the {n} registered students:")
    for i in range(n):
        roll = int(input(f"Student {i + 1} roll number: "))
        registered_students.append(roll)
        
    print("\nRegistered Student Roll Numbers:", registered_students)
    
    
    target_roll = int(input("\nEnter the roll number to search/verify: "))
    
   
    linear_result = linear_search(registered_students, target_roll)
    
    sorted_students = sorted(registered_students)
    binary_result = binary_search(sorted_students, target_roll)
    
    
    print("\n--- Search Results ---")
    if linear_result != -1:
        print(f"Linear Search: Roll number {target_roll} found at index {linear_result}.")
    else:
        print(f"Linear Search: Roll number {target_roll} not found.")
        
    if binary_result != -1:
        print(f"Binary Search: Roll number {target_roll} found at index {binary_result} (in sorted order).")
    else:
        print(f"Binary Search: Roll number {target_roll} not found.")
