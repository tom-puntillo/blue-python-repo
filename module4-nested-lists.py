cells = [['A1', 'A2', 'A3'], ['B1', 'B2','B3']]
print(cells[0])
print(cells[0][0])
print(cells[0][1])
print(cells[1][2])

for x in cells:
    print('Element: ', x)
    
for x in cells:
    for y in x:
        print('Element: ', y)
        
tables = [['A1', 'A2', 'A3'], ['B1', 'B2','B3']]
for row in tables:
    for cells in row:
        print('Element: ', cells)
        
        
tables = [['A1', 'A2', 'A3'], ['B1', 'B2','B3']]
for row in tables:
    for cells in row:
        print(cells, '', end = '')
    print()
    
table = [[i for i in range(1,6)] for j in range(4)]
print(table)