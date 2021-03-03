
# Python program to explain os.path.exists() method   
      
# importing os module   
import os  
    
# Specify path  
path = '/usr/local/bin/'
    
# Check whether the specified  
# path exists or not  
isExist = os.path.exists(path)  
print(isExist)  
    
    
# Specify path  
path = '/home/ubuntuclient/Desktop/file.txt'
    
# Check whether the specified  
# path exists or not  
isExist = os.path.exists(path)  
print(isExist)  
