a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 76     # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")

# Unpacking tuples never causes an error because they are immutable
data_list = [12, 13, 14]
# data_list.append(15)  # This caused error because it exceeded the variables
p, q, r = data_list
print(p)
print(q)
print(r)
