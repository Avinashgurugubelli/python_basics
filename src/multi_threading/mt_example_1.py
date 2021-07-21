"""
Older and manual way of creating the multi threading
"""

import time

import threading


def do_something():
    print('Sleeping 1 second ...')
    time.sleep(1)
    print('Done Sleeping ....')


def do_something_with_args(sleep_seconds, thread_name=None):
    print(
        f'Sleeping the thread {thread_name}, for {sleep_seconds} second(s) ...')
    time.sleep(sleep_seconds)
    print(f'{thread_name} Sleeping done ....')


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


def call_do_something_fn_using_threads():
    # Start time
    start = time.perf_counter()
    t1 = threading.Thread(target=do_something)
    t2 = threading.Thread(target=do_something)

    # To starat executing threads
    t1.start()
    t2.start()

    # Join method pause execution on the main thread by 'joining' all of our started threads.
    t1.join()
    t2.join()

    finish = time.perf_counter()
    # Actual time
    actual_time = round(finish-start, 2)
    print(f'finished in {actual_time} second(s)')


def call_do_something_fn_with_args_using_threads():
    # Start time
    start = time.perf_counter()

    # crating and Calling threads in loop
    threads = []
    """
    Tip:
    using underscore is because we actually not using the loop index or value
    for _ in range(10):
    """
    # Thread creation and starting
    for i in range(10):
        t = threading.Thread(target=do_something_with_args, args=[1.5, "Thread-"+str(i)])
        t.start()
        threads.append(t)
    
    # Calling join methods for the created threads to stop executing the below line until all the threads get finished.
    for thread in threads:
        thread.join()

    # Finish time
    finish = time.perf_counter()
    # Actual time
    actual_time = round(finish-start, 2)
    print(f'finished in {actual_time} second(s)')


if __name__ == "__main__":
    """
    o/p:
    Sleeping 1 second
    Done Sleeping ....
    Sleeping 1 second
    Done Sleeping ....
    finished in 2.02 second(s)
    """
    # call_do_something_in_sync_manner()

    """
    O/P:
    If we don't use thread join:
        Sleeping 1 second
        Sleeping 1 second        
        finished in 0.0 second(s)
        Done Sleeping ....
        Done Sleeping ....

        Question: why finished in 0.0 second(s)?
            (Ans): Both threads(t1, t2) started and while the threads were sleeping,
             our scripts ran concurrently and continued on with rest of the script. so immediately it came down and calculated the finish time.

    (Q): What if we want to finish the threads job before we calculated the finish time?
        (A): Use thread join method. t1.join() , t2.join()
        o/p:
        Sleeping 1 second
        Sleeping 1 second
        Done Sleeping ....
        Done Sleeping ....
        finished in 1.01 second(s)

    """
    # call_do_something_fn_using_threads()

    """
    O/P:
        Sleeping the thread Thread-0, for 1.5 second(s) ...
        Sleeping the thread Thread-1, for 1.5 second(s) ...
        Sleeping the thread Thread-2, for 1.5 second(s) ...
        Sleeping the thread Thread-3, for 1.5 second(s) ...
        Sleeping the thread Thread-4, for 1.5 second(s) ...
        Sleeping the thread Thread-5, for 1.5 second(s) ...
        Sleeping the thread Thread-6, for 1.5 second(s) ...
        Sleeping the thread Thread-7, for 1.5 second(s) ...
        Sleeping the thread Thread-8, for 1.5 second(s) ...
        Sleeping the thread Thread-9, for 1.5 second(s) ...
        Thread-7 Sleeping done ....
        Thread-4 Sleeping done ....
        Thread-0 Sleeping done ....
        Thread-9 Sleeping done ....
        Thread-2 Sleeping done ....
        Thread-5 Sleeping done ....
        Thread-6 Sleeping done ....
        Thread-8 Sleeping done ....
        Thread-1 Sleeping done ....
        Thread-3 Sleeping done ....
    """
    call_do_something_fn_with_args_using_threads()
