from time import clock, sleep

def wait_for_service(fn, *a):
    print 'Preparing service.',
    while True:
        try:
            start_time = clock()
            fn.service(*a)
            print
            break
        except Exception:
            if clock() - start_time > 10:
                # Probably a real error, not authentication
                raise
            print '.',
            sleep(1.0)
    print 'Ready for use!'
    return start_time
