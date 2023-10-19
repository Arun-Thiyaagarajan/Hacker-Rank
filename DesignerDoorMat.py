#eg: print
# Size: 7 x 21 
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

# My Solution
n, m = map(int, input().split())

for i in range(n):
    if (i != n // 2):
        dashes = abs((m // 2) - (3 * i) - 1)
				
				# (2*i+1) is odd no. sequence and here pattern is ".|."
        pattern = (2 * i + 1) if (i < n // 2) else pattern - 2

        line = ("-" * dashes) + (".|." * pattern) + ("-" * dashes)
        print(line)

    else:
				# This code is only for the middle row i.e. for WELCOME row 
        dashes = (m - 7) // 2
        pattern += 2
        line = ("-" * dashes) + "WELCOME" + ("-" * dashes)
        print(line)

# Shorrter Version
import os
os.system('cls')
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))