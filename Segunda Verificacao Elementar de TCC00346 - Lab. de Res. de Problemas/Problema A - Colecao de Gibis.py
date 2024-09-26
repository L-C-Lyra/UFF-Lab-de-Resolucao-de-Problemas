n, c, m = map(int, input().split())
c_xi = list(map(int, input().split()))
m_yi = list(map(int, input().split()))
c_to_buy = 0

c_xi.sort()
m_yi.sort()

# for i in range(len(c_xi)):
    # switch = True
    # for j in range(len(m_yi)):
        # if c_xi[i] == m_yi[j] and switch:
            # switch = False
    # if switch:
        # c_to_buy += 1

for i in c_xi:
    switch = True
    if i in m_yi:
        switch = False
    if switch:
        c_to_buy += 1

print(c_to_buy)

