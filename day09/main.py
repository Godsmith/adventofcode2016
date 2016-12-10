from day09.compressed_string import CompressedString, CompressedString2

with open('input.txt') as f:
    text = f.read().replace('\n', '')
    s = CompressedString(text)
    print(s.decompressed_length())
    s = CompressedString2(text)
    print(s.decompressed_length())
