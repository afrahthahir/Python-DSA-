# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190


# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses = [2200, 2350, 2600, 2130, 2190]
print("dollars spent extra in feb compared to jan", expenses[1] - expenses[0])

total_3months = expenses[0] + expenses[1] + expenses[2]
print("total expense for first 3 months", total_3months)

print("Did i spend 2000 in any month?", 2000 in expenses)

expenses.append(1980)
print("June expenses added", expenses)

expenses[3] = expenses[3] - 200
print("Returned item on april, got refund for 200. So, i get 200 profit from the expenses", expenses[3])


heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print("Length of the list", len(heros))

heros.append("black panther")
print("Black panther added at end of the list", heros)

heros.remove("black panther")
print("black panther removed", heros)
heros.insert(3, "black panther")
print("black panther inserted after hulk", heros)

# heros.remove("thor")
# heros.remove("hulk")
# heros.insert(2, "doctor strange")
#above code done in one line of code below
heros[1:3] = ["doctor strange"]
print("removed thor and hulk and replaced doctor strange",heros)

heros.sort()
print("sorted",heros)

# print(dir(heros))






