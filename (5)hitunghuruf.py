def hitung_huruf(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

print(hitung_huruf("banana"))
print(hitung_huruf("hello"))