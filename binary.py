class BinarySearch(list):
  """Class binary search that uses binary search algorithm"""

  def __init__(self, a, b):
      """Create a list of length a, firsting element b and step b"""

      list.__init__(self)
      first = b
      last = a * b
      self.length = a
      while first <= last:
          self.append(first)
          first += b

  def search(self, number):
      """Method search"""
      found = False
      first = 0
      last = self.length - 1
      mid = (first + last) // 2
      count = 0

      if (number == self[first]) or (number == self[last]) \
          or (number == self[mid]):
          return {
              'count': count,
              'index': self.index(number)
          }
      if self.count(number) == 0:
        return {
            'count': 3,
            'index': -1
            }
      else:
        while first < last and not found:

            mid = (first + last) // 2

            if number == self[mid]:
              found = True
            else:
              count += 1
              if number > self[mid]:
                  first = mid + 1
              else:
                  last = mid - 1

        if found:
          return {
              'count': count,
              'index': self.index(number)
          }
        else:
          return {
              'count': count,
              'index': -1
          }