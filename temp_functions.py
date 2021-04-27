def fahr_to_celsius(temp_fahrenheit):
  """convert from Fahrenheit to Celsius"""
  converted_temp = (temp_fahrenheit - 32) / 1.8
  return converted_temp


def temp_classifier(temp_celsius):
  """classify into four groups by degrees"""
  if temp_celsius < -2:
    number = 0
    return number
  elif -2 <= temp_celsius < 2:
    number = 1
    return number
  elif 2 <= temp_celsius < 15:
    number = 2
    return number
  else:
    number = 3
    return number


