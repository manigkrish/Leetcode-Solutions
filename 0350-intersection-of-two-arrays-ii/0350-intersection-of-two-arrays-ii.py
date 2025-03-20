class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        i, j = 0, 0
        intersect_list = []

        while i < len(sorted_nums1) and j < len(sorted_nums2):
            if sorted_nums1[i] < sorted_nums2[j]:
                i += 1
            elif sorted_nums2[j] < sorted_nums1[i]:
                j += 1
            else:
                intersect_list.append(sorted_nums1[i])
                i += 1
                j += 1

        return intersect_list