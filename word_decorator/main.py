

def decorator(text:str) -> str:
    _l = len(text)
    if _l < 1:
        return None, "Invalid Text"
    elif _l == 1:
        return "'%s'" % text, None

    return '"%s"' % text, None