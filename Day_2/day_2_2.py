def solve(reports):
    safe_reports = 0
    # report is safe iff:
    #   - it's only increasing or decreasing
    #   - adjacent values differ by at least 1, and at most 3.
    for report in reports:
        result = checkReport(report)
        if result == -1:
            safe_reports += 1 # add the report
        else:
            # Terrible O(n^2) solution but fuck it it's day 2.
            for i in range(len(report)):
                new_report = report.copy()
                del new_report[i]
                if checkReport(new_report) == -1:
                    safe_reports+=1
                    break
    print(safe_reports)


'''
Checks the report and returns either -1 showing the report is safe,
or any other number indicating the location of the bad level within the report
'''
def checkReport(report):
    increasing = report[0] < report[1]
    prev = report[0]
    for idx, item in enumerate(report):
        if idx == 0:
            continue # ignore the first level
        # first check slope
        if (prev < item) != increasing:
            return idx-1
        # now check distance
        if abs(prev - item) > 3:
            return idx-1
        if prev == item:
            return idx-1
        prev = item
    return -1



if __name__ == '__main__':
    # read each line, strip whitepace, convert to list of strings split off the inner space, map each of those strings to an int.
    reports = [list(map(int, l)) for l in [_.rstrip().split() for _ in open("input.txt",'r').readlines()]]
    solve(reports)