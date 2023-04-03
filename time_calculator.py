def add_time(start, duration, weekday = "default"):

  parsed_start = start.split()
  parsed_start = parsed_start[0].split(":")
  parsed_start += start[-2]
  parsed_duration = duration.split(":")
  parsed_duration[0] = int(parsed_duration[0])
  parsed_duration[1] = int(parsed_duration[1])

  #parsed_start = {[0] -> [HH], [1] -> [MM], [2] -> [AM/PM]} 
  
  time_calculations = []
  time_calculations.append(int(parsed_start[0]) + parsed_duration[0])
  time_calculations.append(int(parsed_start[1]) + parsed_duration[1])
  days_pass = 0

  weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
  ]

  if time_calculations[1] > 59:
    time_calculations[0] = time_calculations[0] + 1
    time_calculations[1] = time_calculations[1] - 60
      
  if parsed_start[2] == 'P':
    time_calculations[0] += 12

  days_pass = time_calculations[0] // 24

  time_calculations[0] %= 24

  if time_calculations[0] == 0: time_calculations[0] = 12

  if time_calculations[0] > 12:
    time_calculations[0] -= 12
    parsed_start[2] = 'P'
  elif time_calculations[0] == 12 and parsed_start[2] == 'A':
    parsed_start[2] = 'P'
  else:
    parsed_start[2] = 'A'
  
  if weekday != 'default':
    for day in weekdays:
      if weekday.casefold() == day.casefold():
        weekday = day
        break
    day_index = weekdays.index(weekday)
    i = 0
    while i < days_pass:
      day_index = (day_index + 1) % 7
      weekday = weekdays[day_index]
      i += 1
      

  new_time = (f"{time_calculations[0]}:")
  
  if time_calculations[1] > 9:
    new_time = new_time + (f"{time_calculations[1]}")
  else:
    new_time = new_time + (f"0{time_calculations[1]}")

  new_time = new_time + (f" {parsed_start[2]}M")

  if weekday != "default":
    new_time = new_time + (f", {weekday}")

  if days_pass > 1:
    new_time = new_time + (f" ({days_pass} days later)")
  elif days_pass == 1:
    new_time = new_time + (" (next day)")

  return new_time