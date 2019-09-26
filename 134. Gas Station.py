class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        max_of_g = float("-inf")
        for i in range(len(gas)):
            if gas[i] > gas[max_of_g]:
                max_of_g = i

        min_of_c = float("inf")
        for i in range(len(cost)):
            if cost[i] > cost[min_of_c]:
                min_of_c = i

        pointer = None
        if max_of_g == min_of_c:
            pointer = max_of_g
        elif gas[max_of_g] - cost[max_of_g] > gas[min_of_c] - cost[min_of_c]:
            pointer = max_of_g
        else:
            pointer = min_of_c

        loop_invarient = len(gas)
        left_gas = gas[pointer] - cost[pointer]
        while loop_invarient >= 0:
            if pointer == len(gas) - 1:
                pointer = 0
                loop_invarient -= 1

            if left_gas - cost[pointer] < gas



if __name__ == '__main__':
    g =
    c =
    sol = Solution()
    print(sol.canCompleteCircuit(g, c))