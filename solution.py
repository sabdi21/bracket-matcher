
def bracket_matcher(input): 

  open_list = ["[","{","("]
  close_list = ["]","}",")"]
  stack= []
  for i in input:
      if i in open_list:
          stack.append(i)
      elif i in close_list:
          pos = close_list.index(i)
          if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
              stack.pop()
          else:
              return "Unbalanced"
  if len(stack) == 0:
      return "Balanced"
  return bracket_matcher("{[()](){}}")

bracket_matcher('abc(123)')
# returns true

bracket_matcher('a[b]c(123')
# returns false -- missing closing parens

bracket_matcher('a[bc(123)]')
# returns true

bracket_matcher('a[bc(12]3)')
# returns false -- improperly nested

bracket_matcher('a{b}{c(1[2]3)}')
# returns true

bracket_matcher('a{b}{c(1}[2]3)')
# returns false -- improperly nested

bracket_matcher('()')
# returns true

bracket_matcher('[]]')
# returns false - no opening bracket to correspond with last character

bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched