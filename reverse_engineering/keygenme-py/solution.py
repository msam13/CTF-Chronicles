import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic_trial = ""
key_part_static2_trial = "}"

bUsername_trial = b"FREEMAN"
HashDigest = hashlib.sha256(bUsername_trial).hexdigest();

ilist = [4,5,3,6,2,7,1,8]

for i in ilist:
	key_part_dynamic_trial+=str(HashDigest[i])

print(key_part_static1_trial+key_part_dynamic_trial+key_part_static2_trial)