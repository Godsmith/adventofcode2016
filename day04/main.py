from day04 import Room

with open('input.txt') as f:
    lines = f.readlines()
    sum_ = 0
    for line in lines:
        r = Room(line)
        if r.is_real():
            sum_ += r.sector_id
            if 'pole' in r.real_name:
                print(r.real_name)
                print(r.sector_id)
    print(sum_)
