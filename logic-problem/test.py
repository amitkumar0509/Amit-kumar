# Loading.
# Loading..
# Loading...
# Loading....
# Loading.....
# print("Loading"+ ".")
# print("Loading"+ "..")
import time
for i in range(0,6):
    # print("Loading"+ "."*i)
    print(f"\rLoading{'.' * (i + 1)}")
    time.sleep(0.5)