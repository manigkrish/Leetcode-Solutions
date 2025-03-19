class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None  # Return None if input list is empty

        heap = []

        # Build a min-heap with first k elements
        for i in range(k):
            heapq.heappush(heap, nums[i])

        # Process the rest of the elements
        for j in range(k, len(nums)):
            if nums[j] > heap[0]:  # Compare with the smallest in the heap
                heapq.heappop(heap)  # Remove smallest
                heapq.heappush(heap, nums[j])  # Push the new element

        return heapq.heappop(heap)  # The root of the min-heap is the k-th largest element
