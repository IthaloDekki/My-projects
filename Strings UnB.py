string = input()
count = 0 
space = len(string)

while count < space:
    if (count % 2) != 0 and string[count] != " ":
        print(string[count], end='')
    count += 1