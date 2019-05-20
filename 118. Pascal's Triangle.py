"""
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]
"""
def solution(numrows):

    for row in range(0, numrows+1):
        temp = []
        for cols in range(row):
            temp.append(row)
        print(temp)
if __name__ == '__main__':
    k = 5
    solution(k)
    # for i in solution(k):
    #     print(i)