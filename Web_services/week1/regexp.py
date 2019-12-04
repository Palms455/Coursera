def calculate(data, findall):
    matches = findall(r"\w?([abc])([-+]?)=([abc]?)([-+]?\d+)?")

    for v1, s, v2, n in matches:
        p = 0
        if s == '-':
            s = -1
            p = 1
        elif s == '+':
            s = 1
            p = 1
        else:
            s = 1
        data[v1] = data[v1] * p + (data.get(v2, 0) + int(n or 0)) * s
    return data