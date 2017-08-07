import sys
import math

counter = 0
def swap(i,j,array):
    tmp = array[i] #create a tmp variable which help to switch elements
    array[i] = array[j]
    array[j] = tmp

def quicksort(array,low,high):

    if low < high:
        pivot = partition(array,low,high)
        quicksort(array,low,pivot-1)
        quicksort(array,pivot+1,high)
    return array

def partition(array,low,high):
    global counter
    position = array[low] #taking first element as pivot
    left = low+1
    right = high
    swap_d = False

#check until the elements are swapped in correct positions
    while not swap_d:
        counter += (right - left)
        while right >= left and array[left] <= position:
            left += 1
        while position <= array[right] and right >= left:
            right -= 1
        if int(left) > int(right):
            swap_d =True
        else:
            swap(int(left),int(right),array)

    swap(low, right, array)
    return right
    counter = 0

def bubblesort(array):
    global counter
    print("Using Bubble Sort:")
    length = len(array)
    #loop all the elements in array and check the
    #  remaining with the first element selected.
    for i in range(length):
        for j in range(length-1, i, -1):
            counter += 1
            #check if one element in array is greater than
            #the other
            if(int(array[j]) < int(array[j-1])):
                #call swap function
                swap(j,j-1,array)

    ApproxMin = math.ceil(math.log(math.factorial(len(array)), 2))
    print(array)
    print("Comparision: " + str(counter))
    print("ApproxMin: " + str(ApproxMin))
    counter = 0

def insertion(array):
    global counter
    print("Using Insertion Sort:")
    length = len(array)
    for i in range(length):
        tmp = int(array[i])
        k = i
        #check element with tmp and swap until it reach
        #to the place where everything is sorted.
        while k > 0 and tmp < int(array[k - 1]):
            array[k] = array[k - 1]
            k = k-1
            array[k] = tmp
            counter += 1

    ApproxMin = math.ceil(math.log(math.factorial(len(array)), 2))
    print(array)
    print("Comparision: " + str(counter))
    print("ApproxMin: " + str(ApproxMin))
    counter = 0

def merge(left_part,right_part):
    global counter
    if not len(left_part):
        return right_part

    if not len(right_part):
        return left_part

    merge_result = []
    i = 0
    j = 0

    # Run till left part and right part does not less than 0
    #and arange them in sorted order
    while len(left_part) > i and len(right_part) > j:
        if int(left_part[i]) > int(right_part[j]):
            merge_result.append(right_part[j])
            j += 1
        else:
            merge_result.append(left_part[i])
            counter += (len(left_part) - j)
            i += 1

    #append all the elements
    merge_result = merge_result+left_part[i:]
    merge_result = merge_result+right_part[j:]

    return merge_result

def mergesort(array):
    global counter
    if len(array) <= 1: #return 1 element as a sorted array
        return array
    else:
    # find out the middle of array
        middle = int(len(array)/2)
        left_part = mergesort(array[:middle]) # taking all the elements before middle
        right_part = mergesort(array[middle:]) # taking all the elements after middle
    return merge(left_part,right_part)


if __name__ == '__main__':

    print("Welcome to the sorting thunderdome")
    print("This program is used to compare sorting methods")
    print("Commands: \n"
          "help - Prints this menu \n"
          "exit or CTRL-D - Exits the program \n"
          "sort_method int_list - Enter a sort method followed by a list of space sperated integers to sort them\n"
          "Possible Sort Methods: bubblesort insertion mergesort quicksort")

    while True:  # check until the exit or Ctrl+D is entered
        try:
            Command = input("Command: ")
            list_new = Command.split()
            array = []
            for i in range(len(list_new) - 1):
                array.append(int(list_new[i + 1]))

        except (EOFError):
            print("Bye")
            break
        if Command == "exit":
            print("Bye")
            sys.exit(0)

        elif Command == "help":
            print("Commands: \n"
                  "help - Prints this menu \n"
                  "exit or CTRL-D - Exits the program \n"
                  "sort_method int_list - Enter a sort method followed by a list of space sperated integers to sort them\n"
                  "Possible Sort Methods: bubblesort insertion mergesort quicksort")
        else:
            if list_new[0] == "bubblesort":
                bubblesort(array)

            elif list_new[0] == "insertion":
                insertion(array)

            elif list_new[0] == "mergesort":
                print("Using Merge Sort:")
                print(mergesort(array))
                ApproxMin = math.ceil(math.log(math.factorial(len(array)), 2))
                print("Comparision: " + str(counter))
                print("ApproxMin: " + str(ApproxMin))
                counter = 0

            elif list_new[0] == "quicksort":
                print("Using Quick Sort:")
                print(quicksort(array,0,len(array)-1))
                ApproxMin = math.ceil(math.log(math.factorial(len(array)), 2))
                print("Comparision: " + str(counter))
                print("ApproxMin: " + str(ApproxMin))
                counter = 0
            elif list_new[0] != "quicksort" or "mergesort" or "bubblesort" or "insertion":
                print("Sorry there is no options called " + list_new[0])
