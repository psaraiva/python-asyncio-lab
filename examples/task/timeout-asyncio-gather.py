import argparse
import asyncio
import time
import random
import os

async def main():
    global debug, debug_real_time, log
    log = []
    populate_args()

    start_time = time.time()
    msg = f"[{time.strftime('%X')}]:[Main] Started."
    log.append(msg)
    if debug_real_time:
        print(msg)

    remove_files(['a','b','c'])

    try:
        result = []
        tasks = asyncio.gather(
            incrementRandon('A'),
            incrementRandon('B'),
            incrementRandon('C'))
        result = await asyncio.wait_for(tasks, timeout=6.0)
    except asyncio.TimeoutError:
        print(f"[{time.strftime('%X')}]:[EXCEPTION] The operation timed out...")
        print(f"[{time.strftime('%X')}]:[EXCEPTION] The tasks will canceled...")
        tasks.cancel()
    except asyncio.CancelledError:
        print(f"[{time.strftime('%X')}]:[EXCEPTION] The tasks have been cancelled")

    print("+------------------------+")
    for i in result:
        print(f"{i[0]}({len(i)}): {i}")
    print("+------------------------+")

    msg = f"[{time.strftime('%X')}]:[Main] Finished."
    log.append(msg)
    if debug_real_time:
        print(msg)
    execution_time = time.time() - start_time
    msg = f"[{time.strftime('%X')}]:[Main] Duration: {format(execution_time, '.4f')} s."
    log.append(msg)
    if debug_real_time:
        print(msg)
    if debug and (debug_real_time == False or debug_real_time == None):
        [print(i) for i in log]

def remove_files(files) -> None:
    for file in files:
        if os.path.exists(f"examples/task/storage/{file}.txt"):
            os.remove(f"examples/task/storage/{file}.txt")

def populate_args() -> None:
    global debug, debug_real_time, log
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('--debug', action='store_true', help='Debug mode')
    parser.add_argument('--debug-real-time', action='store_true', help='Debug in real time')
    args = parser.parse_args()
    debug = args.debug
    debug_real_time = args.debug_real_time

async def incrementRandon(str) -> str:
    start_time = time.time()
    msg = f"[{time.strftime('%X')}]:[{str}] Started incrementRandon()."
    file_name = 'examples/task/storage/'+str.lower()+'.txt'
    with open(file_name, 'a') as f:
        f.write(msg+'\n')
    log.append(msg)
    if debug_real_time:
        print(msg)

    char = str
    for _ in range(3):
        sleep = random.randint(1, 3)
        msg = f"[{time.strftime('%X')}]:[{str}] Sleeping for {sleep}s."
        log.append(msg)
        if debug_real_time:
            print(msg)
        char += str * sleep
        await asyncio.sleep(sleep)
        msg = f"[{time.strftime('%X')}]:[{str}] Value updated: {char}."
        with open(file_name, 'a') as f:
            f.write(msg+"\n")
        if debug_real_time:
            print(msg)

    execution_time = time.time() - start_time
    msg = f"[{time.strftime('%X')}]:[{str}] Finished incrementRandon()."
    log.append(msg)
    with open(file_name, 'a') as f:
        f.write(msg+'\n')

    if debug_real_time:
        print(msg)
    msg = f"[{time.strftime('%X')}]:[{str}] Duration: {format(execution_time, '.4f')}s."
    log.append(msg)
    with open(file_name, 'a') as f:
        f.write(msg+'\n')
    if debug_real_time:
        print(msg)
    return char

asyncio.run(main())
