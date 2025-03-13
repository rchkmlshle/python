class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(data, left_child, start, mid)
            self.build(data, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update_range(self, l, r, val):
        self._update_range(0, 0, self.n - 1, l, r, val)

    def _update_range(self, node, start, end, l, r, val):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0

        if start > end or start > r or end < l:
            return

        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * val
            if start != end:
                self.lazy[2 * node + 1] += val
                self.lazy[2 * node + 2] += val
            return

        mid = (start + end) // 2
        self._update_range(2 * node + 1, start, mid, l, r, val)
        self._update_range(2 * node + 2, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query_range(self, l, r):
        return self._query_range(0, 0, self.n - 1, l, r)

    def _query_range(self, node, start, end, l, r):
        if start > end or start > r or end < l:
            return 0

        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0

        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_query = self._query_range(2 * node + 1, start, mid, l, r)
        right_query = self._query_range(2 * node + 2, mid + 1, end, l, r)
        return left_query + right_query

# Example usage:
data = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(data)

# Update range [1, 3] by adding 3
seg_tree.update_range(1, 3, 3)

# Query range [1, 4]
result = seg_tree.query_range(1, 4)
print(result)  # Output should reflect the updated range
"""
Explanation
Initialization: The SegmentTree class is initialized with the input data array. The segment tree and lazy arrays are created with sizes four times the input array size to accommodate the tree structure.

Build Function: The build function constructs the segment tree by recursively dividing the array and storing the sum of segments.

Update Range: The update_range function updates a range of values by adding a specified value to each element in the range. It uses lazy propagation to defer updates to child nodes until necessary.

Query Range: The query_range function retrieves the sum of elements in a specified range. It also uses lazy propagation to ensure all updates

"""