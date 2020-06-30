def add_time(start, duration, weekDay = ''):
  startStr = start.split(':')
  startHour = int(startStr[0])
  startStr = startStr[1].split(' ')
  startMin = int(startStr[0])
  startPeriod = startStr[1]

  durationHour = int(duration.split(':')[0])
  durationMin = int(duration.split(':')[1])

  finalHour = startHour + durationHour
  finalMin = startMin + durationMin 
  finalPeriod = startPeriod
  finalDays = 0

  while finalMin >= 60:
    finalHour += 1
    finalMin -= 60

  if startPeriod == "PM" or finalHour >= 24:
    finalDays = round(finalHour / 24)
  
  while finalHour > 12:
    finalHour -= 12
    finalPeriod = "PM" if finalPeriod == "AM" else "AM" 

  if finalHour == 12:
    finalPeriod = "PM" if finalPeriod == "AM" else "AM" 

  if weekDay:
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    startDayIndex = days.index(weekDay.lower())
    finalDayIndex = startDayIndex + finalDays
    while finalDayIndex >= 7:
      finalDayIndex =- 7
    finalWeekDay = days[finalDayIndex]

  finalHour = str(finalHour)
  finalMin = str(finalMin)
  new_time = finalHour + ':' + ('0' + finalMin if len(finalMin) == 1 else finalMin) + ' ' + finalPeriod

  if weekDay:
    new_time += ', ' + finalWeekDay.title()

  if finalDays > 1:
    new_time += ' (' + str(finalDays) + ' days later)'
  if finalDays == 1:
    new_time += ' (next day)'


  return new_time
