class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0

        for i in range(n):
            papers_with_at_least = n - i
            h = max(h, min(citations[i], papers_with_at_least))

        return h
