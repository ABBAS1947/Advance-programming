# Create a tuple with values
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# Access the value at index -3
print(f"Value at index -3: {year[-3]}")

# Reverse the tuple and print both
reversed_year = tuple(reversed(year))
print(f"\nOriginal tuple: {year}")
print(f"Reversed tuple: {reversed_year}")

# Count number of times 2009 is in the tuple
count_2009 = year.count(2009)
print(f"\nNumber of times 2009 appears: {count_2009}")

# Get the index value of 2018
index_2018 = year.index(2018)
print(f"Index of 2018: {index_2018}")

# Find length of given tuple
length = len(year)
print(f"Length of tuple: {length}")