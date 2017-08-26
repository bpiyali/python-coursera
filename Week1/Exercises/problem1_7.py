#%%
def problem1_7():
    b1_str = input("Enter the length of one of the base: ")
    b2_str = input("Enter the length of the other base: ")
    h_str = input("Enter the height: ")
    if b1_str and b2_str and h_str:
        if b1_str.isdigit() and b2_str.isdigit() and h_str.isdigit():
            b1 = float(b1_str)
            b2 = float(b2_str)
            h = float(h_str)
            if b1 != b2:
                area = (1/2)*(b1+b2)*h
                print("The area of a trapezoid with bases", b1, "and", b2, "and height", h, "is", area)
        else:
            print("This is not a number")
