def valid_ip(IP):

    if "." in IP:
        for i in IP.split("."):
            try:
                if int(i) > 255 or int(i) < 0:
                    return "Neither"
            except:
                continue
        return "IPv4"
    elif ":" in IP:
        for i in IP.split(":"):
            try:
                if len(i) == 0:
                    return "Neither"
                if len(i) > 1 and int(i, 16) == 0:
                    return "Neither"           
                elif len(i) == 1 and i != "0":
                    return "Neither"
            except:
                return "Neither"
        return "IPv6"
                
    return "Neither"


if __name__ == '__main__':
    # s = "2001:0db8:85a3::0:8A2E:0370:7334"
    s = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
    print(valid_ip(s))
