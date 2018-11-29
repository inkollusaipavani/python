str= raw_input()
count = 0
for x in str:
    if(x.isdigit()):
        count=count+1
print(count)
