# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        min_temp = self._data[i]
        left = 2 * i + 1
        right = 2 * i + 2
        if right < len(self._data):
            min_temp = min(min_temp, self._data[left], self._data[right])
            if min_temp == self._data[left]:
                self._data[i], self._data[left] = self._data[left], self._data[i]
                self._swaps.append((i, left))
                self.sift_down(left)
            elif min_temp == self._data[right]:
                self._data[i], self._data[right] = self._data[right], self._data[i]
                self._swaps.append((i, right))
                self.sift_down(right)
        elif left < len(self._data):
            min_temp = min(min_temp, self._data[left])
            if min_temp == self._data[left]:
                self._data[i], self._data[left] = self._data[left], self._data[i]
                self._swaps.append((i, left))
                self.sift_down(left)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
