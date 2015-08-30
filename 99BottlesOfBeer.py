def sing_99_bottles():
  for i in range(99, 0, -1):
    print "%d bottles of beer on the wall, %d bottles of beer." % (i, i)
    print "Take one down, pass it around, %d bottles of beer on the wall.\n" % (i - 1)
    
sing_99_bottles()
