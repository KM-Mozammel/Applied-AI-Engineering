# Exercise 1: Input নিয়ে Positive/Negative Check করো।

# number = int(input("Enter your number:"))
# if number % 2 == 0:
#     print("This number is positive")
# else:
#     print("This number is negative!!")
    
# Exercise 2: Marks নিয়ে Grade বের করো।

# marks = int(input("Enter your marks: "))
# if marks >= 80:
#     print("You got a+")
# elif marks >= 70:
#     print("You got straight a")
# elif marks >= 60:
#     print("You got a-")
# elif marks >= 33:
#     print("You got b+")
# else: 
#     print("You are failed!!")

# Exercise 3: for Loop দিয়ে, 1-20 Print করো।

# for j in range(20):
#     print(j)
    
# Exercise 4: while দিয়ে ১০ থেকে ১ পর্যন্ত Countdown করো।

# count = 10
# while count > 0:
#     print(count)
#     count = count - 1

# Exercise 5: break ব্যবহার করে, 1-100 এর মধ্যে 50 এ Loop বন্ধ করো।

# count = 1
# while count < 100:
#     print(count)
#     count = count + 1
#     if count > 50:
#         break

# Exercise 6: continue ব্যবহার করে, Even Number Skip করো।

# count = 1
# while count < 100:
#     count = count + 1
#     if count % 2 == 0:
#         continue
#     print(count)
        
# Exercise 7: pass ব্যবহার করে, একটি Empty Function লিখো।
# def emptyFunction(): 
#     pass

# Exercise 8: match ব্যবহার করে, Week Day Print করো।

# day = 3
# match day:
#     case 1: 
#         print("Saturday")
#     case 2:
#         print("Sunday")
#     case 3:
#         print("Monday")
#     case 4:
#         print("Tuesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Wednesday")
#     case 7:
#         print("Friday")

# Exercise 9: 1-100 পর্যন্ত, সব Prime Number Print করো।

# list_of_prime = []
# for i in range(2, 101):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i)
#         list_of_prime.append(i)
        
# print(list_of_prime)

# Exercise 10: Nested for Loop দিয়ে, Pattern Print করো।
# *
# **
# ***
# ****
# *****
# """

# for i in range(2, 20):
#     for j in range(2, i + 1):
#         print("*", end = "")
#     print()