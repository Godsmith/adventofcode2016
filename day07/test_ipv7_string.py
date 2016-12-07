from day07.ipv7_string import Ipv7String


def test_strings_outside_brackets():
    assert Ipv7String('abba[mnop]qrst[uvwx]yz')._strings_outside_brackets == ['abba', 'qrst', 'yz']


def test_strings_inside_brackets():
    assert Ipv7String('abba[mnop]qrst[uvwx]yz')._strings_inside_brackets == ['mnop', 'uvwx']


def test_contains_abba():
    assert Ipv7String._contains_abba('abba')
    assert Ipv7String._contains_abba('sdfsabbafdfd')
    assert not Ipv7String._contains_abba('aaaa')


def test_contains_abba_outside_brackets():
    assert Ipv7String('abbaf')._contains_abba_outside_brackets()
    assert Ipv7String('abba[mnop]qrst[uvwx]yz')._contains_abba_outside_brackets()
    assert Ipv7String('aba[mnop]qrst[uvwx]zyyz')._contains_abba_outside_brackets()
    assert not Ipv7String('asa')._contains_abba_outside_brackets()
    assert not Ipv7String('aba[mnop]qrst[uvwx]xyyz')._contains_abba_outside_brackets()


def test_supports_tls():
    assert Ipv7String('abba[mnop]qrst').supports_tls()
    assert not Ipv7String('abcd[bddb]xyyx').supports_tls()
    assert not Ipv7String('aaaa[qwer]tyui').supports_tls()
    assert Ipv7String('ioxxoj[asdfgh]zxcvbn').supports_tls()
