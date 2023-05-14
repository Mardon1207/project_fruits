from csv import reader
def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    f=open('fruits.csv')
    r=reader(f,delimiter=',') 
    m=100000
    for i in r:
        if i[1]!='price' and m>float(i[1]):
            m=float(i[1])
    return int(m)
data=str()
print(get_cheapest_fruit_id(data))
    
