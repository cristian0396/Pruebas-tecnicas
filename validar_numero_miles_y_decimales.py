import re
def FormattedNumber(strArr):

  cad =  strArr[0]
  patron = re.match("^([0-9]{0,3},)*([0-9]{0,3})(.[0-9]+)?$", cad)
  
  if patron is not None:
    return True
  else:
    return False

print FormattedNumber(raw_input())
