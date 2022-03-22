# Asyncio Create Tasks

you can use Create tasks for runing coroutines concurrently.

create a Task by .create_task() modules 
the await the created task

## Tasks Methods
- `.cancel()`
    * you can cancel a task if it take too long time.

- `.done()`
    * check if task is done return `true` or `false`.

- `.wait_for()`
    * set a time out for task if it take more time than timeout.

- `.cancelled()`
    * check if a task is cancelled or not return `true` or `false`.

- `.sheild()`
    * prevent a task from cancelling . i make a shield for prevent from cancelling a task.
    
## blocking APIS(CPU bands Tasks)
remember that `Asyncio` has a sigle-threaded concurrency model. So we have a limitations of a single thread and the GIL.

if you create 2 same task they still executes squentially.becuase first block the event loop

for example `requests` library blocks the event loop from doing any thing concurrently. instead of using `requests` use `aiohttp` 
