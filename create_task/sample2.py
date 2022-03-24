import asyncio
from time import sleep


class Sample2:
    """Sample 2 class 
        this class is made for showing if its possible to make 
        heavy proccecing none blocking by using asyncio.sleep()
        
        result: 
            when i ran this module i found out that it will run sequencially
            and there is no concurrent action 
            because of blocking action
        
    """
    def __init__(self):
        pass
    
    async def my_heavy_async_procces(slef):
        print("heavy task 0")
        await asyncio.sleep(2)
        
        for i in range(10):
            await asyncio.sleep(1)
            print(i, "heavy proccess 0")                
    
    async def main(self):
        
        tasks_list = []
        for i in range(3):
            tasks_list.append(
                asyncio.create_task(self.my_heavy_async_procces())
                )
        [await task for task in tasks_list]        
        # asyncio.gather(*tasks_list)
        

# object = Sample2()
# asyncio.run(object.main(), debug=True)

class Sample3(Sample2):
    async def my_heavy_async_procces1(self):
        print("heavy task 1")
        await asyncio.sleep(1.5)
        for i in range(10):
            await asyncio.sleep(1)
            print(i, "async proccess 1")   
    
    async def main(self):
        tasks = [
            asyncio.create_task(self.my_heavy_async_procces()) , 
            asyncio.create_task(self.my_heavy_async_procces1())
        ]
        
        # [await task for task in tasks]
        await asyncio.gather(*tasks)
        
sample = Sample3()

asyncio.run(sample.main())