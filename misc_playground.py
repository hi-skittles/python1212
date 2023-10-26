"""
    Joining of two tables
"""
def join_loop(table1, table2, join_condition):
    # empty result list
    res = []

    # table1 loop
    for row1 in table1:
        # table2 loop
        for row2 in table2:
            # filter callback
            if join_condition(row1, row2, 0):
                res.append(row1 + row2)
    res = order_callback(res)
    return res


"""
    This is an example for simple join callback, which can be used as a filter.
"""
def join_condition_callback(row1, row2, condition=any):
    return row1[condition] == row2[condition]


"""
    Sorting a resulting table.
"""
def order_callback(raw):
    return sorted(raw)


# sample tables
table1 = [('cat', 'tom'), ('mice', 'jerry'), (3, 'Charlie')]
table2 = [('cat', 'mice'), ('mice', 'cheese'), (4, 40)]

result = join_loop(table1, table2, join_condition_callback)

print(result)
