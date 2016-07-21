# don't touch these!
import multiprocessing
import time
import timeit

# fill out these functions
def slower_euler():
    fileIn = open('slower_euler.txt', 'r')
    #your code here

def faster_euler():
    fileIn = open('faster_euler.txt', 'r')
    #your code here


# no touchie
if __name__ == '__main__':
    start_time = timeit.default_timer()
    print("Running slower_euler:")
    se = multiprocessing.Process(target=slower_euler, name='slower_euler')
    se.start()
    se.join(10)

    if (se.is_alive()):
        print('Operation timeout. You have reached the end of your 10 seconds.')
        se.terminate()
    else:
        stop_time = timeit.default_timer()
        print('\nFinished slower_euler!\nRuntime:', stop_time - start_time, 'seconds')

    start_time = timeit.default_timer()
    print("\nRunning faster_euler:")
    fe = multiprocessing.Process(target=faster_euler, name='faster_euler')
    fe.start()
    fe.join(10)

    if (fe.is_alive()):
        print('Operation timeout. You have reached the end of your 10 seconds.')
        fe.terminate()
    else:
        stop_time = timeit.default_timer()
        print('\nFinished faster_euler!\nRuntime:', stop_time - start_time, 'seconds')

    