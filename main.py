num = int(input())
sum1 = 0
for i in range(1, num):
    if(num % i == 0):
        sum1 = sum1 + i
if (sum1 == num):
    print("Đây là số hoàn hảo")
else:
    print("Đây không phải là số hoàn hảo.")
reverse = 0
while num!=0:
  rem = num%10
  reverse = rem + (reverse*10)
  num = int(num/10)
if reverse == num:
  print("Đây là số đối xứng")
else:
  print("Đây không phải là số đối xứng")