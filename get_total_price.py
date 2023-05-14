from csv import reader
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    f=open('fruits.csv')
    r=reader(f,delimiter=',')
    s=0
    for i in r:
        if i[1]!='price':
            s+=float(i[1])
    return s
data=str()
print(get_total_price(data))

    