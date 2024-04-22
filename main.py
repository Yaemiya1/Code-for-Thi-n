num = int(input())
sum1 = 0
for i in range(1, num):
    if(num % i == 0):
        sum1 = sum1 + i
if (sum1 == num):
    print("Đây là số hoàn hảo.")
else:
    print("Đây không phải là số hoàn hảo.")
num2 = num
reverse = 0
while num2!=0:
  digit = num2 % 10
  reverse = reverse * 10 + digit
  num2 //= 10
if num == reverse:
  print("Đây là số đối xứng.")
else:
  print("Đây không phải là số đối xứng")
