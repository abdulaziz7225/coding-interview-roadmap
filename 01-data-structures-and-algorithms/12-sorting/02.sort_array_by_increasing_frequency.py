from typing import List


# Solution 1: Lambda function
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return sorted(nums, key=lambda x: (freq[x], -x))

# Time Complexity: O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * n) => O(n)


# Solution 2: Custom Merge Sort
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        self.custom_merge_sort(nums, 0, len(nums) - 1, freq)
        return nums

    def custom_merge_sort(self, array, left, right, freq):
        if left < right:
            middle = (left + right) // 2

            self.custom_merge_sort(array, left, middle, freq)
            self.custom_merge_sort(array, middle + 1, right, freq)

            self.custom_merge(array, left, middle, right, freq)

    def custom_merge(self, array, left, middle, right, freq):
        n1 = middle - left + 1
        n2 = right - middle

        left_array = array[left:middle + 1]
        right_array = array[middle + 1:right + 1]

        i = j = 0
        k = left
        while i < n1 and j < n2:
            if (freq[left_array[i]] < freq[right_array[j]]) or \
                    (freq[left_array[i]] == freq[right_array[j]] and left_array[i] > right_array[j]):
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < n1:
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < n2:
            array[k] = right_array[j]
            j += 1
            k += 1

# Time Complexity: O(n * log(n) + n) ==> O(n * log(n))
# Space Complexity: O(2 * n + log(n)) ==> O(n)
