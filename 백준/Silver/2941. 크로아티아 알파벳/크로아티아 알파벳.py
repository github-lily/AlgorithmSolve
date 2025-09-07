
text = input()
text = text.replace("dz=","*")
for p in ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=") :
    text = text.replace(p,"*")

print(len(text))