from day09.compressed_string import CompressedString

with open('input.txt') as f:
    text = f.read().replace('\n', '')
    s = CompressedString(text)
    print(len(s.decompress()))
