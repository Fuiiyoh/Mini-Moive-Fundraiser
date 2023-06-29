import pandas
import random
from datetime import date

###  FUNCTIONS GO HERE  ###


# shows instructions
def show_instructions():
  print('''\n
------------------------ Instructions -------------------------

For each ticket enter...
- The person's name (can't be blank)
- Age (between 12 to 120)
- Payment method (cash or credit)

When you have entered all the users, press 'xxx' to quit.

The program will display the ticket details including the cost
of each ticket, the total cost and the total profit.

This information will automatically be written to a text file.

---------------------------------------------------------------
  ''')


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


# calculate the ticket price based on the age
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

  error = "Please choose {} or {}".format(valid_responses[0],
                                          valid_responses[1])

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

# asks user if they want to see the instructions
want_instructions = string_checker(
  "Do you want to read the instructions (y/n)? ", 1, yes_no_list)

if want_instructions == "yes":
  show_instructions()

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
  name = not_blank("please enter your name (or 'xxx' to quit): ")

  if name == "xxx" and len(all_names) > 0:
    break
  elif name == "xxx":
    print("You must sell at least ONE ticket before quitting")
    continue

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
  pay_method = string_checker("Choose a payment method (cash/credit): ", 2,
                              payment_list)

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

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame[
  'Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# calculate profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose a winner and look at total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# currency formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
  mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# set index at the end before printing
mini_movie_frame = mini_movie_frame.set_index('Name')

# Get current date for heading and filename
# Get today's date
today = date.today()

# Get the day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "\n---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(
  day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Change frame to a string so it can be exported to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create strings for printing...
ticket_cost_heading = "\n---- Ticket Cost / Profit ----\n"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit: ${:.2f}".format(profit)

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
  sales_status = "\n**** you have sold all the tickets. ****"
else:
  sales_status = "\n**** you have sold {} ticket/s. there is {} ticket/s left. ****".format(
    tickets_sold, MAX_TICKETS - tickets_sold)

winner_heading = "\n----- Raffle Winner -----"
winner_text = "The winner of the raffle is {}. They have won ${:.2f} ie: your ticket is free!".format(
  winner_name, total_won)

# List holding content to print / write to file
to_write = [
  heading, mini_movie_string, ticket_cost_heading, total_ticket_sales,
  total_profit, sales_status, winner_heading, winner_text
]

# print output
for item in to_write:
  print(item)

# write output to file
# create file to hold data
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
  text_file.write(item)
  text_file.write("\n")

# close file
text_file.close()
