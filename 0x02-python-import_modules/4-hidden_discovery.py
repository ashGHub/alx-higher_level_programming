#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    md = dir(hidden_4)
    for i in range(len(md)):
        if (md[i][0] != '_'):
            print(md[i])
