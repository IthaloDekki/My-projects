def stockmarket(stock):
    dic = {}
    for i in len(stock):
        if not stock[i][0] in dic:
            dic[i][0] = float[stock[i][1]] * int[stock[i][2]]
        
        else:
            dic[stock[i][0]] += float[stock[i][1]] * int[stock[i][2]]
            
    return dic

stock = [('24-Out-2020', 43.50, 25, 'CAT'),
('25-Out-2020', 42.80, 50, 'ITU'),
('26-Out-2020', 42.10, 75, 'ITU'),
('27-Out-2020', 37.58, 100, 'GM')]
print(stockmarket(stock))
