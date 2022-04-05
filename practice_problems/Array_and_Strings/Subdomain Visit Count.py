from collections import Counter

class Solution(object):
    # Time complexity O(N)
    # Space complexity O(N)
    def subdomainVisits(self, cpdomains):
        ans = Counter()

        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans['.'.join(frags[i:])] += count

        return ['{} {}'.format(ct, dm) for dm, ct in ans.items()]