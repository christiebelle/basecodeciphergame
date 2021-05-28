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
    key = input('Please enter a key - this will be a number between 1 and 25: ') #Our key will set how much we scramble the message
    for letter in message: #The variable 'letter' here is a new variable and refers to each individual letter in the message, so this line is saying for each letter in our message do the following...
      if letter in alphabet: #This step is checking that the letter is in our alphabet array above, and if it is then it will...
        position = alphabet.find(letter) #Find the position of the letter in the array and give it a numeric position - remembering that array counts start from 0
        newPosition = (int(position) + int(key)) % 26 #This part is where we do the shuffling. We take the position (now a number remember) and add the key to it. Then the '% 26' is dividing (position + key) by 26, and whatever the remainder is becomes our newPosition
        newLetter = alphabet[newPosition] #We then take the newPosition number and search through the alphabet array to find the letter at that position, and this becomes our newLetter - our encrypted letter
        newMessage += newLetter #Now we add the newLetter to the newMessage and go back to the start of the loop
      else: #The condition for what happens if the letter is not in the alphabet array. For now - we just simply add it to the newMessage as it it
        newMessage += letter
    print('Your message is now: ' + newMessage) #We then print out the newMessage which - if we have done our jobs correctly - be encrypted jibberish
    task = input('Do you want to encrypt (e) or decrypt (d) a message? ') #And so we start again
  elif task == 'd': #Now we move on to the logic for decrypting a message
    key = input('Please enter a key - this will be a number between 1 and 25: ') #So far we have the same set up as for encrypting. We need a message and a key to work with still
    for letter in message: #And we are still going to be looping through the message in the exact same way as we do for encryption. The difference is that this time...
      if letter in alphabet:
        position = alphabet.find(letter)
        newPosition = (int(position) - int(key)) % 26 #Instead of adding the position and key together, we are subtracting them from each other, before we do the % 26. The remainder again becomes our newPosition
        newLetter = alphabet[newPosition] #And then we move back to the same steps as before - finding the letter at our newPosition and adding it to our message
        newMessage += newLetter
      else:
        newMessage += letter
    print('Your message is now: ' + newMessage) #This will be our decrypted message
    task = input('Do you want to encrypt (e) or decrypt (d) a message? ') #And here we go again!
  elif task == 'bf': #BONUS CONTENT! So 'bf' stands for brute force - which is a form of attack against our code that is going to tell the computer to print out all the combinations and keys our encrypted message could be  
    for i in range(len(alphabet)): #Slightly different approach to the conditions here, as we are now saying that we are working with every letter in the alphabet array, and these intructions are telling the computer to list out each combination of letters for keys 1-25
      newMessage = '' #newMessage is being set empty here as each time we loop through we will need a new empty message
      for letter in message:
        if letter in alphabet: #Brute force is forcing the computer to tell us all the possible decrypted combinations, so in this next section we are using the same decryption logic as above
          position = alphabet.find(letter)
          newPosition = (int(position) - i) % 26
          newLetter = alphabet[newPosition]
          newMessage += newLetter
        else:
          newMessage += letter
      print('Key #%s: %s'%(i, newMessage)) #This will print out the number of the key and the possible message that could be
    task = input('Do you want to encrypt (e) or decrypt (d) a message? ') #And here we go again!
  elif task == 'q': #And this quits the application
    print('Thank you! Goodbye!')
    break
