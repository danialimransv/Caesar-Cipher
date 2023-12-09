def caesar_cipher(message, key, mode):
  Letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  translated = ''
  message = message.upper()
  key = key % 26

  for i in message:
      tempLetter = Letter.find(i)
      if mode == 'encrypt':
          tempLetter += key
      elif mode == 'decrypt':
          tempLetter -= key
      if tempLetter >= len(Letter):
          tempLetter -= len(Letter)
      elif tempLetter < 0:
          tempLetter += len(Letter)
      translated += Letter[tempLetter]
  return translated


# Allow user input
user_message = input("Enter the message: ")
user_key = int(input("Enter the key (an integer): "))
user_mode = input("Enter the mode (encrypt/decrypt): ").lower()

# Validate mode input
if user_mode not in ['encrypt', 'decrypt']:
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
else:
  result = caesar_cipher(user_message, user_key, user_mode)
  print("Results:",result)