# def biggieSize(list):
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = 'big'
#     print(list)
#     return list        
# biggieSize([1,2,-3])



# def countPositives(list):
#     count = 0

#     for i in range(len(list)):
#         if list[i] > 0:
#             count = count + 1
#             print(count)
    
#     list[len(list) - 1] = count
#     print(list)
#     return list        
# countPositives([-1,1,1,1,-2,5])



# def sum_list(list):
#     sum = 0
#     for x in range(len(list)):
#         sum += list[x]
#     print(sum)
#     return sum
# sum_list([1,2,3,4])



# def avg_list(list):
#     sum = 0
#     for x in range(len(list)):
#         sum += list[x]

#     avg = sum/len(list)
#     print(avg)
#     return avg
# avg_list([1,2,3,4])


# def lengthlist(list):


#     length = len(list)
#     print(length)
#     return length
# lengthlist([1,2,3,4])


# def min(list):
#     min = list[0]

#     if len(list) < 1:
#         print("false!!")
#         return False
#     else:
#         for i in range(len(list)):
#             if list[i] < min:
#                 min = list[i]
#         print(min)
#         return min        
# min([1,3,2,5,7,8,6])


# def max(list):
#     max = list[0]

#     if len(list) < 1:
#         print("false!!")
#         return False
#     else:
#         for i in range(len(list)):
#             if list[i] > max:
#                 max = list[i]
#         print(max)
#         return max        
# max([1,3,2,5,7,8,6])




# def ultAnalyzer(list):
#     dict = {
#         "sumTotal":'0',
#         "average":'0',
#         "minimum":'0',
#         "maximum":'0',
#         "lenlist":'0',

#     }

#     def sum_list(list):
#         sum = 0
#         for x in range(len(list)):
#             sum += list[x]
#         print(sum)
#         dict['sumTotal'] = sum


#     def avg_list(list):
#         sum = 0
#         for x in range(len(list)):
#             sum += list[x]
#         avg = sum/len(list)
#         print(avg)
#         dict['average'] = avg
    
#     def min(list):
#         min = list[0]
#         if len(list) < 1:
#             print("false!!")
#             return False
#         else:
#             for i in range(len(list)):
#                 if list[i] < min:
#                     min = list[i]
#             dict['minimum'] = min 
#             print(min)

#     def max(list):
#         max = list[0]

#         if len(list) < 1:
#             print("false!!")
#             return False
#         else:
#             for i in range(len(list)):
#                 if list[i] > max:
#                     max = list[i]
#             dict['maximum'] = max      
#             print(max)

#     def lengthlist(list):
#         length = len(list)
#         dict['lenlist'] = length


#     sum_list(list)
#     avg_list(list)
#     min(list)
#     max(list)
#     lengthlist(list)

#     print(dict)
#     return(dict)


# def reverser(list):
#     list.reverse()
#     return(list)
