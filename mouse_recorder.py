"""
Mouse recorder
"""

import sys
import time
from pynput.mouse import Controller

# Instanciates mouse controller object
mouse = Controller()

# List holding tuples <tuple(x_pos, y_pos), float(delay_time)>
positions = []


def record(duration: float) -> None:
    """
    Records user mouse input
    """

    pos = mouse.position

    time_zero = time.time()
    time_last = time_zero

    while time.time() - time_zero < duration:

        # Only records if mouse position changed
        if mouse.position != pos:

            pos = mouse.position
            delay_time = time.time() - time_last

            # Feeds tuple to the positions list
            positions.append((pos, delay_time))

            # Resets timer
            time_last = time.time()
        

def replay() -> None:
    """
    Replays user recorded mouse input
    """
    
    for tup in positions:

        # Sets mouse position
        mouse.position = tup[0]

        # Sleeps the delay time
        time.sleep(tup[1])


def main() -> None:
    
    try:
        input_message = "Input the duration of the recording (in seconds): "
        duration = float(input(input_message).replace(',', '.'))
    except ValueError:
        print("Please input a valid time in seconds.")
        sys.exit(1)

    input("Press any key to start recording...")
    print("Recording...")

    record(duration)
    
    input("Press any key to replay...")

    replay()


if __name__ == "__main__":
    main()
