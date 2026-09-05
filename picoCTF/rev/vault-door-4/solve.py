password_bytes = [
    106, 85, 53, 116, 95, 52, 95, 98,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o67, 0o65,
    '9', '6', '0', '0', 'a', 'b', 'c', '3'
]

password_str = ""

for byte in password_bytes:
    if isinstance(byte, int):
        password_str += chr(byte)
    else:
        password_str += byte

print("picoCTF{" + password_str + "}")