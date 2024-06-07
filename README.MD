# Python Asyncio Lab
This project aims to demonstrate the execution behavior in cooroutines and threads and their interaction with memory.

## 1. Task
The file `asyncio-gather.py` shows a scenario where tree functions are called.
- exec: `python3 examples/task/asyncio-gather.py`

Example terminal output:
```Bash
+------------------------+
A(6): AAAAAA
B(8): BBBBBBBB
C(8): CCCCCCCC
+------------------------+
```

Optional:
- With debug, log: `python3 examples/task/asyncio-gather.py --debug`
- With debug real time, log: `python3 examples/task/asyncio-gather.py --debug-real-time`

## 2. Task with timeout
The file `timeout-asyncio-gather.py` is ready with timeout.
- exec: `python3 examples/task/timeout-asyncio-gather.py`

Example terminal output:
```Bash
[15:05:55]:[EXCEPTION] The operation timed out...
[15:05:55]:[EXCEPTION] The tasks will canceled...
+------------------------+
+------------------------+
```

Example files outputs:
Each process have a log file:
- `cat examples/task/storage/a.txt`
- `cat examples/task/storage/b.txt`
- `cat examples/task/storage/c.txt`

Optional:
- With debug, log: `python3 examples/task/timeout-asyncio-gather.py --debug`
- With debug real time, log: `python3 examples/task/timeout-asyncio-gather.py --debug-real-time`

Obs:
This scenario in timeout condition, the tasks will be canceled.

*_tested using Python 3.10.12_