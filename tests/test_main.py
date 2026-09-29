from homework.main import calculate_hashes


def test_calculate_hashes():
    text = "Hello, world!"

    md5_hash, sha256_hash = calculate_hashes(text)

    assert md5_hash == "6cd3556deb0da54bca060b4c39479839"
    assert sha256_hash == "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3"

