W_College = []
K_College = []
for i in range(1, 21):
    if i < 11:
        n = int(input())
        W_College.append(n)
    else:
        m = int(input())
        K_College.append(m)
    
    W_College.sort(reverse=True)
    K_College.sort(reverse=True)


W_Sum = W_College[0] + W_College[1] + W_College[2]
K_Sum = K_College[0] + K_College[1] + K_College[2]

print(W_Sum, K_Sum)