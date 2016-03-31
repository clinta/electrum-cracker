from electrum import bitcoin
import sys
import itertools

i = 0
choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_$&#@ "
for length in range(0,20):
   for entry in itertools.product(choices,repeat = length):
      i+=1
      if i % 1000 == 0:
          print i
      password = ''.join(entry)
      #print password
      try:
          bitcoin.pw_decode(s, line)
          print password
          break
      except:
          pass

print "fail"
