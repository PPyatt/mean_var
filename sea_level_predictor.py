import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    fileN = 'epa-sea-level.csv'
    df = pd.read_csv(fileN)

    # Create scatter plot

    fig, ax = plt.subplots()
    #plt.plot(df['Year'],df['CSIRO Adjusted Sea Level'],linewidth=0,marker='s',markersize=1)
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linearResult = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])

    plt.plot(range(1880,2051), linearResult.intercept + linearResult.slope * range(1880,2051), 'r')#,label='Fitted line')

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]

    linearResult2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000,2051), linearResult2.intercept + linearResult2.slope * range(2000,2051), 'c')#,, label='Fitted line 2')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    #plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

#draw_plot()
