import numpy as np
import matplotlib.pyplot as plt

# Creating sample dataset for the dogs
# 500 - greyhounds
# 500 - labs
greyhounds = 500
labs = 500

# Every dog is different. So we will add + or - 4 randomly to the
# average dog height.
# The below code will create a list with 500 items with random
# dog height in inches
avg_grey_height = 28 + 4 * np.random.randn(greyhounds)
avg_lab_height = 24 + 4 * np.random.randn(labs)

# Uncomment the below line to visualize the newly created list
#print(avg_grey_height)
#print(avg_lab_height)

# histogram
plt.hist([avg_grey_height, avg_lab_height], stacked=True, color=['r', 'b']);
plt.show()