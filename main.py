import random, time, sys

#colors 
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
Black = "\033[0;30m"
Black = "\033[0;90m"
Green = "\033[0;92m"
Yellow = "\033[0;93m"
Blue = "\033[0;94m"
Magenta = "\033[0;95m"
Cyan = "\033[0;96m"
White = "\033[0;97m"
Bold = "\033[1m"
Underline = "\033[4m"
Italic = "\033[3m"
Darken = "\033[2m"
Reset = "\033[0m"


def s_print(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.04)
  print()

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()
  return value


s_print(Red + Bold + "Welcome to this quiz about Energy!")
s_print("")
time.sleep(1.5)

greetings = ["Hi, ", "Hello, ", "Nice to meet you, ", "I hope you're having a good day, "]

loop = True
while loop:
  Name = typingInput(Green + "What is your name?" + Blue + "\n")
  time.sleep(0.5)
  s_print(Green + random.choice(greetings) + Name)
  time.sleep(0.5)
  s_print("")
  time.sleep(0.5)
  
  s_print (Cyan +"I will ask you 10 questions and give you four choices for each question.")
  s_print("You select which choice is the correct answer. Eg. (a), (b), (c) or (d)")
  time.sleep(2.5)
  s_print("")
  time.sleep(0.5)

  score = 0
  score = int(score)

  s_print(Magenta + "Question 1")
  time.sleep(1)
  s_print(Magenta + "Which of the following is a non-renewable source of energy?")
  time.sleep(0.5)
  s_print(Cyan + " (a) Wood\n (b) Sun\n (c) Fossil fuels\n (d) Wind")
  time.sleep(1.5)
  s_print("")
  time.sleep(0.5)

  q1_answer = "c"
  q1_answer = q1_answer.lower()
  q1_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q1_response != q1_answer):
    time.sleep(1)
    s_print ("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was, " + q1_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 150")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q1_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 150")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  
  s_print(Magenta + "Question 2")
  time.sleep(1)
  s_print(Magenta + "Acid rain happens because:")
  time.sleep(0.5)
  s_print(Cyan +" (a) Sun heats up the upper layer of the atmosphere.\n (b) burning of fossil fuels releases oxides of carbon, nitrogen and sulphur in the atmosphere.\n (c) electrical charges are produced due to friction amongst clouds.\n (d) earth atmosphere contains acids.")
  time.sleep(1.5)
  s_print("")
  time.sleep(0.5)
  
  q2_answer = "b"
  q2_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q2_response != q2_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was, " + q2_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 150")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q2_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 150")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  s_print(Magenta +"Question 3")
  time.sleep(1)
  s_print(Magenta +"Fuel used in thermal power plants is:")
  time.sleep(0.5)
  s_print(Cyan +" (a) water\n (b) uranium\n (c) biomass\n (d) fossil fuels")
  time.sleep(0.5)
  s_print("")
  time.sleep(1.5)
  
  q3_answer = "d"
  q3_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q3_response != q3_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was" + q3_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 150")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    
    s_print("Welldone! " + q3_answer + " is correct!")
    
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 150")
    
    s_print("")
    

  s_print(Magenta + "Question 4")
  time.sleep(1)
  s_print(Magenta + "In a hydro power plant:")
  time.sleep(0.5)
  s_print(Cyan +" (a) potential energy possessed by stored water is converted into electricity.\n (b) kinetic energy possessed by stored water is converted into potential energy.\n (c) electricity is extracted from water.\n (d) water is converted into steam to produce electricity.")
  time.sleep(0.5)
  s_print("")
  time.sleep(1.5)
  
  q4_answer = "a"
  q4_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q4_response != q4_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was " + q4_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q4_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  s_print(Magenta + "Question 5")
  time.sleep(1)
  s_print(Magenta + "A fuel cell, in order to produce electricity, burns:")
  time.sleep(0.5)
  s_print(Cyan +" (a) Helium\n (b) Nitrogen\n (c) Hydrogen\n (d) None of the above")
  time.sleep(0.5)
  s_print("")
  time.sleep(1.5)
  
  q5_answer = "c"
  q5_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q5_response != q5_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was " + q5_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q5_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  s_print(Magenta + "Question 6")
  time.sleep(1)
  s_print(Magenta + "The one thing that is common to all fossil fuels is that they: ")
  time.sleep(0.5)
  s_print(Cyan +" (a) Were originally formed in marine environment\n (b) Contains carbon\n (c) Have undergone the same set of geological processes during their formation\n (d) Represent the remains of one living organisms")
  time.sleep(0.5)
  s_print("")
  time.sleep(1.5)
  
  q6_answer = "b"
  q6_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q6_response != q6_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was " + q6_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q6_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  s_print(Magenta + "Question 7")
  time.sleep(1)
  s_print(Magenta + "The energy possessed by an oscillating pendulum of a clock is:")
  time.sleep(0.5)
  s_print(Cyan +" (a) kinetic energy\n (b) potential energy\n (c) restoring energy\n (d) mechanical energy")
  time.sleep(0.5)
  s_print("")
  time.sleep(1.5)
  
  q7_answer = "d"
  q7_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q7_response != q7_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was " + q7_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q7_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  s_print(Magenta + "Question 8")
  time.sleep(1)
  s_print(Magenta + "A snowboarder sitting at the top of a hill has what type of energy?")
  time.sleep(0.5)
  s_print(Cyan +" (a) Sound energy\n (b) Kinetic energy\n (c) Potential energy\n (d) Electric energy")
  time.sleep(0.5)
  s_print("")
  time.sleep(1.5)
  
  q8_answer = "c"
  q8_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q8_response != q8_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was " + q8_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q8_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  s_print(Magenta + "Question 9")
  time.sleep(1)
  s_print(Magenta + "A fire is being used to warm you up. What form of energy is being used?")
  time.sleep(0.5)
  s_print(Cyan +" (a) Potential energy\n (b) Thermal energy\n (c) Light energy\n (d) Electric energy")
  time.sleep(0.5)
  s_print("")
  time.sleep(1.5)
  
  q9_answer = "b"
  q9_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q9_response != q9_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was " + q9_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q9_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  s_print(Magenta + "Question 10")
  time.sleep(1)
  s_print(Magenta + "Which of the following is not a form of energy?")
  time.sleep(0.5)
  s_print(Cyan +" (a) Nuclear energy\n (b) Potassium energy\n (c) Thermal energy\n (d) Randiant energy")
  time.sleep(0.5)
  s_print("")
  time.sleep(1.5)
  
  q10_answer = "b"
  q10_response = typingInput(Green + "Answer: " + Green)
  s_print("")
  
  if (q10_response != q10_answer):
    time.sleep(1)
    s_print("Sorry, that was incorrect!")
    time.sleep(0.5)
    s_print("The correct answer was " + q10_answer)
    time.sleep(0.5)
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  else:
    time.sleep(1)
    s_print("Welldone! " + q10_answer + " is correct!")
    time.sleep(0.5)
    score = score + 10
    s_print("Your current score is " + str(score) + " out of 100")
    time.sleep(0.5)
    s_print("")
    time.sleep(1.5)

  s_print(Red + "Congratulations on completing this quiz!")
  s_print(Red + "Your final score is " + str(score) + " out of 100")
  
  loop = False
loop = False
