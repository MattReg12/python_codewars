import math

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

def string_to_seconds(str):
    hours, minutes, seconds = str.split(':')
    return (int(hours) * SECONDS_IN_HOUR) + (int(minutes) * SECONDS_IN_MINUTE) + (int(seconds))

def video_part(part, total):
  part_seconds = string_to_seconds(part)
  total_seconds = string_to_seconds(total)
  gcd = math.gcd(part_seconds, total_seconds)

  return [part_seconds // gcd, total_seconds // gcd]
