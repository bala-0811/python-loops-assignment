
print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
for temp in temperatures:
 if temp>32:
  print(f"Highest Temp:{temp}")
 elif temp<28:
  print(f"Lowest temp:{temp}")

print("\n===== Task 2: Count Hot Days =====")

temperatures = [28, 32, 35, 29, 31, 27, 30]
count = 0
for temp in temperatures:
 if temp<=30:
  continue
 count += 1
print(f"Hot days(>30°C):{count}")

print("\n===== Task 3: Alert System =====")

temperatures = [28, 32, 35, 40, 31, 33, 30]
count=0
day=0
for temp in temperatures:
 day+=1
 if temp>=40:
  break
 if temp>30:
  count+=1
print("Hot Days Before Alert", count)
print("Alert! Extreme temperature 40°C detected on Day", day)




 



