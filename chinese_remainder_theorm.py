print("Enter the number of congruences: ")
congruences = int(input())

# x = a mod m WHERE = is the congruence symbol

a = []
m = []

print("x = a mod m WHERE = is the congruence symbol")

for i in range(congruences):
	print("Enter 'a <space> m' for the " + str(i + 1) + " congruence")
	# Get user nput
	temp = input()
	# Split it on spaces
	a_temp, m_temp = temp.split(' ')
	# Convert to integers
	a_temp = int(a_temp)
	m_temp = int(m_temp)
	# Add to respective lists
	a.append(a_temp)
	m.append(m_temp)

# Find n such that n = m1 * m2 * ...
n = 1

for i in m:
	n *= i

# Caluclate delta such that delta_i = n / m_i
delta = []

for i in m:
	delta.append(n/i)

# Find b_i such that delta * bi is congruent to 1 mod m_i
b = []

for i in range(len(m)):
	b_temp = 1
	while True:
		# delta * bi is congruent to 1 mod m_i is equivelent to
		# m_i | (delta_i * b_i) - 1
		multiplier = ((delta[i] * b_temp) - 1) / m[i]
		if multiplier.is_integer():
			b.append(b_temp)
			break
		else:
			b_temp += 1

# x = ((delta_1 * b_1 * a_1) + (delta_2 * b_2 * a_2) + ...) mod n
x = 0
for i in range(len(m)):
	x += delta[i] * b[i] * a[i]
x = int(x) % n

print(str(x))
