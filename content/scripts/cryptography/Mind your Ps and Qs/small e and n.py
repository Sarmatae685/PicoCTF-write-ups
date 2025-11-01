from Crypto.Util.number import inverse, long_to_bytes

c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573

phi = (p - 1)*(q - 1)

# d = e^(-1) mod phi  | d is within the range from 1 to phi-1
# i.e., the inverse(e, phi) method finds the modular inverse of (e mod phi)
# that is, a number such that (e*d) mod phi == 1
# implements the "Extended Euclidean Algorithm"
d = inverse(e, phi)

m = pow(c,d,n) #c**d mod n

print(long_to_bytes(m))
