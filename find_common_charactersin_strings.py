def common_letters():
  try:    
    
    str1 = input("enter first string: ")
    str2 = input("enter second string: ")
    
    st1=set(str1)
    st2=set(str2)
    
    common=st1&st2
    return common
  except Exception as e:
    print("an error occured",e)
    return None

    
common_chars=common_letters() 
if common_chars:
    print("Common characters:", common_chars)
else:
    print("No common characters found.")
