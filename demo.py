from geohash import encode, decode

x = encode(9.856582084367748, 8.900562599301338, 5)
print(x)

y = decode(x)
print(y)