import re

f = open("KEI.html", "r", encoding="latin1")
teks = f.read()
f.close()

s = r"([\w+]+)</a></td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>([\d.\d\d]+)"

strings4 = re.findall(s, teks)

print("No 4 ekstrak semua nama negara :")
print(strings4)
print()



































##f = open("Indonesia.txt", "r", encoding="latin1")
##teks = f.read()
##f.close()

##p = r"me\w+"
##strings1 = re.findall(p, teks)
##print("No 1 awalan me :")
##print(strings1)
##print()

##q = r"di\w+"
##strings2 = re.findall(q, teks)
##print("No 2 awalan di :")
##print(strings2)
##print()

##r = r"di\s\w+"
##strings3 = re.findall(r, teks)
##print("No 3 awalan di  :")
##print(strings3)
##print()


