#DAY3 ASSIGNMENT 2
for Number in range (1, 200):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '\n ')

#OUTPUT
        
##  2
##  3
##  5
##  7
##  11
##  13
##  17
##  19
##  23
##  29
##  31
##  37
##  41
##  43
##  47
##  53
##  59
##  61
##  67
##  71
##  73
##  79
##  83
##  89
##  97
##  101
##  103
##  107
##  109
##  113
