from typing import List


def rotate(string: str, n: int) -> str:
   """Rotate characters in a string.
      Expects string and n (int) for number of characters to move.
   """

   string_list: List[str] = list(string)
   count = 0
   while count < abs(n):

      if n >= 0:

         element = string_list.pop(0)
         string_list.append(element)
      
      else:

         element = string_list.pop()
         string_list.insert(0, element)

      count += 1
   
   return ''.join(string_list)