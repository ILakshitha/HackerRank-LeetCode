class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        z=0
       
        negative = x<0
        x = abs(x)
        for i in range(len(str(x))):
            y = x % 10
            x = x // 10

            z = z*10 + y

        if z < -2**31 or z > 2**31 - 1:
            return 0 
        if(negative):    
            return -z
        else:
            return z
            