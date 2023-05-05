#  FUNCTIONS GO HERE  #

# checks if user entered yes/no to a question
def yes_no(question):

  while True:
    response = input(question).lower()
    
    if response  == "yes" or response  == "y":
      return "yes"

    elif response  == "no" or response  == "n":
      return "no"

    else:
      print("please answer yes/no")

# checks if users response is blank or not
def not_blank(question):

  while True:
    response = input(question)

    # if response is blank, ouput error
    if response == "":
      print("Sorry this cannot be blank. Please try again.")
      
    else:
      return response

# checks if user entered an integer to a given question
def num_check(question):
  while True:
    try:
      response = int(input(question))
      return response
      
    except ValueError:
      print("Please enter an integer.")

#  MAIN ROUNTINE STARTS HERE  #

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# asks user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
  print("Instructions")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
  name = not_blank("please enter your name (or 'xxx' to quit): ")

  if name == "xxx":
    break

  age = num_check("Age: ")

  if 12 <= age <= 120:
    pass
  elif age < 12:
    print("Sorry you are too young for this movie.")
    continue
  else:
    print("That looks like a typo, please try again.")
    continue

  tickets_sold += 1

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
  print("congratulations you have sold all the tickets")
else:
  print("you have sold {} ticket/s. there is {} ticket/s left.".format(tickets_sold,   MAX_TICKETS - tickets_sold))