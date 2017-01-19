def words(stringList):
  counts = {}
  items = stringList.split()
  
  for item  in items:
    if item in counts:
      counts[item] = counts[item] + 1
    else:
      counts[item] = 1
  return counts
