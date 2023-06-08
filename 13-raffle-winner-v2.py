import pandas
import random

# currency fortmatting function
def currency(x):
  return "${:.2f}".format(x)

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
#mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# calculate profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# choose a winner from our name list
winner = random.choice(all_names)

# get position of winner in name list
# win_index = all_names.index(winner)
# look up total amount won (ticket price + surcharge)
#total_won = mini_movie_frame.at[win_index, 'Total']

# set index at the end

#print(mini_movie_frame)

# look up winner in panda and output their data

#print("Value of row (d)")
#print(mini_movie_frame.iloc[3])
#print(mini_movie_frame['Name'])

print(mini_movie_frame.loc[mini_movie_frame['Name'] == winner])

#test = mini_movie_frame._get_value(win_index, 'Name')
#print("test", test)