#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    b1_str = input("Enter length of side one: ")
    b2_str = input("Enter length of side two: ")
    h_str = input("Enter length of side three: ")
    if b1_str and b2_str and h_str:
        if b1_str.isdigit() and b2_str.isdigit() and h_str.isdigit():
            b1 = float(b1_str)
            b2 = float(b2_str)
            h = float(h_str)
            s = .5 * (b1 + b2 + h)
            area = (s * (s - b1) * (s - b2) * (s - h)) ** .5
            print("Area of a triangle with sides", b1, b2, h, "is", area)
        else:
            print("This is not a number")
