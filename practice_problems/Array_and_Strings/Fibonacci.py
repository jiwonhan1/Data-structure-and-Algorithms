class Solution(object):
    def fibonacci(self, n):
        if n < 2:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    def fib(self, N):
        cache = {}
        def recur_fib(N):
            if N in cache:
                return cache[N]
            if N < 2:
                result = N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)
            cache[N] = result
            return result
        return recur_fib(N)