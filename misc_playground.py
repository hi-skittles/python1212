# def join_loop(table1, table2, join_condition):
#     """Joining of two tables"""
#     # empty result list
#     res = []
#
#     # table1 loop
#     for row1 in table1:
#         # table2 loop
#         for row2 in table2:
#             # filter callback
#             if join_condition(row1, row2, 0):
#                 res.append(row1 + row2)
#     res = order_callback(res)
#     return res
#
#
# def join_condition_callback(row1, row2, condition=any):
#     """This is an example for simple join callback, which can be used as a filter."""
#     return row1[condition] == row2[condition]
#
#
# def order_callback(raw):
#     """Sorting a resulting table."""
#     return sorted(raw)
#
#
# # sample tables
# table1 = [('cat', 'tom'), ('mice', 'jerry'), (3, 'Charlie')]
# table2 = [('cat', 'mice'), ('mice', 'cheese'), (4, 40)]
#
# result = join_loop(table1, table2, join_condition_callback)
#
# print(result)


<<<<<<< HEAD
student_id = [80013, 80014, 80031, 80031]
[str(x)[-3:] for x in student_id ]
=======
def join_condition_callback(row1, row2, condition=any):
    """This is an example for simple join callback, which can be used as a filter."""
    return row1[condition] == row2[condition]


def order_callback(raw):
    """Sorting a resulting table."""
    return sorted(raw)


# sample tables
table1 = [('cat', 'tom'), ('mice', 'jerry'), (3, 'Charlie')]
table2 = [('cat', 'mice'), ('mice', 'cheese'), (4, 40)]

result = join_loop(table1, table2, join_condition_callback)

print(result)

>>>>>>> f69e907f4a91692300cd41a6de3f2d16236c8921
