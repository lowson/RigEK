#!/usr/bin/python

import os, sys, getopt


def file_get_contents(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return data


def str_split_like_php(s, n):
    ret = []
    for i in range(0, len(s), n):
        ret.append(s[i:i+n])
    return ret


def main(argv):
    output = 'output.bin'
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print 'decoder.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'decoder.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
          input = arg
      elif opt in ("-o", "--ofile"):
          output = arg

    if not os.path.exists(input):
        print 'No such file or directory:', input
        sys.exit()

    stream = file_get_contents(input)
    stream = str_split_like_php(stream,1)

    s = [154, 3, 164, 45, 73, 234, 131, 156, 189, 36, 155, 107, 239, 88, 250, 143, 226, 167, 236, 7, 50, 102, 145, 132,
          232, 136, 108, 70, 157, 171, 2, 172, 101, 230, 127, 11, 186, 51, 200, 97, 168, 126, 81, 196, 4, 229, 23, 209,
          112, 104, 218, 254, 55, 221, 142, 74, 1, 116, 34, 207, 109, 32, 139, 17, 14, 52, 41, 169, 183, 110, 115, 130,
          111, 63, 175, 124, 244, 208, 249, 237, 178, 191, 161, 42, 96, 173, 86, 187, 133, 78, 59, 150, 195, 40, 48,
          120, 233, 243, 43, 153, 90, 83, 85, 84, 210, 235, 198, 67, 13, 38, 47, 77, 216, 188, 37, 135, 26, 5, 125, 128,
          147, 160, 57, 217, 247, 184, 72, 220, 194, 99, 68, 223, 149, 95, 100, 214, 21, 192, 121, 222, 166, 197, 152,
          119, 76, 252, 114, 162, 118, 146, 31, 46, 24, 177, 103, 251, 54, 33, 137, 56, 211, 255, 203, 231, 19, 80, 106,
          201, 240, 62, 75, 10, 238, 29, 6, 170, 28, 93, 92, 16, 253, 65, 245, 53, 163, 138, 27, 158, 49, 15, 180, 9,
          174, 206, 61, 205, 98, 242, 219, 30, 113, 35, 134, 64, 105, 215, 22, 202, 20, 122, 123, 60, 66, 176, 228, 140,
          89, 82, 18, 182, 39, 225, 179, 129, 213, 165, 0, 248, 91, 190, 199, 151, 8, 71, 212, 227, 148, 141, 185, 241,
          12, 181, 193, 224, 44, 94, 117, 204, 25, 79, 246, 58, 144, 69, 87, 159]

    slen = len(stream)
    rc = []
    x = 0
    y = 0
    for i in range(0,slen):
        x = (x + 1) % 256
        y = (y + s[x]) % 256
        s[x], s[y] = [s[y], s[x]]
        rc.append(chr((s[(s[x] + s[y]) % 256] ^ ord(stream[i])) % 256))

    data = ''.join(rc)
    file = open(output, "w")
    file.write(data)
    file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
