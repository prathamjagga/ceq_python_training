class Solution:
    attr1 = "I am attribute 1 "

    @staticmethod
    def func(a):
        print("hello")
        attr1 = a


obj1 = Solution()


obj1.attr1 = "Object 1"  ## instance attr
Solution.attr1 = "I am changed"  ## class attr

print(Solution.attr1)

print(obj1.attr1)

Solution.func(2)
print(Solution.attr1)
