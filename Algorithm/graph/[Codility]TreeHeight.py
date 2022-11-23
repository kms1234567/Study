# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task

def solution(T):
    def dfs(node):
        if node == None:
            return -1
        height = 0
        height = max(dfs(node.l)+1, dfs(node.r)+1)
        return height

    return dfs(T)