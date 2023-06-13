#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    content = dir(hidden_4)
    x = sorted(name for name in content if not name.startswith("__"))
    for func in x:
        print(func)
