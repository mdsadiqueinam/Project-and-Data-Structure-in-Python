# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main
import time

# starting time
start = time.time()


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_module', exit=False)

# sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

# program body ends

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")