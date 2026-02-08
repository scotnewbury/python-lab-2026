def is_leap_year(year: int) -> bool:
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_integer_from_user(prompt: str) -> int:
  while True:
    try:
      number = input(prompt)
      if not number:
        number = 0
      return(int(number))
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
