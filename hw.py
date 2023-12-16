names = ["Melat", "John", "Yeabnat", "Sisay", "Tikdem"]

# Using a loop
reversed_names1 = []
for i in range(len(names)-1, -1, -1):
  reversed_names1.append(names[i])

# Using reversed() function
reversed_names2 = list(reversed(names))

# Using slicing
reversed_names3 = names[::-1]

print("Reversed names using loop:", reversed_names1)
print("Reversed names using reversed():", reversed_names2)
print("Reversed names using slicing:", reversed_names3)
end loop
