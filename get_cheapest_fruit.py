from csv import reader
def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    f=open('fruits.csv')
    r=reader(f,delimiter=',')
    m=100000
    s=''
    for i in r:
        if i[1]!='price' and m>float(i[1]):
            m=float(i[1])
            s=i[0]
    return s
data=str
print(get_cheapest_fruit(data))