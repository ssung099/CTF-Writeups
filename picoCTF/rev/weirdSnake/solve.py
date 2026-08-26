import re, sys

def extract_consts():
    vals = []
    f = open("chall/snake", "r")
    for line in f:
        if "LOAD_CONST" in line:
            m = re.search(r'\((\d+)\)', line)
            if m:
                vals.append(int(m.group(1)))
        else:
            break
    f.close()
    return vals

if __name__ == "__main__":
    vals = extract_consts()
    key = "t_Jo3"
    key_bytes = [ord(c) for c in key]

    flag = []
    for i in range(0, len(vals)):
        flag.append(vals[i] ^ key_bytes[i % len(key_bytes)])

    print(''.join(map(chr, flag)))