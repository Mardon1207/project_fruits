from csv import reader
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f=open('fruits.csv')
    r=reader(f,delimiter=',')
    lis=[]
    for i in r:
        if i[0]!="`name":
            lis.append(i[0])
    return lis
data=str()
print(get_frutis_name(data))

    