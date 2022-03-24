import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from functools import partial
from time import sleep


class Sample:
    """
    using Proccess pool executor 
        for running blocking thread in parallel or concurrent way
        we create a proccess pool executor
        and in an event loop with asyncio.gather run our task in a proccess
    """
    def my_heavy_async_procces(self):
        print("start heavy proccess 0")
        for i in range(10):
            sleep(1)
            print(i, "heavy proccess 0")  
    
    def my_heavy_async_procces1(self):
        print("start heavy proccess 1")
        for i in range(10):
            sleep(1)
            print(i, "heavy proccess 1")  
            
    def my_heavy_async_procces2(self):
        print("start heavy proccess 2")
        for i in range(10):
            sleep(3)
            print(i, "heavy proccess 2")  
            
    def my_heavy_async_procces3(self):
        print("start heavy proccess 3")
        for i in range(10):
            sleep(3)
            print(i, "heavy proccess 3")  
            
    async def main(self):
        """process pool executor
        running with event loops and async 
        """
        with ProcessPoolExecutor() as proccess_pool:
            loop: AbstractEventLoop = asyncio.get_running_loop()
            call_coros = []
            calls = [
                self.my_heavy_async_procces, 
                self.my_heavy_async_procces1,
                self.my_heavy_async_procces2,
                self.my_heavy_async_procces3,
                ]
            
            for call in calls:
                call_coros.append(
                    loop.run_in_executor(proccess_pool, call)
                    )
            results = await asyncio.gather(*call_coros)
            
            for res in results:
                print(res)
    
    def main2(self):
        """simple usage of thread pool executor
        using submit() method.
        
        """
        with ThreadPoolExecutor() as executor:
            executor.submit(self.my_heavy_async_procces)
            executor.submit(self.my_heavy_async_procces1)

sample = Sample()
asyncio.run(sample.main())