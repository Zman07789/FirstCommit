'''Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, 
and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message
 and skip to the next number '''
# this code was written by Zaackary Paulson


values=[] # i just decided to make an array because it was easier for me at least
while True:  
    num =input('Please type in a number: ')
    if num == 'done':
        break
    try:
        B=int(num)
        values.append(B) 
    except:
        print ('Invalid input')

total= sum(values)
average= total/(len(values))

print ("The total is ", total,  "the count is ", len(values), "and the average is ", average)