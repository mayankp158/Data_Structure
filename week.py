def readable_timedelta(days):
   weeks = days//7
   remaining = days%7
   return "weeks {} days {}".format(weeks,remaining)
# test your function
print(readable_timedelta(20))