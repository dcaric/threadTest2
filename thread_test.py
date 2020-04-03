import threading
import time


def callback2(val):
    print("Val = {}".format(val))


def fun1(a, callback2):
    time.sleep(3)
    print "Working1 " + a
    callback2(123)


def fun2(name):
    time.sleep(1)
    print "Working2 " + name


def main():
    t1 = threading.Thread(target=fun1, args=('12', callback2))
    #t2 = threading.Thread(target=fun2, args=('Mile',))
    t1.start()
    #t2.start()
    t1.join()
    #t2.join()
    print "END"


if __name__ == '__main__':
    main()
