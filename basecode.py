task = input('Do you want to encrypt (e) or decrypt (d) a message? ')

while task == 'e' or task == 'd':
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  newMessage = ''
  
  message = input('Please enter a message: ')
  
  if task == 'e':
    key = input('Please enter a key - this will be a number between 1 and 25: ')
    for letter in message:
      if letter in alphabet:
        position = alphabet.find(letter)
        newPosition = (int(position) + int(key)) % 26
        newLetter = alphabet[newPosition]
        newMessage += newLetter
      else:
        newMessage += letter
    print('Your message is now: ' + newMessage)
    task = input('Do you want to encrypt (e) or decrypt (d) a message? ')
  elif task == 'd':
    key = input('Please enter a key - this will be a number between 1 and 25: ')
    for letter in message:
      if letter in alphabet:
        position = alphabet.find(letter)
        newPosition = (int(position) - int(key)) % 26
        newLetter = alphabet[newPosition]
        newMessage += newLetter
      else:
        newMessage += letter
    print('Your message is now: ' + newMessage)
    task = input('Do you want to encrypt (e) or decrypt (d) a message? ')
  elif task == 'q':
    print('Thank you! Goodbye!')
    break
