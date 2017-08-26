#%%
def problem1_3(n):
    my_sum = 0
    for ct in range(n, 0, -1):
        my_sum = my_sum + ct
    print(my_sum)
