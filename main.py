from numseq.fib import fib
import numseq.geo as geo
import numseq.prime as prime
import timeit


def main():
    print ("Fibonacci")
    for i in range(10):
        print ("{}: {}".format(i, fib(i)))

    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print ("{}: {} {} {}".format(i, geo.square(i), geo.triangle(i), geo.cube(i)))

    print ("Primes")
    prime_list = prime.primes(1000)
    for p in prime_list[-10:]:
        print (p)
    print ("Is 999981 prime? {}".format(prime.is_prime(999981)))
    print ("Is 999983 prime? {}".format(prime.is_prime(999983)))

if __name__ == "__main__":
    main()
    t = timeit.Timer(stmt='pass', setup='pass')
    print('It took this file {} seconds to run!'.format(t.timeit()))