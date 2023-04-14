"""
There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required
for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each
integer represents a customer, and its value is the amount of time they
require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Examples:
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12

Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list)
proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid,
as specified above.

P.S. The situation in this kata can be likened to the
more-computer-science-related idea of a thread pool,
with relation to running multiple processes at the same
time: https://en.wikipedia.org/wiki/Thread_pool



Interesting challenge to simulate a supermarket queue
I needed some help to solve it because I could not think about a way
to distribute the customers.


"""
def queue_time(customers, n):
    # if theres no tills, no waiting time. Close the supermarket!
    if n == 0:
        return 0
    # if there are no customers, also no waiting time
    elif len(customers) == 0:
        return 0
    # if there's just one till, we need to sume the time of every customer
    elif n == 1:
        return sum(customers)
    # if the number of tills is bigger than the number of customers
    # the waiting time will be equal to the slowest customer in line
    elif n >= len(customers):
        return max(customers)
    # the most difficult one is when you have more customers than line
    # First, create a list of zeros that will simulate each till
    # second, every time a new customer is send to a till, we need to
    # sort the tills list again so the next customer goes to the fastest till
    # and we add the waiting time of this customer to the fastest till
    # at the end, you return
    else:
        tills = [0] * n
        for c in customers:
            tills[0] += c
            tills = sorted(tills)
        return max(tills)
