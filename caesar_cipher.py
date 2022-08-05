alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def Caesar(text, shift, message_type):
  total = ""#common line
  #sum = ""
  for i in range(len(text)):#common line
    if message_type == "encode":    
      pos = (alphabet.index(text[i]) + shift)
      while pos > 25:
        pos = pos-26
      total += (alphabet[pos])
      
    elif message_type == "decode":
      pos = (alphabet.index(text[i]) - shift)
      while pos < 0:
        pos = pos+26
      total += (alphabet[pos]) 
  print(f"The  message is : {total}")
    
at_goal = True
while at_goal == True:
  var = input("If you want to quit, press 'Q' and if not press 'Y' : \n")
  if var == 'Q' or var == 'q':
    at_goal = False
  elif var == 'y' or var == 'Y':    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  else:
    print("Please type as per the options provided")
  Caesar(text, shift, direction)
