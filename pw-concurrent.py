from electrum import bitcoin
import itertools
from Queue import Queue
from threading import Thread

u = [
     ["y", "Y"],
     ["o", "O", "0"],
     ["u", "U"]
    ]


pw_prefix = [
       ["", "?", "^", "*", "&", "!", "|"],
       ["", "7980", "8990", "5950", "1010220"],
       ["", "7980", "8990", "5950", "1010220"],
    ]

u = ["".join(i) for i in itertools.product(*u)]

pw = [
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

q = Queue(20)

def worker():
  while True:
    prefix = q.get()
    for i in itertools.product(*pw):
      p = str(prefix+"".join(i))
      #print p
      try:
        bitcoin.pw_decode(s, p)
        solved = True
        print p
        print "success"
        with open('password.txt', 'w') as f:
          f.write(p)
      except:
        pass
    q.task_done()

for i in range(6):
  t = Thread(target=worker)
  t.daemon = True
  t.start()
    
for i in itertools.product(*pw_prefix):
  #print q.qsize()
  q.put(str(i[1]+i[0]+i[2]+i[0]))

q.join()

print "done"
