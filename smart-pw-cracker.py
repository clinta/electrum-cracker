from electrum import bitcoin
import itertools
import concurrent.futures

u = [
     ["y", "Y"],
     ["o", "O", "0"],
     ["u", "U"]
    ]

u = ["".join(i) for i in itertools.product(*u)]

pw = [
       ["", "7980", "8990", "5950", "1010220"],
       ["", "?", "^", "*", "&", "!", "|"],
       ["", "7980", "8990", "5950", "1010220"],
       ["", "?", "^", "*", "&", "!", "|"],
       ["e", "E", "3", "=", "[-"],
       ["l", "L", "|", "1", "!", "|_", "["],
       ["e", "E", "3", "=", "[-"],
       ["c", "C", "(", "<", "[", "{"],
       ["t", "T", "7", "+", "-|-", "]["],
       ["r", "R", "I2", "/2"],
       ["u", "U"] + u, 
       ["m", "M", "^^"],
       ["", ",./", "&*("]
     ]

s = "STcRhPfZeossbG60ZksnkuPVOicUb5dmOKiTS7Ch02AAJvXvGX0hu+qNZFaBbpGk/Jz6y6fCW54sjYKqZEFJs+D3ZUQNMPTj87CN3uC47z+pzhtDJt5ssfHkoJrL1KPwSWDxx0YnMUDg3b5gpIQnyNo60HBmT2c+ICOmryxQOio="

for i in itertools.product(*pw):
  p = "".join(i)
  print p
  try:
    bitcoin.pw_decode(s, p)
    print "success"
    break
  except:
    pass

print "done"
