#!/opt/homebrew/bin/python3

num1 = 0
num2 = 0
num3 = 0
sum_of_elfs = []
sum_of_top3_elfs = 0

f = open('./input1.txt', 'r')
for line in f:
    if line in ['\n', '\r\n']: 
        #print('************ Blank line found *************')
        num2 = num1
        num1 = 0
        sum_of_elfs.append(num2)
        #print('Sum of previous elf : ', num2)
        if (num2 > num3):
            num3 = num2
        #print('Elf with highest calorie so far : ', num3)
    else:
        num1 = num1 + int(line)
        #print(line)

print('Elf with highest calorie so far : ', num3)
sum_of_elfs.sort(reverse=True)
#print(sum_of_elfs)
print('Elf with top 3 calories : ', sum_of_elfs[0], sum_of_elfs[1], sum_of_elfs[2])

for i in range(0,3):
    sum_of_top3_elfs = sum_of_top3_elfs + sum_of_elfs[i]

print('Sum of top3 elfs calories : ', sum_of_top3_elfs)


