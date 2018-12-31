"""wcount.py: count words from an Internet file.
__author__ = "Haozhe Guo"
__pkuid__  = "1800011809"
__email__  = "guohz0528@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import collections

def nor(s):
    """normalize a string
    """
    if not s[-1].isalnum():
        try:
            s = s[0:-1]
            return nor(s)
        except IndexError:
            return
    elif not s[0].isalnum():
        try:
            s = s[1:]
            return nor(s)
        except IndexError:
            return
    else:
        return s

def main(web, n):
    """main module
    """
    url = urlopen(web)
    doc = url.read().decode().lower().split()
    doc = list(map(nor, doc))
    url.close()

    count = collections.Counter(doc)
    cts = [i for i in count.items()]
    cts.sort(key = lambda x:x[1])
    
    for i in range(1, n+1):
        print(cts[-i][0], ' '*(20-len(cts[-i][0])), cts[-i][1])


if __name__ == '__main__':
    length = len(sys.argv)
    if  length == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    elif length == 2:
        try:
            main(sys.argv[1], 10)
        except ValueError:
            print('Url Error: please input a proper url')
        except IndexError:
            print("Topn Error: topn number is bigger than the number words' kinds")
    else:
        try:
            n = int(sys.argv[2])
            try:
                main(sys.argv[1], n)
            except ValueError:
                print('ValueError: please input a proper url')
            except IndexError:
                print("Topn Error: topn number is bigger than the number words' kinds")
        except ValueError:
            print('Topn Error: please input a integer as topn')
