# ==========================
# === 入力
# ==========================
# input()を早くする
import sys
input = sys.stdin.readline   # 改行が削除されないので文字列を受け取る時には注意する

# 整数 1 つ
N = int(input())

# 整数複数個
N, K = map(int, input().split())

# 整数 N 個 (スペース区切り)
A = list(map(int, input().split()))

# 整数 N 個 (改行区切り)
L = [int(input()) for i in range(N)]

# 整数 (縦 H 横 W の行列)
S = [list(map(int, input().split())) for i in range(H)]

# ==========================
# === 標準出力
# ==========================
# リストをスペース区切りで出力
arr = [1, 2, 3]
print(*arr)

# リストを改行区切りで出力
arr = [1, 2, 3]
print(*arr, sep="\n")

# 最後に改行を入れない出力
print("あああ", end="")

# ==========================
# === 処理の終了
# ==========================
exit()

# ==========================
# === ソート
# ==========================
from operator import itemgetter
from numpy.random import random
a = [[random(), random(), random()] for i in range(10**6)]
a.sort(key=itemgetter(1))

# ==========================
# === List
# ==========================
s = []
s.append(1)   # [] -> [1]
s.append(2)   # [1] -> [1, 2]
s.pop()       # [1, 2] -> [1]
s.pop()       # [1] -> []

q = []
q.append(1)   # [] -> [1]
q.append(2)   # [1] -> [1, 2]
q.pop(0)      # [1, 2] -> [2]
q.pop(0)      # [2] -> []

# ==========================
# === Set
# ==========================
d = set()
d.add(1)   # {} -> {1}
d.update({2, 3})   # {1} -> {1, 2, 3}, d |= {2, 3} は等価
d.intersection_update({1, 2})   # {1, 2, 3} -> {1, 2}, d &= {1, 2}は等価

# ==========================
# === Deque
# ==========================
from collections import deque
s = deque()       # deque([])
s.appendleft(1)   # deque([1])
s.appendleft(2)   # deque([2, 1])
s.popleft()       # deque([1])
s.append(3)       # deque([1, 3])
s.pop()           # deque([1])