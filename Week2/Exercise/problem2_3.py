#%%
newEngland = ["Maine", "New Hampshire", "Vermont", "Rhode Island",
              "Massachusetts", "Connecticut"]


def problem2_3(ne):
    num_states = len(ne)
    for i in range(0, num_states):
        sumlet = 0
        for let in ne[i]:
            sumlet = sumlet + 1
        print(ne[i], "has", sumlet, "letters.")
