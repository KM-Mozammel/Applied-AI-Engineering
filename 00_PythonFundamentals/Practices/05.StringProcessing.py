# Exercise 1: একটি String কে শব্দে ভাগ করো।
string = "I love coding"
words = string.split()
# print(words)

# --------------------------------
# Exercise 2: একটি List কে "-" দিয়ে Join করো।
words = ["What", "is", "Love"]
results = "-".join(words)
# print(results)

# --------------------------------
# Exercise 3: সব "Python" কে "AI" দিয়ে Replace করো।
word = "Python"
replaced = word.replace("Python", "AI")
# print(replaced)

# --------------------------------
# Exercise 4: একটি Email ".com" দিয়ে শেষ হয়েছে কিনা দেখো।
email = "example@gmail.com"
# print(email.endswith(".com"))
# --------------------------------
# Exercise 5: Extra Space Remove করো।
words = " Hello "
# print(words)
# print(words.strip())
# --------------------------------
# Exercise 6: নিজের নাম ও বয়স f-string দিয়ে Print করো।
name = "Mozammel"
age = 27
# print(f"My name is {name}, age is {age}")
# --------------------------------
# Exercise 7: Regex ব্যবহার করে একটি Paragraph থেকে সব সংখ্যা বের করো।
import re
paragraph = "My phone number is: 01795593541"
# print(re.findall(r"\d+", paragraph))
# --------------------------------
# Exercise 8: Regex ব্যবহার করে সব Email বের করো।
EmailInString = "mk@gmail.com, welcome to abcd@email.com"
# print(re.findall(r"\S+@\S+", EmailInString))
# --------------------------------
# Exercise 9: একটি URL "https://" দিয়ে শুরু হয়েছে কিনা দেখো।
url = "https://facebook.com"
# print(url.startswith("https://"))
# --------------------------------
# Exercise 10: CSV String কে List-এ Convert করো।
data = "Name, Age, City"
print(data.split(","))
