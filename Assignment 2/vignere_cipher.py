key = "jcjcffcccb"
encrypted_text = "Kg fcwd qh vin pnzy hjcocnt cjjwg ku wnth nnyvng kxa cjjwg.Urfjm xwy yjg rbbufqwi \"vjg_djxn_ofs_dg_rmncbgi\" yq iq uqtxwlm.Oca zxw qcaj vjg tctnplyj hqs cjn pjcv ejbvdnt. Yt hkpe cjn gcnv,aqv okauy bknn ongm vt zvvgs vcpkh bqtft cjntj.";
decrypted_text ,j = "" , 0
for i in range(len(encrypted_text)):
    if encrypted_text[i] >= 'a' and encrypted_text[i] <= 'z':
        diff = (ord(encrypted_text[i]) - ord(key[j]) + 26) % 26
        temp = chr(ord('a')+diff)
        j = (j+1)%(len(key))
    elif encrypted_text[i] >= 'A' and encrypted_text[i] <= 'Z':
        diff = (ord(encrypted_text[i].upper()) - ord(key[j].upper()) + 26) % 26
        temp = chr(ord('A')+diff)
        j = (j+1)%(len(key))
    else:
        temp = encrypted_text[i]
    decrypted_text += temp
print(decrypted_text)