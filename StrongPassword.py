password=input()
sc=["!","@","#","$","%","^","&","*","(",")"]
if len(password)>=8:
  if len(password)<=24:
    if " " not in password:
      i,cA=0,0
      ca,cn,cs=0,0,0
      while i<len(password):
        if password[i]>="A" and password[i]<="Z":
          cA+=1
        elif password[i]>="a" and password[i]<="z":
          ca+=1
        elif password[i]>="0" and password[i]<="9":
          cn+=1
        elif password[i] in sc:
          cs+=1
        i+=1
      if cA>0 and ca>0 and cn>0 and cs>0:
        print("Strong password")    
      if cA<=0:
        print("1 uppercase character should be present at least.")
      if ca<=0:
        print("1 lowercase character should be present at least.")
      if cn<=0:
        print("1 number should be present at least.")
      if cs<=0:
        print("1 special character should be present at least.")
      else:
        print()
    else:
      print("Space cann't be in password.")        
  else:
    print("You exceed the limit, password shouldn't be more then 24 characters long.")      
else:
  print("Password should be 8 characters long at least.")