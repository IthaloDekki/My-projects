def stockmarket(stock):
    dic = {}
    for i in len(stock):
        if not stock[i][0] in dic:
            dic[i][0] = float[stock[i][1]] * int[stock[i][2]]
        
        else:
            dic[stock[i][0]] += float[stock[i][1]] * int[stock[i][2]]
            
    return dic