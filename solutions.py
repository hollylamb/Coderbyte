#letter capitalise challenge

def letterCapitalise(str):
 return (str.title())

print (letterCapitalise(input()))


#simplesymbolschallenge

def SimpleSymbols(str): 
  
  str = '=' + str + '='

  for i in range(0, len(str)):
     
    if str[i].isalpha():

  
      if str[i-1] != '+' or str[i+1] != '+':
        return False

  return True
