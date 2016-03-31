from electrum import bitcoin

i = 0
with open("/home/clint/password-list/crackstation.txt") as infile:
    for line in infile:
        i+=1
        if i % 1000 == 0:
            print i," / 1493677782", float((i/1493677782)*100),"%"
        try:
            bitcoin.pw_decode(s, line)
            print line
            break
        except:
            pass

print "fail"
