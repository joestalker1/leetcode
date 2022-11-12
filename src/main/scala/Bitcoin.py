from fastecdsa import keys, curve,ecdsa
priv_key, pub_key = keys.gen_keypair(curve.P256)
#print(priv_key)
#print(pub_key)
message = 'I am a message'
(r,s) = ecdsa.sign(message,priv_key)
print((r,s))
valid = ecdsa.verify((r,s),message,pub_key)
print(valid)