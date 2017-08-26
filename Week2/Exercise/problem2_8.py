#%%
def problem2_8(temp_list):
    high_temp = temp_list[0]
    low_temp = temp_list[0]
    tot_temp = 0
    for tem in temp_list:
        if high_temp < tem:
            high_temp = tem
        if low_temp > tem:
            low_temp = tem
        tot_temp = tot_temp + tem
    print("Average:", tot_temp / len(temp_list))
    print("High:", high_temp)
    print("Low:", low_temp)

