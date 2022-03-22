# Learn Asyncio 

these notes are collected from `python concurrency with asyncio` book.

## Coroutines
couroutines are like a regular python functions but with the superpower that it can pause its execution when it encounters an operations that could take a while to complete.

`async` keywords will let us define a coroutines.

`await` keywords will let us pause our coroutines when we have a long-running operation.

### create coroutines
```python
import asyncio

async def my_coroutines():
    await asyncio.sleep(4)
    print("this is my coroutine")
```

## mudoles

- `asyncio.run()`
    * create a event-loop and run couroutine in event loop

- `asyncio.sleep(4)`
    * awaitable sleep with asyncio

- `asyncio.get_running_loop()`
    * get current running event loop

- `asyncio.new_event_loop()`
    * create new event loop 





## decorator for timing coroutines

```python
import functools
import time 
from typing import Callable, Any

def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"starting {func} ")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end-start

                print(f"finished {func} in {total:.4f} seconds")
            return wrapped
        
        return wrapper
```        