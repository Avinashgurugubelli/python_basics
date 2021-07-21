"""
Older and manual way of creating the multi processing
"""

import time

import multiprocessing


def do_something():
    print('Sleeping 1 second ...')
    time.sleep(1)
    print('Done Sleeping ....')


def do_something_with_args(sleep_seconds, process_name=None):
    print(
        f'Sleeping the process {process_name}, for {sleep_seconds} second(s) ...')
    time.sleep(sleep_seconds)
    print(f'{process_name} Sleeping done ....')


def call_do_something_in_sync_manner():
    # Start time
    start = time.perf_counter()
    do_something()
    do_something()
    # Finish time
    finish = time.perf_counter()
    # Actual time
    actual_time = round(finish-start, 2)
    print(f'finished in {actual_time} second(s)')


def call_do_something_fn_using_process():
    # Start time
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # To starat executing process
    p1.start()
    p2.start()

    # Join method pause execution on the main process by 'joining' all of our started process.
    p1.join()
    p2.join()

    finish = time.perf_counter()
    # Actual time
    actual_time = round(finish-start, 2)
    print(f'finished in {actual_time} second(s)')


def call_do_something_fn_with_args_using_process():
    # Start time
    start = time.perf_counter()

    # crating and Calling process in loop
    processes = []
    """
    Tip:
    using underscore is because we actually not using the loop index or value
    for _ in range(10):
    """
    # process creation and starting
    for i in range(5):
        t = multiprocessing.Process(target=do_something_with_args, args=[1.5, "Process-"+str(i)])
        t.start()
        processes.append(t)
    
    # Calling join methods for the created process to stop executing the below line until all the process get finished.
    for process in processes:
        process.join()

    # Finish time
    finish = time.perf_counter()
    # Actual time
    actual_time = round(finish-start, 2)
    print(f'finished in {actual_time} second(s)')


if __name__ == "__main__":
    """
    o/p:
 
    """
    # call_do_something_in_sync_manner()

    """
    O/P:
    If we don't use process join:
        

        Question: why finished in 0.0 second(s)?
            (Ans): Both process(p1, p2) started and while the process were sleeping,
             our scripts ran concurrently and continued on with rest of the script. so immediately it came down and calculated the finish time.

    (Q): What if we want to finish the process job before we calculated the finish time?
        (A): Use process join method. p1.join() , p2.join()
        o/p:
        

    """
    # call_do_something_fn_using_process()

    """
    O/P:
        
    """
    call_do_something_fn_with_args_using_process()
