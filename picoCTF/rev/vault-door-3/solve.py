s = "jU5t_a_sna_3lpm13gf49_u_4_m9r540"

password = ""

password += s[0:8] # for loop 1 
password += s[8:16][::-1] # for loop 2

for i in range(16, 32):
    if i % 2 == 0: # for loop 3
        password += s[46-i]
    else: # for loop 4
        password += s[i]

print("picoCTF{" + password + "}")