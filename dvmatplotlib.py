#Data visualization with matplotlib
#using matplotlib.pyplot interface


#instructions
'''Import the matplotlib.pyplot API, using the conventional name plt.
Create Figure and Axes objects using the plt.subplots function.
Show the results, an empty set of axes, using the plt.show function.'''

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()



#instructions
'''Import the matplotlib.pyplot submodule as plt.
Create a Figure and an Axes object by calling plt.subplots.
Add data from the seattle_weather DataFrame by calling the Axes plot method.
Add data from the austin_weather DataFrame in a similar manner and call plt.show to show the results.'''

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Call the show function
plt.show()



#Customizing your plots

#instructions
'''Call ax.plot to plot "MLY-PRCP-NORMAL" against "MONTHS" in both DataFrames.
Pass the color key-word arguments to these commands to set the color of the Seattle data to blue ('b') and the Austin data to red ('r').
Pass the marker key-word arguments to these commands to set the Seattle data to circle markers ('o') and the Austin markers to triangles pointing downwards ('v').
Pass the linestyle key-word argument to use dashed lines for the data from both cities ('--').'''

# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color = "b", marker = "o", linestyle = "--")

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color = "r", marker = "v", linestyle = "--")

# Call show to display the resulting plot
plt.show()



#instructions
'''Use the set_xlabel method to add the label: "Time (months)".
Use the set_ylabel method to add the label: "Precipitation (inches)".
Use the set_title method to add the title: "Weather patterns in Austin and Seattle".'''

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()


#Smalll multiples

#instructions
'''Create a Figure and an array of subplots with 2 rows and 2 columns.
Addressing the top left Axes as index 0, 0, plot the Seattle precipitation.
In the top right (index 0,1), plot Seattle temperatures.
In the bottom left (1, 0) and bottom right (1, 1) plot Austin precipitations and temperatures.'''

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather["MONTH"],seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1,0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1,1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()



#instructions
'''Create a Figure with an array of two Axes objects that share their y-axis range.
Plot Seattle's "MLY-PRCP-NORMAL" in a solid blue line in the top Axes.
Add Seattle's "MLY-PRCP-25PCTL" and "MLY-PRCP-75PCTL" in dashed blue lines to the top Axes.
Plot Austin's "MLY-PRCP-NORMAL" in a solid red line in the bottom Axes and the "MLY-PRCP-25PCTL" and "MLY-PRCP-75PCTL" in dashed red lines.'''

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation data in the bottom axes
# Plot Seattle precipitation data in the top axes
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')
plt.show()



#PLotting time series data
#instructions
'''Import the pandas library as pd.
Read in the data from a CSV file called 'climate_change.csv' using pd.read_csv.
Use the parse_dates key-word argument to parse the "date" column as dates.
Use the index_col key-word argument to set the "date" column as the index.'''

# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates = ["date"] , index_col = "date")


#instructions
'''Add the data from climate_change to the plot: use the DataFrame index for the x value and the "relative_temp" column for the y values.
Set the x-axis label to 'Time'.
Set the y-axis label to 'Relative temperature (Celsius)'.
Show the figure.'''

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel("Relative temperature (Celsius)")

# Show the figure
plt.show()


#instructions
'''Use plt.subplots to create a Figure with one Axes called fig and ax, respectively.
Create a variable called seventies that includes all the data between "1970-01-01" and "1979-12-31".
Add the data from seventies to the plot: use the DataFrame index for the x value and the "co2" column for the y values.'''

import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()



#Plotting time series with different variables
#instructions
'''Use plt.subplots to create a Figure and Axes objects called fig and ax, respectively.
Plot the carbon dioxide variable in blue using the Axes plot method.
Use the Axes twinx method to create a twin Axes that shares the x-axis.
Plot the relative temperature variable in red on the twin Axes using its plot method.'''

import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"] , color='b')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"] , color='r')

plt.show()


#instructions
'''Define a function called plot_timeseries that takes as input an Axes object (axes), data (x,y), a string with the name of a color and strings for x- and y-axis labels.
Plot y as a function of in the color provided as the input color.
Set the x- and y-axis labels using the provided input xlabel and ylabel, setting the y-axis label color using color.
Set the y-axis tick parameters using the tick_params method of the Axes object, setting the colors key-word to color.'''

# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color= color )

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color= color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors= color)
  
  
  
#instructions
'''In the provided ax object, use the function plot_timeseries to plot the "co2" column in blue, with the x-axis label "Time (years)" and y-axis label "CO2 levels".
Use the ax.twinx method to add an Axes object to the figure that shares the x-axis with ax.
Use the function plot_timeseries to add the data in the "relative_temp" column in red to the twin Axes object, with the x-axis label "Time (years)" and y-axis label "Relative temperature (Celsius)".'''


fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax,climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax,climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative temperature (Celsius)")

plt.show()



#Annotating time series data
#instructions
'''Use the ax.plot method to plot the DataFrame index against the relative_temp column.
Use the annotate method to add the text '>1 degree' in the location (pd.Timestamp('2015-10-06'), 1).'''

fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change["relative_temp"])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate( ">1 degree", xy = (pd.Timestamp('2015-10-06'), 1))

plt.show()



#instructions
'''Use the plot_timeseries function to plot CO2 levels against time. Set xlabel to "Time (years)" ylabel to "CO2 levels" and color to 'blue'.
Create ax2, as a twin of the first Axes.
In ax2, plot temperature against time, setting the color ylabel to "Relative temp (Celsius)" and color to 'red'.
Annotate the data using the ax2.annotate method. Place the text ">1 degree" in x=pd.Timestamp('2008-10-06'), y=-0.2 pointing with a gray thin arrow to x=pd.Timestamp('2015-10-06'), y = 1.'''

fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time (years)', 'CO2 levels')

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax, climate_change.index, climate_change['relative_temp'], 'red', 'Time (years)', 'Relative temp (Celsius)')

# Annotate point with relative temperature >1 degree
ax2.annotate(">1 degree", xy = (pd.Timestamp('2015-10-06'), 1), 
xytext = (pd.Timestamp('2008-10-06'), -0.2),
arrowprops = {'arrowstyle': '->', 'color' : 'gray'})

plt.show()
