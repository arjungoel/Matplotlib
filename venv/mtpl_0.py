from matplotlib import pyplot as plt

dev_x = ['Spain', 'Italy', 'Iran', 'USA', 'India']

dev_y = [200, 1500, 120, 100, 5]

plt.plot(dev_x, dev_y)

# labeling the x and y co-ordinates
plt.xlabel('Countries')
plt.ylabel('Median Deaths (Years)')

# titling the graph
plt.title('Median Deaths (Years) by Ages in Countries')

# to display the graph
plt.show()