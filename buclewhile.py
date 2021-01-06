numbers = [1,2,3,4,5,6,7,8,9,10]
value = 1
while value in numbers:
    if value == 5:
        break
    print('Im  ' + str(value))
    value = value + 1
  
print('Sorry, I had to quit the loop when the value became 5')