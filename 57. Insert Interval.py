# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def solution(intervals, newInterval):
    ans = []
    ith = None
    for i in range(len(intervals)):
        if intervals[i].end < newInterval.start:
            ans.append(intervals[i])
        else:
            if newInterval.start < intervals[i].start:
                ith = i
                break
            newInterval.start = intervals[i].start
            ith = i
            break
    if ith == None:
        ans.append(newInterval)
        return ans
    for j in range(ith, len(intervals)):
        if newInterval.end > intervals[j].end:
            ith += 1
            continue
        elif newInterval.end < intervals[j].end and newInterval.end < intervals[j].start:
            break
        elif newInterval.end <= intervals[j].end and newInterval.end >= intervals[j].start:
            newInterval.end = intervals[j].end
            ith = j
            break

    ans.append(newInterval)
    if len(ans) > 1:
        return ans + intervals[ith+1:]
    return ans + intervals[ith:]

if __name__ == '__main__':
    l = [[1,2],[3,5],[6,7],[8,10],[12,16]]

    intervals = []
    new_i = Interval(4, 8)
    for i in l:
        intervals.append(Interval(i[0], i[1]))

    result = solution(intervals, new_i)
    for i in result:
        print(i.start, i.end)

def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
    ans = []
    ith = None
    for i in range(len(intervals)):
        if intervals[i].end < newInterval.start:
            ans.append(intervals[i])
        else:
            if newInterval.start < intervals[i].start:
                ith = i
                break
            newInterval.start = intervals[i].start
            ith = i
            break
    if ith == None:
        ans.append(newInterval)
        return ans
    for j in range(ith, len(intervals)):
        if newInterval.end > intervals[j].end:
            ith += 1
            continue
        elif newInterval.end < intervals[j].end and newInterval.end < intervals[j].start:
            break
        elif newInterval.end <= intervals[j].end and newInterval.end >= intervals[j].start:
            newInterval.end = intervals[j].end
            ith = j
            break

    ans.append(newInterval)
    if len(ans) > 1:
        return ans + intervals[ith+1:]
    return ans + intervals[ith:]
        #         ans = []
#         insert_start = Interval[0]
#         insert_end = Interval[1]
#         ith = None
#         for i in range(len(intervals)):
#             if intervals[i][1] < insert_start:
#                 ans.append(intervals[i])
#             else:
#                 insert_start = intervals[i][0]
#                 ith = i
#                 break

#         for j in range(ith, len(intervals)):
#             if insert_end <= intervals[j][1] and insert_end >= intervals[j][0]:
#                 insert_end = intervals[j][1]

#                 ith = j

#         ans.append([insert_start, insert_end])
