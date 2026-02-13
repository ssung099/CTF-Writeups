from collections import defaultdict
import re

phonetic_map = {"A":"ALPHA","B":"BRAVO","C":"CHARLIE","D":"DELTA","E":"ECHO","F":"FOXTROT","G":"GOLF","H":"HOTEL","I":"INDIA","J":"JULIETT","K":"KILO","L":"LIMA","M":"MIKE","N":"NOVEMBER","O":"OSCAR","P":"PAPA","Q":"QUEBEC","R":"ROMEO","S":"SIERRA","T":"TANGO","U":"UNIFORM","V":"VICTOR","W":"WHISKEY","X":"XRAY","Y":"YANKEE","Z":"ZULU","_":"UNDERSCORE","{":"OPENCURLYBRACE","}":"CLOSECURLYBRACE","0":"ZERO","1":"ONE","2":"TWO","3":"THREE","4":"FOUR","5":"FIVE","6":"SIX","7":"SEVEN","8":"EIGHT","9":"NINE"}
f = open("./ct.txt")
line = f.readline()
dict = defaultdict(int)

def phonetic_mapping(ptext):
    cleanptext = re.sub(r'[^a-zA-Z0-9_{}]', '', ptext).upper()
    mapped = "".join([phonetic_map[c] for c in cleanptext])
    if (len(mapped) % 2 == 1):
        mapped += "X"
    return mapped

def generate_known():
    bigram_map = {}
    known = phonetic_mapping(phonetic_mapping("lactf{"))
    for i in range(0, len(known), 2):
        value = known[i:i+2]
        key = line[i:i+2]
        bigram_map[key] = value
    bigram_map.update({"HS" :"SI", "QC":"AO", "ZW":"EO", "TF":"MI", "TT": "RU", "TG":"OR","PR":"OM","SR":"OH","IO":"OF","KG":"RR","UG":"OU","MJ":"AU","ML":"AE","NO":"AF","YL":"AT","NR":"CT","PC":"VI","CD":"XT","JF":"TO","NE":"FH", "NQ":"AG","FF":"AS","CS":"OY","MI":"RE","WB":"YA","NG":"NK","UB":"UN","CP":"IF","TZ":"MR","SV":"RV","LL":"IC","OR":"RD","ZF":"MN","ZJ":"ES","VP":"RG","FB":"RN","PG":"OG","SZ":"DE","YU":"LT","NZ":"RI","QN":"AK","JI":"IL","ST":"YH","VU":"IS","KT":"WH","DP":"AV","SE":"BR", "FP":"KI","RI":"LO", "EP":"RW", "RV":"HI","SM":"SK", "GC":"EY", "LF":"OZ", "OO":"UL","ED": "UE", "LX":"OE","EI":"ZU", "LN":"LU"})
    bigram_map.update({"QJ":"OV","KZ":"EM","EH":"BE", "UW": "ON"})

    # ED -> ?E
    # LF -> O?
    # EP -> R?
    return bigram_map

def decode_phonetic_concatenated(s):
    """
    Decode a concatenated phonetic string into letters using phonetic_map.
    
    Args:
        s (str): concatenated phonetic words (no spaces)
        phonetic_map (dict): char -> phonetic word
    
    Returns:
        str: decoded letters
    """
    # Reverse map: word -> char
    reverse_map = {v: k for k, v in phonetic_map.items()}
    # Sort phonetic words by length descending (greedy match)
    words = sorted(reverse_map.keys(), key=len, reverse=True)
    
    result = ""
    i = 0
    while i < len(s):
        matched = False
        for w in words:
            if s.startswith(w, i):
                result += reverse_map[w]
                i += len(w)
                matched = True
                break
        if not matched:
            # unknown part, put a placeholder or skip
            result += "?"
            i += 1
    return result

def break_ciphertext():
    for i in range(0, len(line), 2):
        bigram = line[i:i+2]
        dict[bigram] += 1
        print(bigram)

def word_to_letter(text):
    reverse_phonetic_map = {v: k for k, v in phonetic_map.items()}
    words = text.strip().split()
    return "".join(reverse_phonetic_map[word] for word in words)

if __name__ == "__main__":
    bigram_map = generate_known()
    final = ""
    unknown_map = {}
    count = 0
    for i in range(0, len(line), 2):
        bigram = line[i:i+2]
        if bigram not in bigram_map:
            final = final + f"[{bigram}:UNK]"
            unknown_map[bigram] = "UNK"
            count += 1
        else:
            final += bigram_map[bigram]

    # print(final)
    # print(unknown_map)
    # print(bigram_map)

    # print(phonetic_mapping("lactf{"))
    # print(phonetic_mapping(phonetic_mapping("lactf{")))
    # print(phonetic_mapping(phonetic_mapping("w}")))

    # print(word_to_letter("UNIFORM NOVEMBER DELTA ECHO ROMEO SIERRA CHARLIE OSCAR ROMEO ECHO OSCAR NOVEMBER ECHO UNIFORM NOVEMBER DELTA ECHO ROMEO SIERRA CHARLIE OSCAR ROMEO ECHO WHISKEY HOTEL INDIA SIERRA KILO ECHO YANKEE OSCAR NOVEMBER ECHO LIMA INDIA MIKE ALPHA LIMA INDIA MIKE ALPHA UNIFORM NOVEMBER DELTA ECHO ROMEO SIERRA CHARLIE OSCAR ROMEO ECHO TANGO ALPHA NOVEMBER GOLF OSCAR ALPHA LIMA PAPA HOTEL ALPHA KILO INDIA LIMA OSCAR TANGO HOTEL ROMEO ECHO ECHO UNIFORM NOVEMBER DELTA ECHO ROMEO SIERRA CHARLIE OSCAR ROMEO ECHO OSCAR NOVEMBER ECHO TANGO ALPHA NOVEMBER GOLF OSCAR UNIFORM NOVEMBER DELTA ECHO ROMEO SIERRA CHARLIE OSCAR ROMEO ECHO FOXTROT OSCAR XRAY TANGO ROMEO OSCAR TANGO ZULU ECHO ROMEO OSCAR ROMEO OSCAR MIKE ECHO OSCAR UNIFORM NOVEMBER DELTA ECHO ROMEO SIERRA CHARLIE OSCAR ROMEO ECHO NOVEMBER OSCAR VICTOR ECHO MIKE BRAVO ECHO ROMEO ZULU ECHO ROMEO OSCAR WHISKEY HOTEL INDIA SIERRA KILO ECHO YANKEE CHARLIE LIMA OSCAR SIERRA ECHO CHARLIE UNIFORM ROMEO LIMA YANKEE BRAVO ROMEO ALPHA CHARLIE ECHO"))

    # print(word_to_letter("UNDERSCORE ONE UNDERSCORE WHISKEY ONE LIMA LIMA UNDERSCORE TANGO ALPHA KILO THREE UNDERSCORE ONE TANGO UNDERSCORE FOXTROT ZERO ROMEO UNDERSCORE NOVEMBER ZERO WHISKEY CLOSECURLYBRACE"))

    # print("=====")
    print(decode_phonetic_concatenated(decode_phonetic_concatenated(final)).lower())
# lactf{}
# LIMA_ALPHA_