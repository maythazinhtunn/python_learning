nested_list=[[1,2,3],
            [4,5,6],
            [7,8,9]]
print("nested_list",nested_list)

for row,row_item in enumerate(nested_list):
    print("Row",row,"Value",row_item)
    for col,col_item in enumerate(row_item):
        print("Col",col,"Value",col_item)