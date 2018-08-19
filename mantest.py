import json
import random
import time

# import json questions
with open("questions.json") as json_file:
    data = json.load(json_file)
    q = data["questions"]

qlength = len(q)
qlist = [0]
number = 0
while len(qlist) <= qlength - 1:
    number += 1
    qlist.append(number)
quest3 = random.choice(qlist)
qlist.remove(quest3)
quest4 = random.choice(qlist)
qlist.remove(quest4)
quest5 = random.choice(qlist)
qlist.remove(quest5)

# question 1 + 2
print("Question 1. How old are you?")
print("Enter age")
ans1 = int(input())
print("Ok, What do you identify as?")
print("['1. Man', '2. Woman', '3. Other']")
print("Enter answer number")
ans2 = int(input())
if ans2 == 1 or ans2 == 2 or ans2 == 3:
    print("Ok, next question")
else:
    print("Re-enter answer")
    ans2 = int(input())
# question 3
print("Question 3. " + q[quest3]["question"])
print(q[quest3]["options"])
print("Enter answer number")
ans3 = int(input())
if ans3 == 1 or ans3 == 2 or ans3 == 3:
    print("Ok, next question")
else:
    print("Re-enter answer")
    ans3 = int(input())
# question 4
print("Question 4. " + q[quest4]["question"])
print(q[quest4]["options"])
print("Enter answer number")
ans4 = int(input())
if ans4 == 1 or ans4 == 2 or ans4 == 3:
    print("Ok, next question")
else:
    print("Re-enter answer")
    ans4 = int(input())
# question 5
print("Question 5. " + q[quest5]["question"])
print(q[quest5]["options"])
print("Enter answer number")
ans5 = int(input())
while ans5 == 1 or ans5 == 2 or ans5 == 3:
    print("Ok, your done calculating you total")
else:
    print("Re-enter answer")
    ans5 = int(input())
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")

# Scoring
total = 0
total += ans1 // 10
if ans2 == 1:
    total += 3
else:
    total += 1
points = q[quest3]["points"]
total += points[ans3 - 1]
points = q[quest4]["points"]
total += points[ans4 - 1]
points = q[quest5]["points"]
total += points[ans5 - 1]
print("you have a total of " + str(total) + " manliness points!")
end = input()
