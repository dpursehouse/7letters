import re
PATTERN = re.compile(r'[a-f0-9]{7}')
for line in open("words.txt"):
  for word in line.split():
    if PATTERN.match(word):
      print word
