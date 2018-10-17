#oef 13

def getallen_gelijk(list1, list2):
    #lengte
    if(len(list1) != len(list2)):
        return False
    else:
        list1.sort()
        list2.sort()
        for i in range(0,len(list1)):
            if(list1[i] != list2[i]): return False
            return True

print(getallen_gelijk([1,2,3,4,5], [1,2,3,4,5]))