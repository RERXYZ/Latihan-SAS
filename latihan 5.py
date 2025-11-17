def count_characters(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    print(result)


# contoh penggunaan
count_characters("banana")  
count_characters("hello")   
