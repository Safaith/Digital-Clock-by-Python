w1 = input("w1: ")
w2 = input("w2: ")

print("\nEnter attribute of accuracy:")
B1 = input("B1: ")
B2 = input("B2: ")
B3 = input("B3: ")
Bh = float(1)-(float(B1) + float(B2) + float(B3))
print("\nBh =", Bh)

print("\n Probability mass for accuracy :\n")
m1 = float(w1) * float(B1)
print("average probability mass m1 =", m1)
m2 = float(w1) * float(B2)
print("good probability mass m2 =", m2)
m3 = float(w1) * float(B3)
print("poor probability mass m3 =", m3)
m_bar = float(1)-float(w1)
print("m_bar =", m_bar)
m_tilda = float(w1) * float(Bh)
print("m_tilda =", m_tilda)
mH = float(m_bar)+float(m_tilda)
print("mH = ", mH)

print("\nEnter attribute of reputation :")
B1 = input("B1: ")
B2 = input("B2: ")
B3 = input("B3: ")
Bh = float(1)-(float(B1)+float(B2)+float(B3))
print("\nBh =", Bh)

print("\nProbability mass for reputation :\n")
m1 = float(w2) * float(B1)
print("average probability mass m1 =", m1)
m2 = float(w2) * float(B2)
print("good probability mass m2 =", m2)
m3 = float(w2) * float(B3)
print("poor probability mass m3 =", m3)
m_bar = float(1)-float(w2)
print("m_bar =", m_bar)
m_tilda = float(w2) * float(Bh)
print("m_tilda =", m_tilda)
mH = float(m_bar)+float(m_tilda)
print("mH = ", mH)
print("not pass")