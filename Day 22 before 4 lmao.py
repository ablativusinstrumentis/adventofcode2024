## lmaooooo 22 before 4 :skull:

nums = [int(i) for i in open("input2.txt","r").readlines()]

## is there a faster way considering all of the operations are powers of 2?
## yeah probably
## am i gonna spend time trying to find it?
## no :skull:
## bitwise is fast enough

total = 0
for i in nums:
    count = 0
    num = i
    while count<2000:
        ## pov me when i use ^ as the binary operation
        ## and then.
        ## try to use ^
        ## as a power
        ## in python
        ## jumping off a bridge
        num = ((num<<6) ^ num) & (2**24 - 1)
        num = ((num>>5) ^ num) & (2**24 - 1)
        num = ((num<<11) ^ num) & (2**24 - 1)
        count += 1
    total += num

print(total)

## part two
## bold of you to expect a part 2 sol from me, the guy whose middle name is "He Who Doesnt Finish What He Started"
