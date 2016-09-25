import sys

show_steps = False
if "-s" in sys.argv:
	show_steps = True

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

if show_steps:
	print("\n----------------------------")
	print("Input\n")
	for i in range(len(m)):
		print("x = " + str(a[i]) + " mod " + str(m[i]))

if show_steps:
	print("\n----------------------------")
	print("Solve for As\n")
	for i in range(len(a)):
		print("a_" + str(i) + " = " + str(a[i]))

# Find n such that n = m1 * m2 * ...
n = 1

for i in m:
	n *= i

if show_steps:
	print("----------------------------")
	print("Solve for n")
	sys.stdout.write("\nn = ")
	for i in m:
		sys.stdout.write(str(i))
		if i != m[-1]:
			sys.stdout.write("*")
	sys.stdout.write(" = " + str(n) + "\n")

# Caluclate delta such that delta_i = n / m_i
delta = []

for i in m:
	delta.append(n/i)

if show_steps:
	print("----------------------------")
	print("Solve for Deltas\n")
	for i in range(len(m)):
		sys.stdout.write("d_" + str(i) + " = " + "n/n_" + str(i) + " = " + str(n) + "/" + str(m[i]) + " = " + str(delta[i]) + "\n")

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

if show_steps:
	print("----------------------------")
	print("Solve for Bs")
	for i in range(len(m)):
		print("\n" + "d_" + str(i) + "*b_" + str(i) + " = 1 mod " + str(m[i]))
		print(str(delta[i]) + "*b_" + str(i) + " = 1 mod " + str(m[i]))
		print(str(m[i]) + " | " + str(delta[i]) + "*b_" + str(i) + " - 1")
		print("b_" + str(i) + " = " + str(b[i]))
	

# x = ((delta_1 * b_1 * a_1) + (delta_2 * b_2 * a_2) + ...) mod n
x = 0
for i in range(len(m)):
	x += delta[i] * b[i] * a[i]
x = int(x) % n

if show_steps:
	print("----------------------------")
	print("Solve for x\n")
	sys.stdout.write("x = (")
	for i in range(len(m)):
		sys.stdout.write(str(delta[i]) + "*" + str(b[i]) + "*" + str(a[i]) + ")")
		if m[i] != m[-1]:
			sys.stdout.write(" + (")
	sys.stdout.write(" mod " + str(n) + "\n")

	sys.stdout.write("x = (")
	for i in range(len(m)):
		sys.stdout.write(str((delta[i]) * (b[i]) * (a[i])) + ")")
		if m[i] != m[-1]:
			sys.stdout.write(" + (")
	sys.stdout.write(" mod " + str(n) + "\n")

	sys.stdout.write("x = ")
	total = 0
	for i in range(len(m)):
		total += (delta[i]) * (b[i]) * (a[i])
	sys.stdout.write(str(total) + " mod " + str(n) + "\n")
	print("----------------------------\n")

print(str(x))
