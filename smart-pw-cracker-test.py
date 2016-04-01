from electrum import bitcoin
import itertools

pw = [
       ["", "P", "p"],
       ["", "A", "a"],
       ["", "S", "s"],
       ["", "S", "s"],
       ["", "W", "w"],
       ["", "O", "o"],
       ["", "R", "r"],
       ["", "D", "d"],
     ]

s = "0JCC965FrZgUYJcKPNwiOKCznP/j0i0u15uHq1Z+u4jwIroTj337wnKz/yW6CgREDPYnMtd5+O2DsxJXKYbWIWbar4pzOpqzl9FZUoZ8GykFL4kFWHxRnNlN6y4v9BD5+D6ul2X7N1nTNR+nrmCKwGVtAFBOUqYM3aDMDIghaGM="

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
