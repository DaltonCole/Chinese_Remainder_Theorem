print("Enter the number of congruences: ")
congruences = int(input())

# x = a mod m WHERE = is the congruence symbol

a = []
m = []

print("x = a mod m WHERE = is the congruence symbol")

for i in range(congruences):
	print("Enter 'a <space> m' for the " + str(i + 1) + " congruence")
	temp = input()
	a_temp, m_temp = temp.split(' ')
	a_temp = int(a_temp)
	m_temp = int(m_temp)
	a.append(a_temp)
	m.append(m_temp)

n = 1

for i in m:
	n *= i

delta = []

for i in m:
	delta.append(n/i)

b = []

for i in range(len(m)):
	b_temp = 1
	while True:
		multiplier = ((delta[i] * b_temp) - 1) / m[i]
		if multiplier.is_integer():
			b.append(b_temp)
			break
		else:
			b_temp += 1

x = 0
for i in range(len(m)):
	x += delta[i] * b[i] * a[i]

x = int(x) % n

print(str(x))
