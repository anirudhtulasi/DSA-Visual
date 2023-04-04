import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the Bubble Sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Swap adjacent elements if they are in the wrong order
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr, i, j

# Generate a random unsorted array
arr = random.sample(range(1, 101), 50)

# Create the figure and axes for the initial animation
fig1, ax1 = plt.subplots()
ax1.set_title('Unsorted Array')
ax1.set_xlabel('Index')
ax1.set_ylabel('Value')
ax1.set_facecolor('black')

# Initialize the bar plot with the unsorted array
bar_plot1 = ax1.bar(range(len(arr)), arr, align='edge', color='blue')

# Define the update function for the initial animation
def update_initial(data):
    # Update the heights and colors of the bar plot with the current state of the array
    arr = data
    for k, bar in enumerate(bar_plot1):
        bar.set_height(arr[k])
        bar.set_color('blue')
    ax1.set_facecolor('black')
    return bar_plot1

# Create the initial animation
ani1 = animation.FuncAnimation(fig1, update_initial, frames=[arr], blit=True, repeat=False)

# Create the figure and axes for the sorting animation
fig2, ax2 = plt.subplots()
ax2.set_title('Bubble Sort')
ax2.set_xlabel('Index')
ax2.set_ylabel('Value')
ax2.set_facecolor('black')

# Initialize the bar plot with the unsorted array
bar_plot2 = ax2.bar(range(len(arr)), arr, align='edge', color='blue')

# Define the update function for the sorting animation
def update_sort(data):
    # Update the heights and colors of the bar plot with the current state of the array
    arr, i, j = data
    for k, bar in enumerate(bar_plot2):
        bar.set_height(arr[k])
        if k == j or k == j+1:
            bar.set_color('red')
        else:
            bar.set_color('blue')
    ax2.set_title(f'Bubble Sort (Pass {i+1}, Comparing {j+1} and {j+2})')
    ax2.set_facecolor('black')
    return bar_plot2

# Create the sorting animation
ani2 = animation.FuncAnimation(fig2, update_sort, frames=bubble_sort(arr), blit=True, repeat=False, interval=10)

# Combine the two animations
ani = animation.FuncAnimation(fig1, update_initial, frames=[arr], blit=True, repeat=False)
ani.event_source.stop()
ani.event_source.interval = 10
ani.event_source.frames = [ani1.new_frame_seq(), ani2.new_frame_seq()]

# Show the animation
plt.show()

# Print the initial unsorted array and the sorted array after completion
print(f'Initial unsorted array: {arr}')
sorted_arr = list(bubble_sort(arr))[-1][0]
print(f'Sorted array: {sorted_arr}')
