def haiku_checker(line_1,line_2,line_3):
  vowel = "aeiouyAEIOUY"
  syllable2 = "aiouyAIOUY"
  total_1 = 0
  total_2 = 0
  total_3 = 0

  if len(line_1) == 1 or line_1[0] == "":
    print "Invalid line 1 entry, do not start entry with a space or leave entry empty, add spaces between words."
  else:
    for item in line_1:
      if len(item) == 1:
        total_1 += 1
      else:
        if item[0] in vowel:
          total_1 += 1
        for i in range(1, len(item)):
          if item[i] in vowel and item[i-1] not in vowel:
            total_1 += 1
        if item[len(item)-1] == "e" or item[len(item)-1] == "E":
          total_1 -= 1    
    print "Syllables in line 1: %d" % total_1

  

  if len(line_1) == 1 or line_2[0] == "":
    print "Invalid line 2 entry, do not start entry with a space or leave entry empty, add spaces between words."
  else:      
    for item in line_2:
      if len(item) == 1:
        total_2 += 1
      else:
        if item[0] in vowel:
          total_2 += 1
        for i in range(1, len(item)):
          if item[i] in vowel and item[i-1] not in vowel:
            total_2 += 1
        if item[len(item)-1] == "e" or item[len(item)-1] == "E":
          total_2 -= 1 
    print "Syllables in line 2: %d" % total_2        


  if len(line_1) == 1 or line_3[0] == "":
    print "Invalid line 3 entry, do not start entry with a space or leave entry empty, add spaces between words."
  else:
    for item in line_3:
      if len(item) == 1:
        total_3 += 1
      else:
        if item[0] in vowel:
          total_3 += 1
        for i in range(1, len(item)):
          if item[i] in vowel and item[i-1] not in vowel:
            total_3 += 1
        if item[len(item)-1] == "e" or item[len(item)-1] == "E":
          total_3 -= 1 
    print "Syllables in line 3: %d" % total_3     
          

    if total_1 == 5 and total_2 == 7 and total_3 == 5:
      print "This is a haiku"
      return True
    else:
      print "This is not a haiku as the correct syllables per line has not been met"
      return False
