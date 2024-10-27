import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'], s = 2)

    # Create first line of best fit
    fit1 = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    slope1 = fit1.slope
    intercept1 = fit1.intercept
    #x_fit1 = np.array([df['Year'].min(), 2050], dtype = float)
    x_fit1 = np.linspace(df['Year'].min(), 2050, 2051 - df['Year'].min())
    y_fit1 = x_fit1 * slope1 + intercept1
    
    ax.plot(x_fit1, y_fit1, 'r-')


    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    
    fit2 = linregress(x = df2000['Year'], y = df2000['CSIRO Adjusted Sea Level'])
    slope2 = fit2.slope
    intercept2 = fit2.intercept
    #x_fit2 = np.array([df2000['Year'].min(), 2050], dtype = float)
    x_fit2 = np.linspace(df2000['Year'].min(), 2050, 2051 - df2000['Year'].min())
    y_fit2 = x_fit2 * slope2 + intercept2
    
    ax.plot(x_fit2, y_fit2, 'g-')
    


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
