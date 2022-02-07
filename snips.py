
# Super simple find/replace in same file
with open("test.txt") as r:
  text = r.read().replace("THIS", "THAT")
with open("test.txt", "w") as w:
  w.write(text)