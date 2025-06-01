#simon parker

#this takes a ternary string (state representation for robby) andturns it into an index for the Q-matrix
#5 digit ternary string
def ter_to_dec(string):
  result = 0
  for i in range(len(string)):
    result += int(string[i]) * pow(3, len(string) - i - 1)
  return result

x = ter_to_dec("22222")
print(x)
    
