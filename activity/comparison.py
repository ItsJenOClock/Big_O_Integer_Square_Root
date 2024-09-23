from activity.find_square_root_integer import (
    find_square_root_integer,
    find_square_root_integer_linear
)

import math
import time

LOOP_COUNT = 100_000

def check_many_values():
    for i in range(LOOP_COUNT):
        assert find_square_root_integer(i) == int(math.sqrt(i))

    print(f"matched all values up to {LOOP_COUNT}")

def check_many_values_linear():
    for i in range(LOOP_COUNT):
        assert find_square_root_integer_linear(i) == int(math.sqrt(i)), f"wrong at {i=}"

    print(f"matched all values up to {LOOP_COUNT}")

def timing():
    start_time_in_s = time.perf_counter()
    for i in range(LOOP_COUNT):
        find_square_root_integer(i)
    stop_time_in_s = time.perf_counter()
    print(f"find_square_root_integer={stop_time_in_s - start_time_in_s}")
    
    start_time_in_s = time.perf_counter()
    for i in range(LOOP_COUNT):
        find_square_root_integer_linear(i)
    stop_time_in_s = time.perf_counter()
    print(f"find_square_root_integer_linear={stop_time_in_s - start_time_in_s}")
    
    start_time_in_s = time.perf_counter()
    for i in range(LOOP_COUNT):
        int(math.sqrt(i))
    stop_time_in_s = time.perf_counter()
    print(f"int(math.sqrt())={stop_time_in_s - start_time_in_s}")
    
