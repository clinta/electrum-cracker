import itertools

words = u"cargo series gloom wing normal velvet sock acid fat view wing rib"

for subset in itertools.permutations(words.split()):
  print " ".join(subset)
