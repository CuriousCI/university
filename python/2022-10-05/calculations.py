from math import pi as PI


# 42 42s


def seconds(minutes: int, seconds: int) -> int:
    return minutes * 60 + seconds


print(f'Second in 42 minuti e 42 secondi: {seconds(42, 42)}s')


# Km to miles

def km_to_miles(km):
    return km / 1.61


print(f'Miles in 10km: {km_to_miles(10)}',
      f'Miles in a marathon: {km_to_miles(40)}', sep='\n')


# Best runner!


def speed(distance: int, minutes: int, seconds: int) -> float:
    time = seconds(minutes, seconds)
    return time / distance


print(f'Average speed: {speed(10, 42, 42)}',
      f'Cadence: {speed(km_to_miles(10), 42, 42)}', sep='\n')


# Bob plays with 'biglie'


def sphere_volume(radius):
    return 4/3 * PI * radius**3


print(f'A \'biglia\' with raius 5\'kPotatoes\' has volume: {sphere_volume(5)}')


# Fantastic books and where to find 'em


price = 24.95 * .6
print(f'Total books cost: {3 + price + (0.75 + price) * 59}')


# Pendolari alla riscossa


travel_time = seconds(8, 15) + 3 * seconds(7, 12) + seconds(9, 45)
# Expressed in minutes
time = 6 * 60 + 52 + travel_time // 60
print(f'Ora di arrivo: {time // 60}:{time % 60}')
