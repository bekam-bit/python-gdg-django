from typing import List
#1
def checkDiscount():
    numOfProducts=int(input("Enter the number of products: "))

    if numOfProducts>3:
        print(" discounts applied")
    else:
        print("no discounts applied")
    
checkDiscount()

#2
def getExpensiveProsucts(prices):
    filteredProducts=[]
    for price in prices:
        if price > 100:
            filteredProducts.append(price)
    return filteredProducts

prices=[120, 45, 300, 85, 150]
print(getExpensiveProsucts(prices))

# #3
def logger():
    with open("log.txt","a")as file:
        file.write("User logged in")
    with open("log.txt","r")as file:
        for line in file:
            print(line.strip())
logger()

#4
def get_grade(student_grades,student_name):
    try:
        return student_grades[student_name]
       
    except KeyError:
        return "Student not found"
    
print(get_grade({"John": 85, "Alice": 92, "Bob": 78}, "Bob"))

#5
def sales():
    sales=[200,450,"abc",700]
    with open("sales.txt","w") as file:
        for sale in sales:
            file.write(str(sale)+"\n")
sales()

#6
def readSales():
    sales=[]
    with open("sales.txt","r") as file:
        for line in file:
            line=line.strip()
            try:
                sale=int(line)
                sales.append(sale)
            except ValueError:
                continue
        total_sales=sum(sales)
        print("Total sales: ", total_sales)
readSales()

#7
def FizzBuzz(n:int)->List[str]:
    ans=[]
    for i in range(1,n+1):
        if i%3 == 0 and i%5==0:
            ans.append("FizzBuzz")
        elif i%3 == 0:
            ans.append("Fizz")
        elif i%5==0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans
print(FizzBuzz(3))

#8
def moveAllZerosOpt(nums):
    pos=0
    n=len(nums)
    for i in range(n):
        if n == 1:
            return [nums[0]]
        if nums[i]!=0:
            if pos!=i:
                nums[pos],nums[i]=nums[i],nums[pos]
            pos += 1
    return nums
print(moveAllZerosOpt([0,1,0,3,12]))
print(moveAllZerosOpt([0]))

#9
def SumEqualToTarget(nums:List,target:int)->List[int]:
    dict={}
    n=len(nums)
    for i,num in enumerate(nums):
        comp=target-num
        if comp in dict:
            return [i,dict[comp]]
        dict[num]=i
print(SumEqualToTarget([2,7,11,15],9))

#10
def isPaildrome(x:int)->bool:
    reverse=0
    original=x
    if x<0:
        return False
    while x>0:
        unit=x%10
        reverse=reverse*10+unit
        x=x//10
    return original == reverse 
print(isPaildrome(121))
print(isPaildrome(-121))

#11
def Sqroot(x):
    left=0
    right=x

    while left <= right:
        mid=(left+right)//2
        if mid*mid <= x:
            left=mid+1
        else:
            right=mid-1
    return right
print(Sqroot(8))

#12
def numbers():
    n=[10,20,30,"abc",40]
    with open("numbers.txt","w") as file:
        for nu in n:
            file.write(str(nu)+"\n")
    nums=[]
    with open("numbers.txt","r") as file:
        for line in file:
            line=line.strip()
            try:
                num=int(line)
                nums.append(num)
            except ValueError:
                continue
        total_sum=sum(nums)
        print("Sum of integers: ", total_sum)
numbers()

#13
def toUpperCase():
    with open("message.txt","w") as file:
        file.write("Python is fun")
    with open("message.txt","r") as file:
        for line in file:
            line=line.strip()
            upper_text=line.upper()
            return upper_text
print(toUpperCase())

#14
def scores():
    scores = {"John": 85, "Sara": 92, "Fraol": 78}
    name=input("Enter a student name: ")
    try:
        return scores[name]
    except KeyError:
        return "Student not found!"
print(scores())

#15
def word_dict(sentence:str):
    words=sentence.split(" ")
    word_freq={}

    for word in words:
        word_freq[word]=word_freq.get(word,0)+1
    return word_freq
print(word_dict("python is fun and python is powerful"))

#16
def KeysToValues():
    grades = {"John": "A", "Sara": "B", "Musa": "A"}
    new_grades={}
    key_list=[]
    for key,val in grades.items():
        if val in new_grades:
            new_grades[val].append(key)
        else:  
            new_grades[val]=[key]
    return new_grades
print(KeysToValues())