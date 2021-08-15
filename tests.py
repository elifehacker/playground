import unittest

def get_local_max(input):
    l = [input[x] for x in range(len(input)) if (x-1 >=0 and input[x] != input[x-1]) or x == 0]
    return [l[x] for x in range(len(l)) if l[x] == max(l[0 if x-1 <0 else x-1 : len(l) if x+2 > len(l) else x+2 ])]

class Test(unittest.TestCase):

    def test(self):
        input = [
            ([1,2,3,2,4],[3,4]),
            ([1,3,3,3,3,4], [4]),
            ([5,3,3,-1,3,4],[5,4]),
            ([1, 1.5, 2, 1.7, 3, 4, 3.7, 5],[2,4,5]),
            ([3, 1.5, 2, 1.7, 3, 4, 3.7, 5],[3,2,4,5]),
            ([3, 1.5, 2, 1.7, 3, 4, 3.7, 2.5],[3,2,4]),
            ([3, 1.5, 2, 1.7, 3, 3, 3, 3, 4, 3.7, 5],[3,2,4,5])
        ]
        for i in input:
            self.assertEqual(i[1], get_local_max(i[0]))

if __name__ == '__main__':
    unittest.main()