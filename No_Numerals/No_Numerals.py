msg = input().split()
res = ""
nums = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","10":"ten"}

for x in msg:
    res += nums[x] if x in nums else x
    res += " "

print(res,end="")
