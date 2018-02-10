import random
import matplotlib.pyplot as plt


max_group_size = 100
trials = 100
share_count = 0
results_x = []
results_y = []

for group_size in range(max_group_size):
    print(group_size)
    share_count = 0
    for trial in range(trials):
        birthdays = []
        for i in range(group_size):
            birthday = random.randrange(365)
            birthdays.append(birthday)

        collision = False
        for birthday in birthdays:
            if birthdays.count(birthday) > 1:
                collision = True

        if collision == True:
            share_count = share_count + 1

    share_probability = share_count / float(trials)
    results_x.append(group_size)
    results_y.append(share_probability)

plt.plot(results_x, results_y)
plt.title("Probability of shared birthday day in a group")
plt.xlabel("Group Size")
plt.ylabel("Probability")
plt.savefig("birthday_problem_monte-carlo.svg")