# functions go here

# checks if the users response is blank or not
def not_blank(question):

  while True:
    response = input(question)

    # if response is blank, ouput error
    if response == "":
      print("Sorry this cannot be blank. Please try again.")
      
    else:
      return response

# main routine goes here
while True:
  name = not_blank("Enter your name (or 'xxx' to quit) ")

  if name == "xxx":
    break

print("we are done")