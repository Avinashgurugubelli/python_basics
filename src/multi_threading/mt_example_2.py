"""
newer way and faster way of creating threads.

In python 3.2 the feature added called "Thread pool executor" and in lot of cases this is the easier and more efficient to run these threads.
And it also allows to easily switch over to multiple processes instead of threads as well depending on the problem we trying to solve.

"""
import re
import time
import concurrent.futures


def do_something(sleep_seconds=1, thread_name=None) -> str:
    thread_name = thread_name if thread_name else f"Thread-{str(sleep_seconds)}"
    print(
        f'Sleeping the thread {thread_name}, for {sleep_seconds} second(s) ...')
    time.sleep(sleep_seconds)
    return f'{thread_name } Sleeping done ....'


def multi_thread_using_context():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start = time.perf_counter()

        t1 = executor.submit(do_something, 1, "thread-1")
        t2 = executor.submit(do_something, 1, "thread-2")

        print(t1.result())
        print(t2.result())

        finish = time.perf_counter()
        # Actual time
        actual_time = round(finish-start, 2)
        print(f'finished in {actual_time} second(s)')


def multi_thread_get_result_using_loop():
    with concurrent.futures.ThreadPoolExecutor() as executor:

        start = time.perf_counter()

        sleep_seconds = [5, 4, 3, 2, 1]

        """
        Using general Loop:

        futures = []
        for i in sleep_seconds:
            futures.append(executor.submit(do_something, i, f'Thread-{i}'))
        
        for f in concurrent.futures.as_completed(futures):
            print(f.result())
        """

        # The same general for loop can be written using LIST comprehension.
        futures = [executor.submit(
            do_something, sec, f'Thread-{sec}') for sec in sleep_seconds]

        """
        An iterator over the given futures that yields each as it completes.
        # Using plain for loop:
          for f in futures:
              print(f.result())
        Returns:
        --------
        An iterator that yields the given Futures as they complete (finished or
        cancelled). If any given Futures are duplicated, they will be returned
        once.
        """
        for f in concurrent.futures.as_completed(futures):
            print(f.result())

        finish = time.perf_counter()
        # Actual time
        actual_time = round(finish-start, 2)
        print(f'finished in {actual_time} second(s)')


def multi_thread_get_result_using_map():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start = time.perf_counter()
        sleep_seconds = [5, 4, 3, 2, 1]
        """
        An iterator equivalent to: python map(func, *iterables) but the calls may be evaluated out-of-order

        map Directly returns the results, instead of futures like we see in threads using loop.
        """
        results = executor.map(do_something, sleep_seconds)

        for result in results:
            print(result)

        finish = time.perf_counter()
        # Actual time
        actual_time = round(finish-start, 2)
        print(f'finished in {actual_time} second(s)')


if __name__ == "__main__":
    """
    O/P:
    ---

    Sleeping the thread thread-1, for 1 second(s) ...
    Sleeping the thread thread-2, for 1 second(s) ...
    thread-1 Sleeping done ....
    thread-2 Sleeping done ....
    finished in 1.01 second(s)
    """
    # multi_thread_using_context()

    """
    Yields the results as they complete (finished or cancelled)

    O/P:
    -----

    Sleeping the thread Thread-5, for 5 second(s) ...
    Sleeping the thread Thread-4, for 4 second(s) ...
    Sleeping the thread Thread-3, for 3 second(s) ...
    Sleeping the thread Thread-2, for 2 second(s) ...
    Sleeping the thread Thread-1, for 1 second(s) ...
    Thread-1 Sleeping done ....
    Thread-2 Sleeping done ....
    Thread-3 Sleeping done ....
    Thread-4 Sleeping done ....
    Thread-5 Sleeping done ....
    finished in 5.01 second(s)
    """
    # multi_thread_get_result_using_loop()

    """
    Yields the results as they created.
    
    O/P:
    ---

    Sleeping the thread Thread-5, for 5 second(s) ...
    Sleeping the thread Thread-4, for 4 second(s) ...
    Sleeping the thread Thread-3, for 3 second(s) ...
    Sleeping the thread Thread-2, for 2 second(s) ...
    Sleeping the thread Thread-1, for 1 second(s) ...
    Thread-5 Sleeping done ....
    Thread-4 Sleeping done ....
    Thread-3 Sleeping done ....
    Thread-2 Sleeping done ....
    Thread-1 Sleeping done ....
    finished in 5.01 second(s)
    """
    multi_thread_get_result_using_map()
