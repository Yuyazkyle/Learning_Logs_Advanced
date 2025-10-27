from plotly.graph_objs import Bar, Layout
from  plotly import offline
from rich import print
from .die import Die

# Rolling just one dice
def plot():
    # Time to plot the bar chart
    x_values = list(die.sides)
    y_values = list(frequencies)

    data = [Bar(x=x_values, y=y_values)]
    xaxis_config = {'title': f'No of sides'}
    yaxis_config = {'title': f'No of times appeared'}
    m_layout = Layout(title=f"Result of rolling a D{die.num_sides} dice, {num_rolls} times",
                    xaxis=xaxis_config, yaxis=yaxis_config)

    offline.plot({'data':data, 'layout':m_layout}, filename='templates/reports/one_die.html')

die = Die(8)
num_rolls = 2000

# Time to roll the dice
result = []
for i in range(num_rolls):
    rollz = die.roll()
    result.append(rollz)

print(f"The result for rolling a D{die.num_sides} dice {num_rolls} times\n {result}")
print('\n\t [u] In summary[/u],')
# Time to calculate for their frequencies, ie No of times appeared
frequencies = []
total = 0
for i in die.sides:
    frequency = result.count(i)

    if frequency == 1:
        print(f"Side {i} appeared once")
    elif frequency == 0:
        print(f"Side{i} didn't appear at all")
    else:
        print(f"Side {i} appeared {frequency} times")
    total += frequency
    frequencies.append(frequency)
print(f'TOTAL = {total}')

#plot()