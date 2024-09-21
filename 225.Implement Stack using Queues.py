#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] Implement Stack using Queues
#
from collections import deque


# @lc code=start
class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        while len(self.queue_in) > 1:
            self.queue_out.append(self.queue_in.popleft())
        result = self.queue_in.popleft()
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return result

    def top(self) -> int:
        if self.empty():
            return None
        while len(self.queue_in) > 1:
            self.queue_out.append(self.queue_in.popleft())
        ans = self.queue_in.popleft()
        self.queue_out.append(ans)
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return ans

    def empty(self) -> bool:
        return len(self.queue_in) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
