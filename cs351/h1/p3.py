import sys

input = int(sys.argv[1])

twos = ~input + 1

print("{:032b} {}\n{:032b} {}".format(input,input,twos,twos))

