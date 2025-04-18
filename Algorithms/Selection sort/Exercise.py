
def selectionSort(arr):
   
   for i in range(len(arr)):
       minIndex = i
       for j in range(minIndex+1, len(arr)):
           if arr[j]['First Name'] < arr[minIndex]['First Name']:
               minIndex = j

           elif arr[j]['First Name'] == arr[minIndex]['First Name']:
               if arr[j]['Last Name'] < arr[minIndex]['Last Name']:
                   minIndex = j
       if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
   


if __name__ == "__main__":
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    selectionSort(elements)
    print(elements)




