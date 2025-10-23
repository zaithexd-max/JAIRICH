questions = ("Do you love me?",
             "Are you a nigga?",
             "Are you colouredskin?",
             "Fuck you",
             "Nigga")
options = (("A.No","B.No","C.Nigger"),
           ("A.Yes","B.Yeah my boy","C.Good Boyyy"),
           ("A.Yeah","B.My n","C.My jit"),
           ("A.Fuck you","B.Sigma","C.real"),
           ("A.N","B.Nigger","C.Nigga"))
answers = ("C","B","C","A","B")
guesses = []
score = 0
question_num = 0
for question in questions:
  print("------------")
  print(question)
  for option in options[question_num]:
    print(option)
  guess = input("Enter (A,B,C,D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score +=1
    print("Correct")
  else:
    print("Incorrect")
    print(f"The Answer is {answers[question_num]}")
  question_num +=1
print(f"You got {score}/5")

