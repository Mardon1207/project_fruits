from csv import reader
def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    # your code here
    f=open('fruits.csv')
    r=reader(f,delimiter=',')
    s=''
    m=0
    for i in r:
        if i[1]!='price' and m<float(i[1]):
            m=float(i[1])
            s=i[0]
    return  s
data=str()
print(get_expensive_fruit(data))


