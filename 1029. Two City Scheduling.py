def twocityscheduling(costs):
    A = sorted(costs, key=lambda item: item[0])
    for i in range(len(costs) // 2):


if __name__ == '__main__':
    c = [[10, 20], [30, 200], [400, 50], [30, 20]]
    print(twocityscheduling(c))
