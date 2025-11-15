# Fungsi untuk menghitung kemunculan setiap karakter dalam string
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)

# Contoh penggunaan
count_characters("banana")
count_characters("hello")
count_characters("programming")
count_characters("data science")
count_characters("abracadabra")