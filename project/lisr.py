a=[1,"s",2,3,4,"gt","we"]
print(a[5])
print(a[2:5])
print(a[:7])
print(a[5:])

#manupulation of list
data = ["aman",11,"shivu",23,"sonu",56,"mukesh",32]
print(data)
#update sonu age 23
data[5]=23
print(data)
# another method
data[0:2]=("Aman Thakur",22)
print(data)
new =data +["rahul",22] # add new data to list
print(new)
del(data[1])# delete  method
print(data)

# copy of list
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)