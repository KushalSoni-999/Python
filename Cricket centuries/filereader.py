# import pandas as pd
# from tabulate import tabulate
# import matplotlib.pyplot as plt 
# import numpy as np
# import mplcursors
# import matplotlib.dates as mdates


# df = pd.read_csv("final.csv")

# # Define the categories based on runs
# df['Category'] = pd.cut(
#     df['runs'], 
#     bins=[0, 50, 100, 200, float('inf')], 
#     labels=['', 'half centuries', 'centuries', 'double centuries'],
#     right=False
# )

# # Filter the df based on the categories
# half_centuries = df[df['Category'] == 'half centuries']
# centuries = df[df['Category'] == 'centuries']
# double_centuries = df[df['Category'] == 'double centuries']

# # Display the categorized df
# half_centuries_output = half_centuries[['runs', 'opponent', 'match', 'date']]
# centuries_output = centuries[['runs', 'opponent', 'match', 'date']]
# double_centuries_output = double_centuries[['runs', 'opponent', 'match', 'date']]
# total_half_centuries = len(half_centuries_output)
# total_centuries = len(centuries_output)
# total_double_centuries = len(double_centuries_output)


# odi_performance = df[df['match'] == 'ODI']
# test_performance = df[df['match'] == 'Test']
# t20_performance = df[df['match'] == 'T20']

# odi_performance_output = odi_performance[['runs', 'opponent', 'ground', 'date']]
# test_performance_output = test_performance[['runs', 'opponent', 'ground', 'date']]
# t20_performance_output = t20_performance[['runs', 'opponent', 'ground', 'date']]

# # Convert 'date' column to datetime format
# df['date'] = pd.to_datetime(df['date'], format='%d%b%Y')

# # Plotting
# fig, ax = plt.subplots(figsize=(14, 8))

# # Plot half centuries
# scatter_half = ax.scatter(half_centuries['date'], half_centuries['runs'], color='blue', label='Half Centuries')

# # Plot centuries
# scatter_centuries = ax.scatter(centuries['date'], centuries['runs'], color='green', label='Centuries')

# # Plot double centuries
# scatter_double = ax.scatter(double_centuries['date'], double_centuries['runs'], color='red', label='Double Centuries')

# # Format the x-axis as date
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# ax.xaxis.set_major_locator(mdates.DayLocator(interval=30))  # Adjust the interval as needed

# # Rotate date labels
# plt.gcf().autofmt_xdate()

# # Set x-axis limits to the range of the data
# ax.set_xlim([df['date'].min(), df['date'].max()])

# # Labels and title
# ax.set_xlabel('Date')
# ax.set_ylabel('Runs')
# ax.set_title('Runs Scored Over Time')
# ax.legend()
# ax.grid(True)

# # Add interactive cursors
# cursor = mplcursors.cursor(hover=True)

# @cursor.connect("add")
# def on_add(sel):
#     date = mdates.num2date(sel.target[0]).strftime('%Y-%m-%d')
#     runs = sel.target[1]
#     sel.annotation.set_text(f'({date}, {runs})')
#     sel.annotation.get_bbox_patch().set(fc="white", alpha=0.8)

# # Show plot
# plt.show()




# # print(tabulate(odi_performance_output , headers="keys", tablefmt="pretty"))
# # print(tabulate(test_performance_output , headers="keys", tablefmt="pretty"))
# # print(tabulate(t20_performance_output, headers="keys", tablefmt="pretty"))



import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import matplotlib.dates as mdates

# Load the CSV file
data = pd.read_csv("final.csv")

# Convert 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'], format='%d%b%Y')

# Define the categories based on runs
data['Category'] = pd.cut(
    data['runs'], 
    bins=[0, 50, 100, 200, float('inf')], 
    labels=['', 'half centuries', 'centuries', 'double centuries'],
    right=False
)

# Filter the data based on the categories
half_centuries = data[data['Category'] == 'half centuries']
centuries = data[data['Category'] == 'centuries']
double_centuries = data[data['Category'] == 'double centuries']
rest = data[data['Category'] == '']

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Plot half centuries
scatter_half = ax.scatter(half_centuries['date'], half_centuries['runs'], color='blue', label='Half Centuries')

# #Plot rest
# scatter_rest = ax.scatter(rest['date'], rest['runs'], color='black', label='Rest')

# Plot centuries
scatter_centuries = ax.scatter(centuries['date'], centuries['runs'], color='green', label='Centuries')

# Plot double centuries
scatter_double = ax.scatter(double_centuries['date'], double_centuries['runs'], color='red', label='Double Centuries')

# Format the x-axis as date
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.AutoDateLocator())

# Rotate date labels
plt.gcf().autofmt_xdate()

# Set x-axis limits to the range of the data
ax.set_xlim([data['date'].min(), data['date'].max()])

# Labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Runs')
ax.set_title('Runs Scored Over Time')
ax.legend()
ax.grid(True)

# Add interactive cursors
cursor = mplcursors.cursor(hover=True)

@cursor.connect("add")
def on_add(sel):
    date = mdates.num2date(sel.target[0]).strftime('%Y-%m-%d')
    runs = sel.target[1]
    sel.annotation.set_text(f'({date}, {runs})')
    sel.annotation.get_bbox_patch().set(fc="white", alpha=0.8)

# Show plot
plt.show()



