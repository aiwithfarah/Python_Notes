import multiprocessing


def heavy_calculation(num):
    return num*num*num


if __name__ == '__main__':
    # creates multiple processses / a pool of workers
    # if you have 4 cores ot can do 4 calculations at the exact same time
    with multiprocessing.Pool() as p:
        print(p.map(heavy_calculation, [1, 2, 3]))  # [1,8,27]
