from math import sqrt
import matplotlib.pyplot as plt
import time
import numpy as np

# function to calculate if a number is prime or not
def Prime(number, itr):
    if itr == 1: return True
    if number % itr == 0: return False
    if Prime(number, itr-1) == False: return False

    return True

# initiate counting variables
prime = 0
non_prime = 0

# start a timer to calculate the time taken to run the program
start_time = time.perf_counter()
for i in range(1, 1000000):
    num = i
    itr = int(sqrt(num)+1) # number always has to be at least one
    
    # conditional to check prime or not
    if Prime(num,itr) == True:
        prime = prime + 1
    else:
        non_prime = non_prime + 1

# calculate time elapsed
end_time = time.perf_counter()
elapsed =  end_time - start_time

print("Prime numbers: ", prime)
print("Non prime numbers: ", non_prime)
print("Calculated in", elapsed, "secs")  
  
# plot the data in a bar graph
plt.bar("Prime", prime)
plt.bar("Non prime", non_prime)
plt.show()

# plot the data as a pie chart
pie = np.array([prime, non_prime])
labels = ["Primes", "Non Primes"]

plt.pie(pie, labels = labels)
plt.show()