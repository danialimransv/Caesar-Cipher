def caesar(message, key, mode):
  Letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  translated = ''
  message = message.upper()
  key = key % 26
  
  for i in message:
    tempLetter = Letter.find(i)
    if mode == 'encrypt':
      tempLetter += key
     # print("encrypt")
    elif mode == 'decrypt':
     # print("decrypt")
      tempLetter -= key
    if tempLetter >= len(Letter):
      tempLetter -= len(Letter)
    elif tempLetter < 0:
     tempLetter += len(Letter)
    translated += Letter[tempLetter]
  return translated

print(caesar("BURGER", 6, 'encrypt'))
print(caesar("HAXMKX", 6, 'decrypt'))

