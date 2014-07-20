import random, sys

wordList = './wordlist.txt'


def generate(wordList, n, domain):
    lines   = open(wordList).read().splitlines()
    samples = random.sample(lines, n)

    for sample in samples:
        print '%s.%s' % (sample, domain)

def usage():
    print "Usage : python hostgenerator.py [number of hostnames] [domain]"
    print "Example : python hostgenerator.py 4 dog.com"

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        usage()
        sys.exit(1)

    try:
        n      = int(sys.argv[1])
        domain = sys.argv[2]
    except:
        usage()
        sys.exit(1)
    generate(wordList, n, domain)