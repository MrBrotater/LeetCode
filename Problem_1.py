from typing import List

# NOTES:
# 1) try using binary to represent the combinations
# 2) try working backwards by factorizing the target value first, then comparing to the data

test_names = [
            'test 1'#,
            # 'test 2',
            # 'test 3',
            # 'test 4',
            # 'test 5'
        ]

test_cases = {
            'test 1': [[2, 7, 11, 15], 9, [0, 1]],
            'test 2': [[3, 2, 4], 6, [1, 2]],
            'test 3': [[3, 3], 6, [0, 1]],
            'test 4': [[0, 4, 3, 0], 0, [0, 3]],
            'test 5': [[-3, 4, 3, 90], 0, [0, 2]]
        }

def test():

    for name in test_names:
        print('beginning', name, '------------------------------------------')
        result = Solution.twoSum(0, test_cases[name][0], test_cases[name][1])
        if result == test_cases[name][2]:
            print(f'{name} passed! {result} == {test_cases[name][2]}')
        else:
            print(f'{name} failed! {result} != {test_cases[name][2]}')


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output = []

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

