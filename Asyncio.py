#Here we learn about Asyncio#

import time
import asyncio
import requests
async def function1():
    # time.sleep(3)
    url = 'https://www.facebook.com/favicon.ico'
    response = requests.get(url, allow_redirects=True)
    open('facebook2.ico', 'wb').write(response.content)
    # await asyncio.sleep(1)
    print('return func1')
    return 'maaz'
    
    
async def function2():
    url = 'https://www.facebook.com/favicon.ico'
    response = requests.get(url, allow_redirects=True)
    open('facebook3.ico', 'wb').write(response.content)
    time.sleep(3)
    print('return func2')
    
    

async def function3():
    url = 'https://www.facebook.com/favicon.ico'
    response = requests.get(url, allow_redirects=True)
    open('facebook.ico', 'wb').write(response.content)
    time.sleep(6)
    print('return func3')
    

async def main():
    task=asyncio.create_task(function1())
    await function1()
    await function2()
    await function3()
    
    L=await asyncio.gather(
    #     function1(),
    #     function2(),
    #     function3(),
    # )
    
    # print(L)
    
asyncio.run(main())