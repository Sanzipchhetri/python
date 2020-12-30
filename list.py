
test_list = [1, 7, 5, 6, 3, 8] 
  
# initializing k 
k = 4
  
# printing list  
print ("The list : " + str(test_list)) 
  
# using naive method  
# to get numbers > k 
count = 0
for i in test_list : 
    if i > k : 
        count = count + 1
  
# printing the intersection  
print ("The numbers greater than 4 : " + str(count))