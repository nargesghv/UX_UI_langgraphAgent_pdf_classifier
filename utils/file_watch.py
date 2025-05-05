import os
import time

def watch_for_file(folder):
    seen = set()
    os.makedirs(folder, exist_ok=True)
    while True:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        new_files = [f for f in files if f not in seen]
        for file in new_files:
            seen.add(file)
            yield os.path.join(folder, file)
        time.sleep(2)
