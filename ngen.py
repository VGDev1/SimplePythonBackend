import getopt, sys
from random import randint
import os

def main():
    size = 0
    output = ""
    numbers = []
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:n:", ["help", "output=", "number="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        print('ngen.py -o <outputfile> -n <list size>')
        sys.exit(2)
    for o, a in opts:
        if o == "-n":
            size = int(a)
        elif o in ("-h", "--help"):
            print('ngen.py -o <outputfile> -n <list size>')
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    
    for i in range(0, int(size)):
        numbers.append(randint(0, sys.maxsize))


    file1 = open(output, "w+")
    file1.write("[")
    for n in numbers:
        file1.write(str(n))
        file1.write(",")
    file1.write(str(sys.maxsize))
    file1.write("]")

    file1.close()


if __name__ == "__main__":
    main()