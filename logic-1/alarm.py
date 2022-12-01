def alarm_clock(day, vacation):
    if not vacation:
        if 1 <= day <= 5:
            return '7:00'
        else:
            return '10:00'

    if 1 <= day <= 5:
        return '10:00'
    else:
        return 'off'


print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))
