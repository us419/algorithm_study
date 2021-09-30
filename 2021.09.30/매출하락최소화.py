# https://programmers.co.kr/learn/courses/30/lessons/72416

import collections

class Node:
    def __init__(self, val, int_children):
        self.val = val
        self.int_children = int_children
        self.children = []

def solution(sales, links):
    # graph 생성
    graph = collections.defaultdict(list)
    for link in links:
        graph[link[0]].append(link[1])
    
    # tree 구조로 변환
    head = Node(sales[0], graph[1])
    stack = [head]
    while stack:
        node = stack.pop()
        int_children = node.int_children
        for c in int_children:
            child = Node(sales[c-1], graph[c])
            node.children.append(child)
            stack.append(child)
            
    return min(minimun_sales(head))

def minimun_sales(node):
    children = node.children
    child_sales = []
    min_diff = 1e5
    for child in children:
        child_head_sum, child_min_sum = minimun_sales(child)
        child_sales.append(child_min_sum)
        if child_head_sum - child_min_sum < min_diff:
            min_diff = child_head_sum - child_min_sum
            
    head_sum = sum(child_sales) + node.val
    child_sum = 0 if min_diff == 1e5 else sum(child_sales) + min_diff
    min_sum = min(head_sum, child_sum)
    
    return [head_sum, min_sum]
    