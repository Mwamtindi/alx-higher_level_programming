#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for h in dir(hidden_4):
        if h[:2] != "__":
            print("{:s}".format(h))
