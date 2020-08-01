# 插入排序
```Python3
def insert_sort(lists):
   # 将list的长度赋值给count
    count = len(lists)
    # 从1开始遍历list
    for i in range(1, count):
        # 将当前遍历的项的值赋值给key
        key = lists[i]
        # 将i-1的值赋值给j
        j = i - 1
        # 使用while循环，当j>=0时执行，即j的位置在list中执行
        while j >= 0:
            # 第一次进入时，因i=1，j=0，j为列表第一位，i为列表第二位，如果第一位大于第二位，让这两个数值交换位置，
            if lists[j] > key:
                lists[j + 1], lists[j] = lists[j], key
            #交换位置后让j-=1，等于是交换后的数值再与其前一位做判断
            j -= 1
    # 将最后的lists返回出去
    return lists

```

# 冒泡排序
```Python3
def bubble_sort(lists):
   # 将lists列表长度赋值给count
    count = len(lists)
    # 遍历lists中每一个位置
    for i in range(0, count):
        # 遍历当前项的下一项
        for j in range(i + 1, count):
            # 如果当前项的值小于下一项的值，则交换位置
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    # 将排序后的列表返回
    return lists
```
# 冒泡排序
```Python3
def bubble_sort(lists):
   # 将lists列表长度赋值给count
    count = len(lists)
    # 遍历lists中每一个位置
    for i in range(0, count):
        # 遍历当前项的下一项
        for j in range(i + 1, count):
            # 如果当前项的值小于下一项的值，则交换位置
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    # 将排序后的列表返回
    return lists
```
# 快速排序
```Python3
# 第一种实现方式
def quicksort(arr, left, right):
    # 只有left < right 排序
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)


def partition(arr, left, right):
    """找到基准位置, 并返回"""
    pivot_index = left
    pivot = arr[left]

    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            # 如果此处索引的值小于基准值, 基准值的位置后移一位
            # 并将后移一位的值和这个值交换, 让基准位置及之前的始终小于基准值
            pivot_index += 1
            if pivot_index != i:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
    # 将基准值移动到正确的位置
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    return pivot_index


if __name__ == '__main__':
    arr = [1, 3, 2, 4, 5, 7, 6, 8]
    print(arr)
    quicksort(arr, 0, len(arr) - 1)
    print(arr)


# 第二种实现方式
def quick_sort(list):
    if not list:
        return []
    pivot = list[0]
    less = [x for x in list[1:] if x <= pivot]
    bigger = [x for x in list[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(bigger)


a = [1, 3, 2, 4, 5, 7, 6, 8]
print(quick_sort(a))


# 第三种实现方式
def quick_sort(list):
    return [] if list == [] else quick_sort([x for x in list[1:] if x <= list[0]]) \
                                 + [list[0]] + quick_sort([x for x in list[1:] if x >= list[0]])


a = [1, 3, 2, 4, 5, 7, 6, 8]
print(quick_sort(a))
```

# 归并排序
```Python3
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)
```
# N 皇后位运算代码示例
```Python3

def totalNQueens(self, n): 
	if n < 1: return [] 
	self.count = 0 
	self.DFS(n, 0, 0, 0, 0) 
	return self.count
def DFS(self, n, row, cols, pie, na): 
	# recursion terminator 
	if row >= n: 
		self.count += 1 
		return
	bits = (~(cols | pie | na)) & ((1 << n) — 1)  # 得到当前所有的空位
	while bits: 
		p = bits & —bits # 取到最低位的1
		bits = bits & (bits — 1) # 表示在p位置上放入皇后
		self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1) 
        # 不需要revert  cols, pie, na 的状态

```
