from functools import lru_cache
class Solution:
    # Top-down Implementation
    # We are passing None to lru_cache which means the cache size is not limited
    # We are doing this because the number of states that will be re-used in this problem is large, and we don't want to evict a state early and have to re-calculate it.
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        # If we cannot schedule at least one job per day,
        # it is impossible to create a schedule
        if n < d:
            return -1

        hardest_job_remaining = [0] * n
        hardest_job = 0
        for i in range(n-1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty(i))
            hardest_job_remaining[i] = hardest_job

        @lru_cache(None)
        def dp(i, day):
            if day == d:
                return hardest_job_remaining[i]

            best = float('inf')
            hardest = 0
            for j in range(i, n - (d-day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest+dp(j+1, day+1))
            return best
        return dp(0,1)

    # To Do: Bottom-Up Implementation


