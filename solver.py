encrypted = "ZLT{Kdwhafy_ak_fgl_gtxmkuslagf}"
decrypted = ''

for i in encrypted:
    if i == '{' or i == '_' or i== '}':
        decrypted += i
    else :
        if i.isupper(): # Cas majuscule
            if (ord(i) - 18) < ord('A'):
                decrypted += chr(ord(i) + 8)
            else:
                decrypted += chr(ord(i) - 18)
        else: # cas minuscule
            if (ord(i) - 18) < ord('a'):
                decrypted += chr(ord(i) + 8)
            else:
                decrypted += chr(ord(i) - 18)

print (decrypted)

