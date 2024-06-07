import argparse
import asyncio
import time
import random

async def main():
    global debug, debug_real_time, log
    log = []
    populate_args()

    start_time = time.time()
    msg = f"[Main] Started at {time.strftime('%X')}."
    log.append(msg)

    if debug_real_time:
        print(msg)

    result = await asyncio.gather(
        incrementRandon('A'),
        incrementRandon('B'),
        incrementRandon('C'))

    print("+------------------------+")
    for i in result:
        print(f"{i[0]}({len(i)}): {i}")
    print("+------------------------+")

    msg = f"[Main] finished at {time.strftime('%X')}."
    log.append(msg)
    if debug_real_time:
        print(msg)
    execution_time = time.time() - start_time
    msg = f"[Main] Duration: {format(execution_time, '.4f')} s."
    log.append(msg)
    if debug_real_time:
        print(msg)
    if debug and (debug_real_time == False or debug_real_time == None):
        [print(i) for i in log]

def populate_args():
    global debug, debug_real_time, log
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('--debug', action='store_true', help='Debug mode')
    parser.add_argument('--debug-real-time', action='store_true', help='Debug in real time')
    args = parser.parse_args()
    debug = args.debug
    debug_real_time = args.debug_real_time

async def incrementRandon(str) -> str:
    start_time = time.time()
    msg = f"[{str}] Started incrementRandon() at {time.strftime('%X')}."
    log.append(msg)
    if debug_real_time:
        print(msg)

    char = str
    for _ in range(3):
        sleep = random.randint(1, 3)
        msg = f"[{str}] Sleeping for {sleep}s."
        log.append(msg)
        if debug_real_time:
            print(msg)
        await asyncio.sleep(sleep)
        char += str * sleep
        if debug_real_time:
            print(f"[{str}] Value updated: {char}.")

    execution_time = time.time() - start_time
    msg = f"[{str}] Finished incrementRandon() at {time.strftime('%X')}."
    log.append(msg)
    if debug_real_time:
        print(msg)

    msg = f"[{str}] Duration: {format(execution_time, '.4f')}s."
    log.append(msg)
    if debug_real_time:
        print(msg)

    return char

asyncio.run(main())
