#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'


list1 = [8999, 1, 33, 44, 7667, 33, 644546, 2, 4444, 65, 43]


# 插入排序
def insert_sort(lists):
	# 列表长度
	count = len(lists)
	for i in range(1, count):    # 100 1-99 0-99
		key = lists[i]  # i指列表下表
		j = i - 1
		while j >= 0:
			if lists[j] > key:
				lists[j + 1] = lists[j]
				lists[j] = key
			j -= 1
	return lists

print('插入排序结果：', insert_sort(list1))


# 希尔排序
def shell_sort(lists):
	count = len(lists)
	# 增量缩减值 2倍
	step = 2
	# 初始增量值
	group = int(count / step)
	# print(group)
	while group > 0:
		for i in range(0, group):
			j = i + group
			while j < count:
				k = j - group
				key = lists[j]
				while k >= 0:
					if lists[k] > key:
						lists[k + group] = lists[k]
						lists[k] = key
					k -= group
				j += group
		group = int(group / step)
	return lists

print('希尔排序结果：', shell_sort(list1))

