"""currency.py: Exchange one currency for another.
__author__ = "Haozhe Guo"
__pkuid__  = "1800011809"
__email__  = "guohz0528@pku.edu.cn"
"""


def getstr(curfrom, curto, amtfrom):
    """get a string from the url
    """
    from urllib.request import urlopen
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.format(curfrom, curto, amtfrom)
    request = urlopen(url)
    doc = request.read()
    request.close()
    str = doc.decode('ascii')
    return str


def tget():
    """test getstr
    """
    assert('{ "from" : "2.5 United States Dollars", "to" : "278.4975 Japanese Yen", "success" : true, "error" : "" }' == getstr('USD', 'JPY', '2.5'))


def explain(str):
    """translate the string
    """
    cut = str.split('"')
    if 'false' in cut[10]:
        if 'currency code is invalid.' in cut[13]:
            return cut[13][:-1]+' : Currency code should refer to a kind of current currency.'
        elif 'Currency amount is invalid.' == cut[13]:
            return 'Currency amount is invalid : Please input a proper number'
        else:
            return cut[13]
    else:
        return 'you can exchange '+cut[3]+' for '+cut[7]


def texp():
    """test explain
    """
    assert('you can exchange 2.5 United States Dollars for 278.4975 Japanese Yen' == explain(getstr('USD', 'JPY', '2.5')))
    assert('Source currency code is invalid : Currency code should refer to a kind of current currency.' == explain(getstr('ZZZ', 'JPY', '2.5')))


def exchange(curfrom, curto, amtfrom):
    """check the inputs and then exchange money
    """
    if len(curfrom) == len(curto) == 3 and curfrom.isupper() and curto.isupper():
        try:
            float(amtfrom)
            str = getstr(curfrom, curto, amtfrom)
            exchange = explain(str)
            return exchange
        except ValueError:
            return 'Currency amount is invalid : Currency amount should be an floating point number or an integer.'
    else:
        return 'Currency code is invalid : Currency code should be 3 capital letters that refers to a kind of currency.'


def texc():
    """test exchange
    """
    assert('you can exchange 2.5 United States Dollars for 278.4975 Japanese Yen' == exchange('USD', 'JPY', '2.5'))
    assert('Currency amount is invalid : Currency amount should be an floating point number or an integer.' == exchange('USD', 'JPY', 'aaa'))


def testall():
    """test all cases
    """
    tget()
    texp()
    texc()
    print("All tests passed")


def main():
    """main module
    """
    curfrom = input('the currency you want to exchange is ')
    curto = input('the currency you want to exchange for is ')
    amtfrom = input('the amount of the currency you want to exchange is ')

    testall()

    print(exchange(curfrom, curto, amtfrom))


if __name__ == '__main__':
    main()
