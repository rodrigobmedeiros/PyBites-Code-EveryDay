def running_mean(sequence):
   """Calculate the running mean of the sequence passed in,
   returns a sequence of same length with the averages.
   You can assume all items in sequence are numeric."""

   return [round(sum(sequence[:ind]) / ind, 2) for ind, _ in enumerate(sequence, start=1)]
