def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def pow(a, b):
    return a ** b

def main():
    while True:
        try:
            print(str(pow(2,3)))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except KeyboardInterrupt:
            print("oops")
        return 0

if __name__ == "__main__":
    main()