import pandas as pd

def compare(): 

    # Sample DataFrames for demonstration
    data1 = {'number': [1, 2, 3, 7], 'text': ['a', 'b', 'c', 'd'], 'money': [100, 200, 400, 500]}
    data2 = {'number': [1, 4, 3], 'text': ['a', 'd', 'c'], 'money': [100, 200, 700]}
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # differences = df1.compare(df2)
    # output = differences.to_string(index=False)

    print(df1)
    print(df2)

    # Assuming df1 and df2 are your DataFrames
    merged_diff = pd.merge(df1, df2, indicator=True, how='outer').loc[lambda x : x['_merge'] != 'both']
    print("Differences between the two DataFrames:")
    print(merged_diff)

    # print('df1') 
    # print(df1)
    # print('df2') 
    # print(df2) 
    # print('---------------') 
    # print(differences)
    # print(type(differences)) 
    # print(type(output)) 

# # Compare DataFrames for differences
# differences = df1.compare(df2)

# # Display the differences in a formatted way
# output = differences.to_string(index=False)

# print("Differences between the two DataFrames:")
# print(output)