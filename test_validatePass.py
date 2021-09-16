from validatePass import validatePass


def test_password_min_chars():
    assert validatePass("aG1!") == False

def test_password_max_chars():
    assert validatePass("abcdefghijklmN1!") == False

def test_password_capital():
    assert validatePass("abcdefg1!") == False

def test_password_digit():
    assert validatePass("abcdefgH!") == False

def test_password_non_alpha():
    assert validatePass("abcdefgH1") == False

def test_password_correct():
    assert validatePass("abcdefG1!") == True