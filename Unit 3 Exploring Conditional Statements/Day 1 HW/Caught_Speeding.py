def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5

    if speed <= 60:
        return "No Ticket"

    if 61 <= speed <= 80:
        return "Small Ticket"

    return "Big Ticket"

print(caught_speeding(73, True))
print(caught_speeding(83, True))
print(caught_speeding(83, False))
