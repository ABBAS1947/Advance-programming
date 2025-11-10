
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# access the value at index -3 so it starts counting from the end
print(f"Value at index -3: {year[-3]}")

#using the reverse function
reversed_year = tuple(reversed(year))
print(f"\nOriginal tuple: {year}")
print(f"Reversed tuple: {reversed_year}")

# so here the count function is used
count_2009 = year.count(2009)
print(f"\nNumber of times 2009 appears: {count_2009}")

# index function is used to check the index of 2018
index_2018 = year.index(2018)
print(f"Index of 2018: {index_2018}")

# and lastly len function checks the length of the tuple
length = len(year)
print(f"Length of tuple: {length}")