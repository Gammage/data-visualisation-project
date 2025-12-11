from die import Die
import plotly.express as px

# #create a die
# die = Die()
    
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# #analyse results
# frequencies = []
# #stops before last number, hence plus 1. exclusive to range
# poss_results = range(1,die.num_sides+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)
    
# print(frequencies)

#in the above, we create an object using the die class
#we then roll it 1000 times and append the results in results list

#we then analyse the results in frequencies, referencing the dice
#for each roll result, we count the frequency each time in a for loop
 #we append the frequency in the list frequencies. this calculates how many
 #times each roll landed between the given sided dice
 
#visualise the results in a histogram
# title = "Results of Rolling one D6 1000, times"
# labels = {'x':'result','y':'frequency of result',}
# fig = px.bar(x=poss_results,y=frequencies, title=title, labels=labels)
# fig.show()

#simple bar chart, but plotly is designed to be simple, represent the data  the way you want it to
#

##rolling two dice##
#rolling two dice results in a larger number and different distribution of results
#modifying our code to create two D6 diece to simulate the way we roll a pair of dice

#create two D6 dice 
die_1 = Die()
die_2 = Die()
    
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyse results
frequencies = []
#stops before last number, hence plus 1. exclusive to range
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling two D6 dice 1000 times"
labels = {'x':'result','y':'frequency of result',}
fig = px.bar(x=poss_results,y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

#poss results = range 2 as min value of rolling 2 dice and then we add the max value of dice in max_result
#code is similiar as before, the x axis displays the larger result pool

