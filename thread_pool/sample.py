import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from time import sleep
from asyncio.events import AbstractEventLoop


class SampleThreadPoolExecutor:
    def __init__(self):
        pass
    
    def my_heavy_task(self, num):
        print(f"start task num {num}")
        for i in range(10):
            sleep(0.5)
            print(i, f" heavy task num {num}")
    
    async def main(self):
        nums = [10,11,12,13]
        loop = asyncio.get_running_loop()
        with ThreadPoolExecutor() as pool:
            tasks = [loop.run_in_executor(
                pool, partial(self.my_heavy_task, num) 
            ) for num in nums]
            results = await asyncio.gather(*tasks)
            
        # if my python version was above 3.9 i could use this 
        # tasks = [asyncio.to_thread(self.my_heavy_task, num) for num in nums]
        
sample = SampleThreadPoolExecutor()

asyncio.run(sample.main())