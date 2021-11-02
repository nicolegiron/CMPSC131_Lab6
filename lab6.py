# Author: Nicole Giron nqg5259@psu.edu
# Collaborator: Bakhtiar Reza bmr5782@psu.edu
# Collaborator:Aditya Majumdar apm6483@psu.edu
# Collaborator: Christopher McKinney cmm8086@psu.edu
# Section: 4
# Breakout: 10

def count_non_overlapping(s, substr, start):
  """
  Return the number of non-overlapping occurrences of substr in s
  starting from the index start.
  You can not use str method s.count.
  """
  total = 0
  i = 0
  nS = s[start:]
  s = s[start:]
  while i < len(nS):
    if(nS[i: i+len(substr)] == substr):
      total+=1
      i+=len(substr)
    else:
      i+=1
  return total

def count_non_overlapping_m(s, substr, start):
  """
  Return the number of non-overlapping occurrences of substr in s
  starting from the index start.
  You must use a one-liner implementation by using s.count().
  """
  return s.count(substr, start, len(s))

def find_smallest(t):
  """
  Return the smallest element in given list t.
  Return None if t is empty
  """
  if len(t)==0:
    return None
  else:
    beg = t[0]
    for i in range(1, len(t)):
      if t[i] < beg:
        beg = t[i]
    return beg

def myfilter(t, cond):
  """
  t is a list, cond(x) is a boolean function that returns True or False
  given an element x in t.
  Return a new list that only includes element x from t such cond(x) is True. 
  """
  l=[]
  for x in t:
      if(cond(x)):
        l.append(x)
  return l

def is_palindrome(s):
  return s[::-1] == s

def is_even(n):
  return n % 2 == 0

def run():
  s = input("Enter a string: ")
  t = input("Enter a substring to count: ")
  i = int(input("Entera starting index: "))
  c1 = count_non_overlapping(s, t, i);
  print(f"{t} occurred in {s} {c1} times starting from index {i}.")
  c2 = count_non_overlapping_m(s, t, i);
  print(f"{t} occurred in {s} {c2} times starting from index {i}.")

  print("Testing find_smallest:")
  t1 = [5, 8, 10, 2, 7] 
  print(f"min in {t1} is {find_smallest(t1)}")
  t1 = ["hello", "apple", "banana", "world"]
  print(f"min in {t1} is {find_smallest(t1)}")
  
  print("Testing myfilter:")
  t1 = ["a", "apple", "racecar", "hannah", "banana"]
  print(f"filering {t1} with is_palindrome is {myfilter(t1, is_palindrome)}")
  t2 = list(range(0, 50, 3))
  print(f"filtering {t2} with is_even is {myfilter(t2, is_even)}")


if __name__ == "__main__":
  run()
