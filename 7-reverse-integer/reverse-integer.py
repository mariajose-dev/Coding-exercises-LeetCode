class Solution(object):
    def reverse(self, x):
        if(x>=-2**31 and x<=2**31-1):
            rev=0
            temp=x  #temporary variable
            if(x<0):
                x=x*-1 #convert the negative into positive
            while(x!=0):
                rem=x%10
                rev=rev*10+rem
                x=x//10
            if(rev>=-2**31 and rev<=2**31-1):
                if(temp>0):
                    return rev
                else:
                    return rev*-1  #return as negative number
            else:
                return 0
        else:
            return 0

        

        