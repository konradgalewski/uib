# G: generator matrix, a matrix
# u: information word/message, a vector
# x = G*u: code word that you send, a vector
# y: what you receive, which is a damaged representation of x

# Decoding: the process of recovering u from y and G
# We need to solve for u in this system.
G * u = y

u = inv(G) * y


# Least squares: Find the "best" solution to the system.
G * u = y

# In our case
x = [u[0], u[1], u[0]+u[1]]
G = [[1, 0], [0, 1], [1, 1]]
u = [1, 2]
x = G*u

# Create a generator matrix, G. Choosing each element of G randomly
# should be fine. G is of size n times k.

# Choose an information word u arbitrarily. The information word
# (vector) is of length k.

# Use G to encode u, resulting in the code word x (vector) of length
# n.

# Simulate an erasure channel by removing some elements of x. Erasures
# are typically represented by an erasure vector. For example, [1, 0,
# 0, 0] means that the first element of x (here of length 4) was
# erased and the remaining elements were received correctly.

# To decode, setup the system of linear equations corresponding the
# rows of G and elements of x that were not erased. You now have
# system we need to solve. Apply lstsq to the system of equations to
# find a solution. Use the numpy implementation of lstsq.
