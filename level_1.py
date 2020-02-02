s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

ns = ''
for c in s:
  if c in ascii_letters:
    ns = ns + ascii_letters[(ascii_letters.index(c)+2)%len(ascii_letters)]
  else:
    ns += c
   
ns = ns.lower()
print(ns)
