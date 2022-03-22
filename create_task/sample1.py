import asyncio
import time
from turtle import st 


class Sample1:
    
    def __init__(self):
        pass
    
    async def task1_concurrent(self):
        for i in range(10):
            await asyncio.sleep(0.5)
            print("sleep 0.5 and number:", i)
    
    async def task2_concurrent(self):
        for i in range(10):
            await asyncio.sleep(1)
            print("sleep 1 and number:", i)

    async def main(self):
        start = time.time()
        print("start")
        await self.task1_concurrent()
        await self.task2_concurrent()
        print("end")
        end = time.time()
        print(end-start)

# it will took 15 second 
# sample = Sample1()
# asyncio.run(sample.main())



# now lets make sample 11 main() async 
# untill task1 & task2 run together we should use create_task() 
# in asyncio

class Sample1Async(Sample1):
    async def main(self):
        task1 = asyncio.create_task(self.task1_concurrent())
        task2 = asyncio.create_task(self.task2_concurrent())
        
        print("start")
        start = time.time()
        
        await task1
        await task2
        
        print("end")
        end = time.time()
        print(end - start)


# it took 10 second time
sample = Sample1Async()

asyncio.run(sample.main())    