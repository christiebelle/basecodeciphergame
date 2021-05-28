#The task message is what tells the programme what function to carry out: either encrypting or decrypting
task = input('Do you want to encrypt (e) or decrypt (d) a message? ')

#These are the accepted options for the input - anything other than an e/d/bf/q will break the application
while task = 'e' or task 'd' or task = 'bf':
  
  #The alphabet array lists out all 26 letters of the alphabet - they are only lowercase for now, but we will be looking at this later on in the session
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  
  #The newMessage variable is currently set to empty, this is where our encrypted/decrypted message will eventually live
  newMessage = ''
  
  #So we have taken in a task, now we need an actual message to work on. This is what this line does.
  message = input('Please enter a message: ')
  
  #Now we come on to our conditional logic statements that tell the programme how to behave and what to do with our message.
  #The first condition handles the logic if we are encrypting a message.
  if task == 'e':
  
