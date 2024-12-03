def solve(reports):
    safe_reports = 0
    for report in reports:
        # report is safe iff:
        #   - it's only increasing or decreasing
        #   - adjacent values differ by at least 1, and at most 3.
        increasing = report[0] < report[1]
        prev = report[0]
        safe = True
        for item in report[1:]:
            # first check slope
            if (prev < item) != increasing:
                safe = False # slope changed
                break
            # now check distance
            if abs(prev - item) > 3:
                safe = False # too much change
                break
            if prev == item:
                safe = False # not enough change
                break
            prev = item
        safe_reports += 1 if safe else 0 # add the report if it's safe
    print(safe_reports)

    


if __name__ == '__main__':
    # read each line, strip whitepace, convert to list of strings split off the inner space, map each of those strings to an int.
    reports = [list(map(int, l)) for l in [_.rstrip().split() for _ in open("input.txt",'r').readlines()]]
    solve(reports)