#here we learn about multiprocessing#
import multiprocessing
import concurrent.futures
import requests


def downloadFile(url, name):
    print(f"started downloading {name}")
    response=requests.get(url)
    open(f"patriot/file{name}.jpg", "wb").write(response.content)
    print(f"Finished downloading {name}")


url="https://picsum.photos/2000/3000"
pros=[]

for i in range(60):
    # downloadFile(url, i)#
    if __name__ == '__main__':
        p=multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)
    
for p in pros:
    p.join()

# if __name__ == '__main__':
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         l1=[url for i in range(60)]
#         l2=[i for i in range(60)]
#         results=executor.map(downloadFile, l1, l2)
#     for r in results:
#         print(r)