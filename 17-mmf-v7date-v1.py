import pandas
import random
from datetime import date

###  FUNCTIONS GO HERE  ###

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

# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

  # ticket is $7.50 for users under 16
  if var_age < 16:
    price = 7.5

  # ticket is $10.50 for users bewteen 16 and 64
  elif var_age < 65:
    price = 10.5

  else:
    price = 6.5

  return price

# checks that users enter a valid response (eg. yes / no) based on a list of options
def string_checker(question, num_letters, valid_responses):

  error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

  if num_letters == 1:
    short_version = 1
  else:
    short_version = 2
  
  while True:
    response = input(question).lower()

    for item in valid_responses:
      if response == item[:short_version] or response == item:
        return item

    print(error)

# currency fortmatting function
def currency(x):
  return "${:.2f}".format(x)


###  MAIN ROUNTINE STARTS HERE  ###

# set maximum number of tickets below
MAX_TICKETS = 5
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# list to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
  "Name": all_names,
  "Ticket Price": all_ticket_costs,
  "Surcharge": all_surcharge
}

# Title and today's date
today = date.today()
print("---- Mini Movie Fundraiser Ticket Data ({}) ----".format(today))
print()

# asks user if they want to see the instructions
want_instructions = string_checker("Do you want to read the instructions (y/n)? ",1 , yes_no_list)

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

  # calculate ticket cost
  ticket_cost = calc_ticket_price(age)

  # get payment method
  pay_method = string_checker("Choose a payment method (cash/credit): ", 2, payment_list)

  if pay_method == "cash":
    surcharge = 0
  else:
    # calculates 5% surcharge if users are paying credit 
    surcharge = ticket_cost * 0.05

  tickets_sold += 1

  # add ticket name , cost and surcharge to lists
  all_names.append(name)
  all_ticket_costs.append(ticket_cost)
  all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# calculate profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# currency formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
  mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner in name list
win_index = all_names.index(winner_name)

# look up total amount won (ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

print("---- Ticket Data ----\n")

# output table ticket data
mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)

print("\n---- Ticket Cost / Profit ----\n")

# output total ticket sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))

print()
print("----- Raffle Winner -----")
print("Congratulations {}. You have won {} ie: your ticket is free!".format(
  winner_name, total_won))

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
  print("congratulations you have sold all the tickets")
else:
  print("you have sold {} ticket/s. there is {} ticket/s left.".format(tickets_sold,   MAX_TICKETS - tickets_sold))