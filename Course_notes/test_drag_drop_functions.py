# ##     WORKING!!!               TEST 16.Create 2 lists with 'e' and without at the end of words Drag & drop function: 
color_list = ['red', 'orange', 'blue', 'brown', 'green', 'white']

end_letter = 'e'
with_e = [x for x in color_list if x.endswith(end_letter)]
without_e = [x for x in color_list if x not in with_e]
print(f"{with_e}")
print(f"{without_e}")
## WORKING !!!                                      TEST 1. вычислить sum in list через функцию drag & drop     
list_first = [[11, 2, 3], [44,5,6], [10,1,2], [17, 8, 6]]
def findingMaxSumItem(list_first):
    maxi = 0
    sum = 0
    for x in list_first:
        for y in x:
            sum +=y
            maxi = max(sum, maxi)
        sum = max(sum, maxi)
    return sum

print(findingMaxSumItem(list_first))
# ###############    !!! NEEDS TO BE SOLVED     TEST 7. drag & drop function return dictionary key=symbols, values=count
def count_symbols():    # working as in test for condition     !!! NEEDS TO BE SOLVED ACCORDING TO THE INSTRACTIONS
    word = 'hhjuiiiijjj'
    result = {}
    for symbol in word:
        result[word] = symbol.count(word)
        result[symbol] = word.count(symbol)
        return result
    if type(word) != str: 
        return False
print(count_symbols())
################################################################