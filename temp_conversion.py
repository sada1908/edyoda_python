def convert():
    ''' Following code is to convert Temp from one unit to other'''
    inp = input("Give your input in F or C :" ).upper()
    temp = float(input("Input he value : "))
    if inp == "F":
        res = (temp-32)*5/9
        print(f'Conersion of {temp} {inp} is {res}')
    elif inp == "C":
        res = (temp * 9/5) + 32
        print(f'Conersion of {temp} {inp} is {res}')
    else:
        print(f'Please provide proper inputs and run again')
    return temp , inp, res
    
if __name__ == "__main__":
    convert()
    