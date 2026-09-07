class Solution:
    def minMaxDist(self, stations, k):
        l = 0
        r = stations[-1] - stations[0]

        while r - l > 1e-6:
            mid = (l + r) / 2

            needed = 0

            for i in range(1, len(stations)):
                gap = stations[i] - stations[i - 1]
                needed += int(gap / mid)

                if gap % mid == 0:
                    needed -= 1

            if needed > k:
                l = mid
            else:
                r = mid

        return r
