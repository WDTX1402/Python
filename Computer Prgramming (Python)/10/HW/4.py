def print_table(table):
    if not table:
        print("Table is empty")
        return

    column_width = []
    for col in range(len(table[0])):
        max_width = 0
        for row in table:
            cell_width = len(str(row[col]))
            if cell_width > max_width:
                max_width = cell_width
        column_width.append(max_width)


    for i, header in enumerate(table[0]):
        print(header.ljust(column_width[i]), end=" ")
    print()
    for row in table[1:]:
        for i, cell in enumerate(row):
            print(str(cell).ljust(column_width[i]), end=" ")
        print()

table_data1 = [['x', 'y'], [0, 0], [10, 10], [200, 200]]
print_table(table_data1)
print()
table_data2 = [['ID', 'Name', 'Surname'], ['001', 'John', 'Cena'], ['002', 'Vladimir', 'Zelensky'], ['003', 'Joe', 'Mama']]
print_table(table_data2)