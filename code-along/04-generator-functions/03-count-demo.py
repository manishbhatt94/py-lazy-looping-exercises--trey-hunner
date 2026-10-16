def count(n=0):
    print("start")
    while True:
        yield n
        n += 1
        print("loop")
    print("end")


def main():
    c = count()
    # Loop once
    print("First loop:")
    for x in c:
        print(x)
        if x > 3:
            break
    # Loop afain
    print("Second loop:")
    for x in c:
        print(x)
        if x > 3:
            break


if __name__ == '__main__':
    main()

