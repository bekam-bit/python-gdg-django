
# # 1
# def checkDiscount():
#     numOfProducts=int(input("Enter the number of products: "))

#     if numOfProducts>3:
#         print(" discounts applied")
#     else:
#         print("no discounts applied")
    
# checkDiscount()

#2
# def getExpensiveProsucts(prices):
#     filteredProducts=[]
#     for price in prices:
#         if price > 100:
#             filteredProducts.append(price)
#     return filteredProducts

# prices=[120, 45, 300, 85, 150]
# print(getExpensiveProsucts(prices))

# #3
# def logger():
#     with open("log.txt","a")as file:
#         file.write("User logged in")
#     with open("log.txt","r")as file:
#         for line in file:
#             print(line.strip())
# logger()

#4
def get_grade(student_grades,student_name):
    try:
        return student_grades[student_name]
       
    except KeyError:
        return "Student not found"
    
print(get_grade({"John": 85, "Alice": 92, "Bob": 78}, "Bob"))

#5 

