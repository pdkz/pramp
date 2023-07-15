route = [
    [0,   2, 10],
    [3,   5,  0],
    [9,  20,  6],
    [10, 12, 15],
    [10, 10,  8]]

#output = 5
# i=0: energy=0
# i=1: energy = energy + route[1][2] = 10
# i=2: energy = energy - route[2][2] = 10 - 6 = 4
# i=3: energy = energy - route[3][2] = 4 - 15 = 9
# 差だけ考えると不足分がわからない

"""
(1)Subproblem 各ルート間で得られる・失う燃料を考える
deficit[0] = 0
deficit[1] = route[0][2] - route[1][2] = 10 - 0 = 10
deficit[2] = route[1][2] - route[2][2] = 0 - 6 = -6
deficit[3] = route[2][2] - route[3][2] = 6 - 15 = -9
deficit[4] = route[3][2] - route[4][2] = 15 - 8 = 7

(2)現在の燃料を保存する変数を用意
curr = 0
curr = curr + route[0][2] - route[1][2] = 0 + 10 - 0 = 10
curr = curr + route[1][2] - route[2][2] = 10 + 0 - 6 = 4
curr = curr + route[2][2] - route[3][2] = 4 + 6 - 15 = -5

もし curr が負になったら, それが不足分の燃料の値
最大値を更新する
"""
testcases = [
    [[0,1,19]],
    [[0,2,10],[10,10,8]],
    [[0,2,6],[10,10,20]],
    [[0,2,10],[3,5,0],[9,20,6],[10,12,15],[10,10,8]],
    [[0,2,10],[3,5,9],[9,20,6],[10,12,2],[10,10,10],[10,10,2]],
]

def calc_drone_min_energy_00(route):
    curr = 0
    max_deficit = float('-inf')

    for i in range(1, len(route)):
        curr = curr + (route[i-1][2] - route[i][2])
        if curr < 0:
            max_deficit = max(max_deficit, curr)
    max_deficit = (-1)*max_deficit
    print(max_deficit)

def calc_drone_min_energy_01(route):
    if len(route) < 2: return 0
    # 最初に 位置0 から上昇するので 最大燃料のインデックスは route[1]
    maxIdx = 1
    for i in range(1, len(route)):
        if route[i][2] > route[maxIdx][2]:
            maxIdx = i
            print(maxIdx)
    return max(route[maxIdx][2] - route[0][2], 0)

if __name__ == '__main__':
    calc_drone_min_energy_01(testcases[3])