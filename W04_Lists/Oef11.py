#oef 11
listA= [2,5,8,85,41]
listB = [1,5,3,41,12]

def get_gem_elements(list1, list2):
    temp_list = []
    for element in list1:
        if(element in list2) and not(element in temp_list):
            temp_list.append(element)
        else:
            temp_list = temp_list

    return temp_list



result = get_gem_elements(listA, listB)
print(result)