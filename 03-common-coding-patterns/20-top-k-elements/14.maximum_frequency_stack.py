class FreqStack:
    def __init__(self):
        self.freq_map = dict()
        self.freq_stack = dict()
        self.max_freq = 0

    def push(self, val: int) -> None:
        curr_freq = self.freq_map.get(val, 0) + 1
        self.freq_map[val] = curr_freq

        if curr_freq > self.max_freq:
            self.max_freq = curr_freq
            self.freq_stack[curr_freq] = []

        self.freq_stack[curr_freq].append(val)

    def pop(self) -> int:
        result = self.freq_stack[self.max_freq].pop()
        self.freq_map[result] -= 1

        if len(self.freq_stack[self.max_freq]) == 0:
            self.max_freq -= 1

        return result

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# Time Complexity:
# push(): O(1)
# pop(): O(1)
# Space Complexity: O(n)
