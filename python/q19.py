'''19. Create a script that simulates a basic stopwatch with start, stop, and reset functionality.'''

import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            # current time in seconds since the Unix epoch (January 1, 1970, 00:00:00 UTC). 
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            print(f"Stopwatch stopped. Elapsed time: {self.format_time()}.")
        else:
            print("Stopwatch is not running.")

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        print("Stopwatch reset.")

    def format_time(self):
        elapsed = self.elapsed_time if not self.running else time.time() - self.start_time
        # divides two numbers and returns the quotient (min) and the remainder (sec) as a tuple.
        minutes, seconds = divmod(int(elapsed), 60)
        # extracting msec in sec and converting it to msec
        milliseconds = int((elapsed - int(elapsed)) * 1000)
        return f"{minutes:02}:{seconds:02}.{milliseconds:02}"

    def display(self):
        print(f"Elapsed time: {self.format_time()}.")

if __name__ == "__main__":
    stopwatch = Stopwatch()
    while True:
        print("\nOptions: [start, stop, reset, display, quit]")
        command = input("Enter command: ").strip().lower()
        if command == "start":
            stopwatch.start()
        elif command == "stop":
            stopwatch.stop()
        elif command == "reset":
            stopwatch.reset()
        elif command == "display":
            stopwatch.display()
        elif command == "quit":
            print("Exiting stopwatch.")
            break
        else:
            print("Invalid command. Please try again.")
