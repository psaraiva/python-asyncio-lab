# Pyhton Asyncio Lab
This project aims to demonstrate the execution behavior in cooroutines and threads and their interaction with memory.

## 1. Task
The file `asyncio-gather.py` shows a scenario where tree functions are called.
- exec: `python3 ./examples/task/asyncio-gather.py`

Example terminal output:
```Bash
+------------------------+
A(6): AAAAAA
B(8): BBBBBBBB
C(8): CCCCCCCC
+------------------------+
```

Optional:
- With debug, log: `python3 ./examples/task/asyncio-gather.py` --debug
- With debug real time, log: `python3 ./examples/task/asyncio-gather.py --debug-real-time`

*_tested using Python 3.10.12_