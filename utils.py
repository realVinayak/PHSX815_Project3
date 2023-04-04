'''
Contains utility functions for projects. Maybe reused
'''


def get_containing_interval_index(intervals, search_value):
    for interval_index in range(len(intervals) - 1):
        if search_value >= intervals[interval_index] and (
                search_value <= intervals[interval_index + 1]):
            return interval_index
    return -1

def get_meaned_interval(intervals):
    meaned_list = []
    for interval_index in range(len(intervals)-1):
        meaned_list.append((intervals[interval_index]+intervals[interval_index+1])/2)
    return meaned_list

if __name__ == '__main__':
    test_intervals = [1, 2, 5, 9, 10]
    print(get_containing_interval_index(test_intervals, 2.5))
    print(get_containing_interval_index(test_intervals, 9.5))
