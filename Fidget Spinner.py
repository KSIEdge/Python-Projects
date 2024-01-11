import sys
import time

#creates a spinner in console
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for i in range(100):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
