def most_common_element(lst):
    previous = 0
    end_lib = {}
    list_nums = set(lst)
    list_nums = list(list_nums)
    end_dict = {}
    end_key = []
    for i in list_nums:
        end_dict[i] = lst.count(i)

    print(end_dict)

    value1 = max(end_dict.values())
    print(value1)
    for i,j in end_dict.items():
        if j == value1:
            end_key.append(i)

    max_val_key = max(end_key)
    print(end_key)
    print(max_val_key)
    print(end_lib[max_val_key])
    #print(end_lib[max_val_key])


list2 = [1,2,2,3,4,4,5,5,5,6,6,6]
most_common_element(list2)