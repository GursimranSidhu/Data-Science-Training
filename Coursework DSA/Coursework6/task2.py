def simplifyPath(path):
    stack = []
    parts = path.split('/')

    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)


# ---- USER INPUT ----
path = input("Path= ")

print("Output:", simplifyPath(path))