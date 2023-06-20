import pandas
import random
from datetime import date

# dictionaires to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_cost = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
  "Name": all_names,
  "Ticket Price": all_ticket_cost,
  "Surcharge": surcharge
}

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

# set index at the end before printing
mini_movie_frame = mini_movie_frame.set_index('Name')

# Get current date for heading and filename 
# Get today's date
today = date.today()

# Get the day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Change frame to a string so it can be exported to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create strings for printing...
ticket_cost_heading = "\n---- Ticket Cost / Profit ----\n"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit: ${:.2f}".format(profit)

"""
# This is for the base project
# output number of tickets sold
if tickets_sold == MAX_TICKETS:
  sales_status = "congratulations you have sold all the tickets"
else:
  sale_status = "you have sold {} ticket/s. there is {} ticket/s left.".format(tickets_sold,   MAX_TICKETS - tickets_sold)
"""

sales_status = "\n**** All tickets has been sold ****"

winner_heading = "\n----- Raffle Winner -----"
winner_text = "The winner of the raffle is {}. They have won ${} ie: your ticket is free!".format(winner_name, total_won)

# List holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, sales_status, winner_heading, winner_text]

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