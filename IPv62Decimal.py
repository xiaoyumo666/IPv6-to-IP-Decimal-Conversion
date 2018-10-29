# !/usr/bin/python
# -*- coding: utf-8 -*-


def num_to_ipv6(num):
    hexstr = (hex(int(num)))[2:].replace('L', '')
    lack = 32 - len(hexstr)
    hexstr = '0' * lack + hexstr
    ipv6 = (hexstr[0:4] + ":" + hexstr[4:8] + ":" + hexstr[8:12] + ":" + hexstr[12:16] + ":"
            + hexstr[16:20] + ":" + hexstr[20:24] + ":" + hexstr[24:28] + ":" + hexstr[28:])
    return ipv6


def ipv6_to_num(ipv6):
    if len(ipv6) == 39:
        num = int(ipv6.replace(':', ''), 16)
    else:
        hexstr = ''
        ipv6 = ipv6.replace('::', (':0000:' * (8 - len([i for i in ipv6.split(':') if i != '']))).replace('::', ':'))
        for sub in [i for i in ipv6.split(':') if i != '']:
            hexstr += ('0' * (4 - len(sub)) + sub)
        num = int(hexstr.replace(':', ''), 16)
    return num


def main():
    ipv6 = num_to_ipv6(47874072285809707943700813380688281601)
    print ipv6  # 2404:3600:0:1::1
    num = ipv6_to_num("2001:c18:dc00:2::114")
    print num  # 42540733520453689120528949304241422612


if __name__ == '__main__':
    main()
