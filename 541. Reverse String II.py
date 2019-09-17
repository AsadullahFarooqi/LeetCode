def reverseString(s, k):
    if len(s) < k:
        return s[::-1]
    elif len(s) < 2 * k:
        e = s[:k]
        return e[::-1] + s[k:]

    s = list(s)
    for i in range(0, len(s) + 1, k * 2):
        t = s[i:i + k]
        s[i:i + k] = t[::-1]

    print(i, len(s) - i, k)

    if len(s) - i >= k:
        e = s[i + k:]
        s[i + k:] = e[::-1]
        i += k
    
    print(len(s)/(2*k))
    
    e = s[i:]
    s[i:] = e[::-1]
    # elif :
    # len(s) - i < k:
    #     e = s[i + k:]
    #     s[i + k:] = e[::-1]

    return "".join(s)

if __name__ == '__main__':

    tests = {
        "bacdfeg":  ["abcdefg", 2],
        "bacd":     ["abcd", 2],
        "dcbaefg":  ["abcdefg", 4],
        "khlzvvxxcawgwkzgospzxuaahjaqagdfjkmyutvhxclzprhwjdlzltpzgfvjkcxvksocfugzqkpaxexezbvggtkoccgdrbxocrfopuviqsyirxvphvdtvrjtsbospmgyfduvnomqaadoizelpeuwxvnlsasxjszyjwjmvgdqgowjjtwdncagtnyfdemijulnrivnymtvyqujvehhvruiolfkeprqexloytdxzmmekuepamvdzpixatgsupvpidmeyifjyxkzxgxrhjsxgzlkthgnusvxdugqcdebukrarpkpqmusempvoiqimrtevfsiapxhsagalurdsyjgyjmkvavxorrmnxbijmndlpamzjkghkpzemxukivfxtmckskiwhdnuqpqrsrdhblmjigayoxjbinxxiuxpsjtuchzbdpaxommfvlbpxfnxqtrvnucarxhhdtnedckkzrbqanufaglncjqiwofanuzpgsbqmctdiqlhelajtbmfnpqyoaoglifareljluigqyxmjxptldmpdirpeztskuevtzdvatgzmqexrauywreoslyelecnqjfhiaiqypiyimdyofiaxjhdaamrvahbvoznsfvylzdlqsdjxoifistklnkdszqkqxkwjfrehqbhlaanbcvzljcgeiatmwbxfqpyyxmoxeslmpghirzsaprxdcbobfljsjvweksqcrgjwxhawpubvyyggozkvwwytrwpmuguclsedybyknwipajkkuwlhsrmsrgdqkhttbakooghbskiqleczmtwmfkhncetoxujrfcosysppmffnskvfabunfzsibqlfetpcsnpcthjznotsfrersnmqqphelpngnlnczritcjawskqlyxaeaprjutfhlwexisvzgciaemvodvcnqtuwcjdnxyvlwwmyfiqakikzjzmkgwwlauwiyiflgoahyaavkuobwuociwtldxlwztffmevdeaddxmvind": ["uxzpsogzkwgwacxxvvzlhkaahjaqagdfjkmyutvhxclzskvxckjvfgzptlzldjwhrpocfugzqkpaxexezbvggtkoxriysqivupofrcoxbrdgccvphvdtvrjtsbospmgyfduvaslnvxwuepleziodaaqmonsxjszyjwjmvgdqgowjjtwdmynvirnlujimedfyntgacntvyqujvehhvruiolfkeprqpzdvmapeukemmzxdtyolxeixatgsupvpidmeyifjyxkzudxvsunghtklzgxsjhrxgxgqcdebukrarpkpqmusempvulagashxpaisfvetrmiqiordsyjgyjmkvavxorrmnxbiikuxmezpkhgkjzmapldnmjvfxtmckskiwhdnuqpqrsrdspxuixxnibjxoyagijmlbhjtuchzbdpaxommfvlbpxfnzkkcdentdhhxracunvrtqxrbqanufaglncjqiwofanuznfmbtjalehlqidtcmqbsgppqyoaoglifareljluigqyxtveukstzepridpmdltpxjmzdvatgzmqexrauywreoslyoydmiyipyqiaihfjqncelefiaxjhdaamrvahbvoznsfvsdknlktsifioxjdsqldzlyzqkqxkwjfrehqbhlaanbcvxomxyypqfxbwmtaiegcjlzeslmpghirzsaprxdcbobflvbupwahxwjgrcqskewvjsjyyggozkvwwytrwpmuguclssmrshlwukkjapiwnkybydergdqkhttbakooghbskiqlesocfrjuxotecnhkfmwtmzcysppmffnskvfabunfzsibqrerfstonzjhtcpnscpteflsnmqqphelpngnlnczritcjxewlhftujrpaeaxylqkswaisvzgciaemvodvcnqtuwcjkmzjzkikaqifymwwlvyxndgwwlauwiyiflgoahyaavkudvemfftzwlxdltwicouwboeaddxmvind", 22],
        "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi": ["hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39]
    }

    for out, inp in tests.items():
        res = reverseString(*inp)
        sign = None
        if res == out:
            sign = "✅"
        else:
            sign = "❌"
        print(inp, "\t" + sign + "\n", "Solution Output: ",
              res, "\n", "Expected Output: ", out)
        print()
        if res != out:
            j = 0
            while j < len(out) and res[j] == out[j]:
                j += 1
            print(res[j:])
            print(out[j:])
