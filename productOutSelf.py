import random
#class ProductOutSelf(object):
def withoutself(nums):
    #input nums
    #output output

    MAX_INF = float('inf')
    MIN_INF = float('-inf')
    size = len(nums)
    if size == 0: return []
    if size == 1: return [0]

    output = [1]*size
    for idx in range(1, size):
        output[idx] = nums[idx-1]*output[idx-1]
        #check overflow
        if nums[idx-1] != 0 and output[idx]/nums[idx-1] != output[idx-1]:
            print nums, out
            output[idx] = None
            return None

    back_product = 1
    for idx in range(size-1,-1,-1):
        prev = output[idx]
        output[idx] = output[idx]*back_product
        #check overflow
        if prev != 0 and output[idx]/prev != back_product:
            output[idx] = None
            return None
        back_product *= nums[idx]
    return output

def testcase():

    # test case to test none value in array or larger value in array
    test_case = []
    num = 1
    for shift in xrange(19):
        result = withoutself(test_case)
        if not result: # return None value
            print test_case
        num = num << 1
        test_case.append(num)

    # test case to test large size of array
    SIZEOFARRAY = 1000000
    RANGEOFELE = 50
    test_case= []
    for count in xrange(SIZEOFARRAY):
        num = random.randint(-RANGEOFELE,RANGEOFELE) # some positive and negative elements
        test_case.append(num)
        if count/100 == 0: #test 100 elements, 200 elements, ... to SIZEOFARRAY
            result = withoutself(test_case)
            if not result: # return None value
                return test_case

    #test case 0
    test_case = [3,3,1,0,11]
    test_case = [0,0]
    if not result: # return None value
        print test_case

if __name__ == "__main__":
    #productAPI = ProductOutSelf();
    testcase()