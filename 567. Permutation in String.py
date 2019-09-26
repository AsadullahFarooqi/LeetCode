from collections import Counter

def checkInclusion(s1, s2):
    s2_dict = [0] * 26
    s1_dict = [0] * 26

    for i in s1:
        s1_dict[ord(i) - ord("a")] += 1
    for i in range(len(s2)):
        s2_dict[ord(s2[i]) - ord("a")] += 1
        # print(s2_dict)

        if i >= len(s1):
            print(i, s2[i-len(s1)])
            s2_dict[ord(s2[i - len(s1)]) - ord("a")] -= 1
        if s1_dict == s2_dict:
            return True

    return False


if __name__ == '__main__':
    s1 = "hello"
    s2 = "ooolleoooleh"
    s1 = "lrxdxvfejdkrnjillizofhtcsnsaayremyicmvfsfuxvmlskswyfjwxdnotttdfisbfnoldsfaarpaesaltnvgrdoktdnxwgyblyshlhlubpeamxfrsfhtlcezzwsjtvcmzkpvfvmhphwksghfnzhbwogziokkkhgvrmndwsjjsegkdfobnecberwraetxwdxemzpoakgnovqpjgslmakuceqdorytxawxndpbkvsbalgfkreaplyrkbxwzfdlzsmoazxcmrmattzszqehtevafgiurhjbtfmztjgozkunklacupomjjafbzjerxlvgmnsjqcrsrbrcugaofbiuvibjmekhyddhwberuoaxfghtdgjwbjlziraohnmkhutuyftiptmdeshtyhrhtdkhgkzoxnulfqboeimlepwyihauwjsermzmefzlkubovxhrtkbfhopvhwuukkacivimrnjaxmpecncgxfelmcfgnqueelqssgpxpidtswwrrlusgwznwvuvdahajoxflexnctsgmjchtgfwlqsfyoamaaaowxttgshiszohczagbgpoqibghhawdjftrrgpuailqfpwzvytgwdyqfymihyuwhxzhawpoxafxvnwvkhwubjypxjnqjkfblpeoxewtjfnlgiwfkxuirhpbeyokyrbnmichszrsntbaxrdiznwfiokbuhkwvmhtunabqninaztpcvzptfjnhtxzjuupwvtsaateiuerftqjxqkljxkdindkrnsmuhouhpquabwanjeoyaheqgdkdyqsqdzlrdwyrakfdphasupvuhwvtsesrlubcapcdzutmiyyudpognnmmncgphgmfdozclwgvxhhsbxaexuenknayihkarjrbipmnujdfqfvvfbaickybuacyuutbarjsmveivscoktcpfzwlcjemengveudvdlcdjnpbjbimokldsbjlsdasbgjukkoeucwlhtmkxhbrnczapqhoyhrqaogbkeqsczwlloqiguclumiggrijlymcszkqnmgtzjcblnylpigzbwiynnwojnkyxnmgoodljmmqcprzznsmcruifltbdujttnpjnttlbfwlclgewsdcjgbtuzwsayatuqvmebtvihljkaewfnqbotnmkabcqsxbohqleqlrujvughzcurfuhmhfklbwbaudmyfttsikiwzbvlfwmetgsnxxlmjofrtfdfcsnqbyeecgzelovranroxccdaqyfqtkjxeqehjoeqytkaombdgfajafmvmqzzxfaiezovbzcyihaucpeopptarcwihwklrpvtkqnbbquqnlmdwygbtkstzwdznbevlyfivqflpacmtcsarbbkmenyijnjvwlixhmqrqrejwznxzdiqzrrfejxfmcdzmfkjvbwfmstilkrmvviywuquenujtcqbhkyxbnbbdoxgyjpxfucdmsecnzstjlsivelupyptdogsjepgjtwgoexaxjfduvkldfudwlxmnjyynypvdvgecyhflaiyrhbqmixmwgsehsfmxyjzvkioaexjbcnakbakbrvtwgghwhfsffnamcgphuqqxqvbdmfhrzxlgiunazqhfsxgxxwktpjicnmeaxyhyfauegcdiykhuouqqnybgxcazckmzriyzuulqeqtgjuawvissukncpataietvuwirkaifroelxsptnolduugufycgnvamsardwrueajvhqkkxkkhzphbuqbldukjdqcznwscvnnqnwxszplqyfuctorjcbucxgfctibwfxftrdliugohjgmbxqduvwgrdmmawyhfgkkbeojyxkoftuluolffjvygyzftmcuthegrxdkyegkucgnukwvyjqjeewteaivfoybrwaceyasgwxsznkjzwyfjoiqeclwlrnyqdxmzadkjvhjaeghfcaiyrjefpkyhslkeogzgijtdymtwcopbvhzcqficucdfzhndzddunzhnkmllhjrrjcvksisdphhmqcnsrlmyygxhlakemvncrogiljrtfyvdrujjwowwjxbjxpjhebvheexkniipvotlumxpjplncxsrezcxmyansqmarfwwtwngvcgqcijzrhvlwalkcdsrccschgudpahdvlunyzbrdfevmnoewvavrklwvfiilgtmtexwzfmgacugaalcxqeplsmpkplutliqairwtbytsxzlupqplbpadgsiuazxvrdwjzxpijvwytgmsocughjqwbsvozcfbflqgokqjdxrivnioxcgefxmkjajkwllqdcepegzzylflfqxclhsooylinxpalctbxsvbdjqmmcyqfgfytstbpmjgmqhmnnesgovyzwsatnvqallzdjrtetzdxhckykznmnuexzsfyncndzbqstxwppzjolipszefzxqoyjteoykmrympogufseghdqlvvipuwfzheescacwrbxkaqcutfrngmzmqxeeorppkjgdroxoqdkyaawrpcjtfxzlfgkrguphggygibcialnnkvlnevkbapazmpcguhmjcmizjsinmqjknavhumrdmjnbscndtfapztvczvhkpcowavszavfcwwlzdddpuliglnjucqziltqwlsibodwdcbmorwyyqcvwoesjibeqcgsbtcelowxtzryhvepjcqnpmigbdbuplezwgcqekhxzvsbwlaunotrhhmdrrfjoeyzwzygeypgpxonkzriqjsecoqdmeslcfgnzlwstigfxogzwrjznvgtrzjdvdiaofktlzpvnjftauzfmgigxuydyddabcucklupsjycdbdzdghkiryjrjuretnulfczhhwdoayrrvljbihhbmxvzyjxrwkpmxxephocpleznusehkxjgjqlalbgenuahcqzcbvnurwvtwvrvefnkdwywtokrxhstwwybamnixtlokktydnuqrnxylazddpvdbfhtevujagbvqkbjtcvedzrqpkwmxnsugrklcimmgbjmnatgmyyuvnbuffgjcvclkglhdwufxclndhyvoecrfqfxtmunjqavkrhyhlltnxwjsdzvkmxayxmgvsoaewlergrdaxssqtavrkazjkamfeyvttdytukwsqxrevtfquuanjywitzajgdlsgonmxjwxqiekadyohkzlowywqrmnydclodaichygaxhljvvlnbdpsweicfyntnxmaxotdnizxdfkhtnegosqynavfeludbsxylfpsxrnasizvozwlljokgirgewaskykpclgictznfysqmwpkyjntcvikxapgxupqewswsuqcnlajdndiujuwcfjkhysjltdbjjgxgnbovwzrcibzwasjoitdrpyureacgvdupxpzqepymwjxruyxkjhlsgiddghluhkomqmpzbucxryifzszpmknuakmbmieksazgsmzpuybfdlpqlilcqfewgqkywbianhzgizbgkruslhepkllojtoewgrhxmqlziexxfacuzjgvpgbusktkkctzyznwycsklkrrjrvbmxbhrhpwaketgqdubkavullzlhxdahukoajvrjfdmcltylxjllnwycvbcddpxidjzhkpwvlbrnxmnvseioujesuieatdxcptqprwaukeqdodaedzbwmybatapayautrbyayjxtnvcniqleohffgxgsogwslduzbpkaxtxwzstjftgriebrlthrhplhpqtglcjzoospsolqtofgjttxzpdceficxvxvzkfbptevvmjiviglepvhatglwgbeywcsgrqrttwjblyskptgwkhlyudcxolbkajzjeuvdbdourryxldpzlbfombingjbamxelfvqnusymtussovzxkyemigegqlqoprynkwuwhxmvkacwplrgsdxbcoykxbgfyfuclxcaxpzqgukwkbvrcmzvuzinucgryrnjvgysihixhcknpfgjmagmlpihnnbniksegyxybmgwsqgitctffwgudyvrkhnnuqczybxadjfzbakmrpzqgsfdtupbrhkyqumimuwwtwaugrpwppfcgpxkumziermyqqrihufxtfklmjsipuyimbrfatepkufdonqditpcnxbanfxfhmmwutomluagakhinnrnjwamaztgozkpwyxipxlellbszvgewelbwvkxxvrmtvuiivdgdfpwwuwvmxnewqkpoocwbzmpbscymmrbrtaazhpxvktdoukayngafglbvnmvstahrlsxwumubkeceevztlzwiyfiwtyuiyjbghofotfqpygwvgzlzieajohxtnfwfjtpezunhtezmgoijeullayhjlrklddeiujhukyhgvwhztrvrdcbxhuvgiwmjwetjmwzoipopdegynbwjbxblgkgcbeljnlmdogjlmfcebkpsdnojqxzgmmwprbvjnvghxqbozfmbfpohiwtmdzumxlgtspaodgmqrykogolwgvklwvcxuwqztapgggossaayeiyramtvoicssnfouddszofopvrmkhyihbiuabdzrxflubidzkorufphwqryyznzlcgffamyeacfjvdkoilbvurswxuwbfsgjqhsajbsbvzxwlsazxgfmnlilenuuowslmlrrbzpkmoelvhpvqdwuutwdsowwldmuwzvouqbynybgnvojeyzvpsyzyrmreeahzutgbgoinadnfnctsezjixjdqkrleovfjydtnndeuycghsuwioyqjpdwhqtgrazzbxfwgykjbvewxrrcdykuomrlhamlhxzstykmfncbbkozncogbthvdrttafboicppqgfuvutfsrdvpnvavatvpfcpoczukoyskqyinzhpdunoxffvjpfxyxnelalhnwmzjzcjbndqkutxlekciqzxsgdynwvfuhkqlssuywktmsgbrazfedmjwfjuoxroanbipuiilqpwzdcbalwdxxrpdkwdrjzxlczzbwxlecntxgstkhctsdjocleuhmstcqnvlgkedyibdcdohnzxavsdbjvxucnuirrjenhxxtsyunbydyllkijehpwffykdjygganbiypiogebqmsndzdkqyodabqrwitrmhwkaptgrtfyxfjtdvyhbjybfftugtdocvomcsfowxbdhncpogbyioijutjgxirsauzvlvjktllxucqyniowzappgxvngghdpdlyrzvfzonmmijwxxbgvaikrswfefrruptiabegaomcjjnkfoazlyvdvppywcxjpjbxauyejrfixnkxflguuqwbuxocawwuhvhlvrjcklekcwocblavcitgpwmuxawxrvgiibgozmuyzvyonyvgyxlezcajxchiytjoaheozixofdgstnijliogyvfrlmaepvifdrqfrdufbuhqjqiehnakvcqoxaskpbrrgynnkqvnzhkbglpaeqdvqxxghuixoydcwupbvpkelrzfwlzenzoqbulgvvkowpddxcpfrigxgeuccqvkzkfplcyyaqsheqjwosqsevbuvpglnlhtoieubioskacdfpvorogamnbwnajomrdfrzgkufouftmdiowtxkmbktzvvnegotgnzmklvnhmwrmajxytpexwymfxcerimsyzxhraehnhmshkwmcvaufbsycfcdjacgawmvwvmvybwqajhflxmbjenkeyvyullqyxotwkrtdgglgrlxcjiicnsutkjldirboqlmvfrlllxtiquhfpxhczzrmumznjpwcfmwmemltqvkhskbchpwhqruvqnqixbtorkrhxomtuybgudzonchsslxyslgzecpdavfxescyoitwqxnvcsepeonbuzoyoeypezouczbzzbnmzccgkhmwfbmeicmwqjdegmbbckgioqwzapatrbeedksjspndjlvljlqqnesduhbbtmgrzpbjhorzhknjpkrxznthoxsxxrnppmalnehvkkpdoskffkqithkqjgmtbxgalntgispxkgqvhxcydzfsdkuwdzytkolzmywtsqqbkssplynomcsnfethndaicofgxsaslupmgtblvwvhsamejhvdqhuijdwglfjpfagvtjmmghikfnetdewtwqgsjwtlvwjcifwurvaqwbcrpiqghnntivzzqdvuqtucbwustfdgpqvvneouriwiqxsyrultkiysyqcgijkiqjrxnfwrxahlkrcnodyjtfybfspqckojtriwfojgpcetjayrgjtrzigvtzosmohlywfyrbtryxhlcbhadacpplueillitgruqhexwcvhxpphbtksuirsnjnxvxyyiibloqmrevjlkghynenizwpkzduifnlfksipmljdujwqafywlvagomisejmbrzbxnogrdkikdvdgfwvxdoxxahtskkyonwlaulsrdjzokijupfxwdsqbveyieuwrohupopshocaeqdnsphawwnvrzkyzazdccnyodxpnuvjshmkrtmcklnqyeoovlexwksutsvhkbrhjhhodjidvkejkkxtvqtcpiiooltimziokpzajzfvpylcoxyglbkrglvnzftsmzmxbovviavuxezpxezuxzzfrefvbukfuwzhxzjkfaynfcjvkvbndrdjqdhnsrcxicxsxfjsdpvsmwvpqijeemnknsofeqywovbdpdopggrfubumvranfzpmehzuqgykddajkwqllyhalnyoylkyoczxozzrebnwljnbxvdxnaprgqwmfjeoyozqwqlwudlxjpuukrqupzigbvmoysjzpprcsusrzomywxqfpqomtztgrfggyhbbceiniofjaghnlucvtfdupgbhbvnfvtgexgnvjvwdtyxxgxxvgymtfigraqskxvnehqohwzqzkhxpifqrutlytfverrlbdwfqkiejvatuzccuxtousmxzppnkngxanzjhugytabydqynmnocqlcdxndwohtptktjdrxgtkvqyzoimgmsomqtnebsdvvrdhcalhgsuoglebfdhafgezwjnmgoshzoqffbtpilpberqitxkzyglpdkcwwvpdqjzwcvqiazhrurnesjrzmvwvdboouqyfhyeziceekrhncfjhdeumvxywinudsfovinwxsbconemtexvfafxhaerjvqnkchnsmgljwdddjsgcadvavlbnikfwvdsckvluigdvcfuezfxxxkrylxsnhwuduhfkdakllkawxmyqbkbzcqjmsbgzfpojtlpqvgtqlmwurarmavmmiatpfxvfzfqacptkhjgobtcsnazpbroehpizwtpmrclahjkkzcmmjznsyaglerbnkzetxrojtsqffhzliqwzdwefypaotvgeiawuwxxfkwlbzrntcaloqbubnyjdnsspmmlckzdpllmcncvrkdqrtmfbbbjsmuamsiipsqzexrckpcpnfnhjukamxctwsbfrcuuccbankpotvedkkyrmbttbzasydxkszzdadjlzrdmzbqtsqazuxeloeutjxdsciiugbwvfvwykptjbmrlxkqxaytyzubavioljyymsmkdzbiboaosucwfvwovzwcblglzdwuiffzclexudskropugxsszdttwruooehksqtgwabwrqxmiqcidjpadjbyldjmgfghezqzkqolfueavyousvfmyuwaaluszwzkgalilmguoiecvhsawptpskudkmvbniybaslympseyyinueidogmoiedkqvuoywnduxctjjvjhcphtaddsasmzrxwvfxkaypozvnhfalmcwvqcaeszthvbqzmdohdeqkfdeeislkblohlxrxqydoogzevgsbzhgrvyxvpgyngsgqzodgrrtqsbnpvfhybjgtuufmmmsekzmuyuejpjtuisqkrptauhsjcllecpfyttiapogqylltbjhzrjldccfybxsionmqpqeyusrtastfoqksshmziezadeogrojwcanijxknuvruioetfexnzfejkkxlxrktswgqdgkeznvyzwkjlixlxxprkbtskpjezoycykjtxjorxiydrgvftxttaciifiifbdmbhozmuftpvekolyxcwnzhwgmzcsiumegewfvyxwaijlgwnjpxohsfkuxxfytbvrkcjzlnxmmcgjmpjzbovcppppmpuvfcknlkyhbcaevgviusffgceekjwhswxhupfrtxhwhjmdtiicppzkcplcqaifzjzfnbbtistgucduxqprfughepxnkzengymokugzokudxesaoflosfcxdulhdqlhebhmuogzkqqmvpsrnljwszawaazgofirmswuogqzdbezgfhydcgtcmbipuuvrzzrlvsuxqgesprlrmdtvzukkyksflpojpmfkurnmjslxvkrqbknmmeavkiqowseqiionjffctbfgvdlgridoowjwflmdjdjpziiioguaspnacxlwlyosixpbxukglrnkzjtcalatqfxqrdrbfqltsgonoyzxaittzathzvrtjpmbnbnbuqmxfcwtxvnafhiksmbjxpxfshqkytwunhflybohwzuvvpwaqlwdbxnnzdnpikwnaxjyldyltfoiyqvhzrysfblphtjyaizftfmgbbicjfvbbnzjjofpymyrfmihrssgxontbmugivvupgczbajxodcdfutzydnfzwogncjrnopjsxkxzpxehitpeduciiiwiowxlbcdjfekjpzhdlmtkckhldpwcqntqnoftmjphqcfpydbmkpgwjpnjcgwwshltewdooxmzmmhwpjckxbrcwismkmkgnduvnbnjntvaaasxocisoreldzcpmnftluzqrvxpftrrvabdojqqklqvssptacdcnlejxgjyvreamirjwvlbdvyuuolbcdgoihylhkpqcuokyyfzzgldesantmyoqgcbyrkdzhhteybvgbeeektccdgkvmmywzdtaspyuilnmziledlzxuhpmcckyxiibjdaxgqmxybpewnynlwykabudmtmjwoujqstusxfkpnbhgjqoxxhxcahezybokuanmqfbotwkagqqohaxytqmeruwakokwomfnrdefuljckiixahakaxsdyojvutmdmgxdiegvlblyhogqlewcddesebpzleihfcrttmkewoalaxathwluyvvfbavhjsqkttzodstcekbpnthsvprfijukbuvtlqedjamwfahjhvivcoarduvrhczuxjbfxzitlorrntwebjauxejwpswfksxbtecdmwvtvjgvelliisqtmbfazilmmizkbqiifokdaajotapnpkqhdgsmxhtndlupujojefwkasgsqgbqnhkrxbfunnzkfdtnlisryccnoobvewvavmhwejomytxxoclwutmthshxdddpokdprsfumpcmqhbtwlmdepchvsfkoyfzlsxnrmmuxlktunydlndafnvwhkymapyfwwgkljzufstoofyguubmmhgqplgyudbpopzvsijjerphhgyqqubnkgqlqhaiyaulzufdrarxaruxhbzeowebppjirmrnffrwcmpxgpeonfndbeivayxqttgjqqpizyuiupftoyvaxxxqqxdnffhmfmtcfkocawihcyopiaxvjibugwitexixqxsuxyubcdysmgzelhgykjfizyuvqmiajlokobiwmnuggqaspymnwfvorlpzjikffuctkjlpsrbbnzpjqgxxbjfuuqkkvscynswjnmfrcfwwjeqntczherfhjrvgbpiqfkhsgjirldsypktnjphrdiuaiiuimptnqofmiqqlqvnhwiitgexcjopbshfubrlsdbvcdfdtoufxiphxrilhemygjytnzvabaqjwbckzbcpltovszpffbzvhlbatguhjufkjd"
    s2 = "ylcotuazxfmsojotjtnjnbmiestmchaxbgxkimkcgtcutoqfunbgnastygeqvljyjnzwssxenqcqmlsfsxyznxqauakdjcczivtdvzhyfyzzzolhqfkaaazkjznxzdwicdrhlbxnwahwichaymehyqtwimnxpszgpdpakeuyqudenyntlpogkitjklxqsalvcdsptrhgdpmuknnnszmbbcroqbasxngigfnuvaehxbfqpmvkmmdlofgemxhordbctbafsvwutdnzmemmvviwubpgjsugexoevbbshdhguvhhvdkstmwbhtygfpzsjuqnxzamcunrqpmceteowiuqrstiqwisnfrwjhlbplwhlazvkobcbzgtaszyejkpcwnpstvsydjfrastxtxgsaeotdgrljmjtcykqvmcwoqjyrsuduekjpmijyotoypocpadvlzlxrpqojoboyflqecaqqkbkuugezkvvcvkuapxiiommosbwnrzxkesrsmzolwbtkrejjmidkbjlleqjlbwszdujsvryswyjmyetbmevrnnmosbbrdjnrfpjunbujpyvykqvwylstblxsqgxfaiiaxlkpkqypseezubvniivhpuzifpdylyrsvskexspzrjppzhkzkhnthtiwtwpknlyyqkclkplsdxtlxcmaplljxyidzwtykvtopfqbckueypiirrugnpvzraezxxmbexalqptvqdyqehyfnvdxmfazxkqzhgqkjdwqqmykvyhfaojgltqwrsesothqrrpdgmepgxtwkgwkxzzdkagvvqqhcsgxeqkajpakymxhybbxvfybgydshwneensnehanrrpkqkmxnyizlficycvywfdvynbxbxkleuhzqjslbolebykvqiarifxbofieboyollxqukpslzlorwcdadmbalgiiyarhkbevhsydredoafxtbkbgghrqrzlwyxpyxsesqobqgvdrjnrtefywdscecurexmqcvjhbeareyrzskicpzxslhdsdilsvdzejjnzuasswomocgmpvxoyolkbvsyvrkpfgdoljgaxzmjrzbsdqqferxhntuklenqcofnrcisedichncejxujhkqbluvckvogiprrmmqmjivomhhduyhastanololwdholknufuipjgadcbkyfhhwmlspckizotmqxstturxhvbopxzatdbcbftsfkvrnliswnlcnfjgztqiilhtrfshrczhwrdgakwyefdcregeybckvuxgefzqitllufrcrdohjrnvsliidhotpfegytotpjgrgvxzuxxmfqsslvleslloegsqiniesztdgqoniyperoecuubmkniqxdrpkautdiepqsfgyeyhcpywybmqpicoxjktqlhdowlzqnkywhbcszahuhdzusjrlytjajkhbekgkhfjhyehaboyodfyemvbdpumpwpepllwnkglmeoeutllgmnefdfsjjrhwncdjuoglolgnigesopzcitzmublikzvbtuwfmlixiouohygtpecaqiarvlvjquhwgskivqnugscbhwbfwczbomoyopkmcfawkptowxhcoinryagwzwqzrcvwqypuvudtqqootykyxjszfnwamnnawsrzxujldwqecjvgqasndukzkhjlglzafuuzkpdopxvzbfztszdbixxdhwuvtmbpgagodfvbkndlfuqsszddpucpcnkkafgztnthrhtviyusxpmvrmxehzihiloycjtxitiysabkskfgadgtanjgwtrtjblxdrpffwxbxxverdeaocyvtbiuoswdfslupbvvljskyyafmafpordsrcxgwhsrzzavxrxyalsltbgpazjsnzszbodpckrbgcswoisqpxrdqpyrfrkmzgnxkmwrsrjpbxdsygiavwrjtsvdrqcqdvcksifjmkxgjjbdhhonsmeeugggzwaehrkksqyuxfiujqzymvshundzkwufqduffudyiwgsmsgpcjcjcjoifgrtzcwzbwugksbjwnagrdkoyupijuususnidrwhutyumztdjhkplfoidxcpecjonvsyyegvgqkkgiftkpoiilavundmhfvylqyvmrsumbilvwuavxaprngmzfjmxfvbvifdujwkufbgdxvtonpbixlgwhaqywmvywqffjxemjyvimpdspcypuybsyplwpmhmoxjqxbbthncmpgtupboupshzwcftfezekfeqbtnznmicivderihfnhzgwnlngzaxmfmguhjzbrjnuvhfcbwbmikizkcrsuosadtdxtvybloevrgbvbqapepuoagfnbghvyczrfuoxfryilptnqvvekkiafdpqxbeebaavhaxodgignoovzdslkjvhhbfrcbyqkxdfpycxxbemedznmybhnmrlbtyaslixovkagqzcrzmuuqmnrmsbczuwazwzbpqjuoztiotejzfhmjdorvdbltqfkgannctbfwspwpplzlrwpxtfknwohsjwkypnccvkudgtkgzqcgrgpuvuhbdbhpcryogpuzozmcnsvrnjnjqimdozemipvdmurucidhtfwqfvvfvdjitdnzguxfmhzpakfacbodntjkkdjlgarjpdvwcmeorpgknauhqmdkbwosxgdgffgnhmmgnmggiemabhzlthcaffclixppqpahguysacoqroiekpgiflcaqkkzothgyfseissmhgknopogzfinuchyfwjsjuiiksttqpwjlyimcjnmalpqvbtsldznqwugkskikroefgqjnvzoplgfkzuqqyaalnefuircgrhwbshxunccnrdldxybkrpwwziakhemeusnxofbqqrkguncposjyljhbpyrzuesxxanbjxmuuabbrwezrehgfwqrqyflmmlydprpfuhecyqvmnhdrgffpkfgaixkrpcrilctvthuvezrudsmlnexfnkzubgbzatfcjjguufflaixwjgvgpcqyuxwsfnowafnglteueffzratxnqgibwtvcygoppgcnblumxfavizherpzfatmrrliswqegsdykjpbzehnexbpmgebrmqasodsgxodeqfwqwnytwtbkfydtizloygnlilyujxvdqeoquovhdpsnbltlopwhjwqzzwstofvocpnmckjlwrzaxrmvbfptucbnfvpqxybsqvekqugkcjcdcdmueoovkeyisnsqlcowimxzuvwpemluweeiuesxzlbrwehzqprznyvpwsezxgvafastynbrmuqchfglcowjvhevwuubhfiormhtlrhpeytnidyzppobjeclubjigdrmjyymyxyelbprgohpberhuhcuyvpchxqqdpgdnfgtmauvwidlvmlacdqycievmjdmbplpcczwiitflemhfesyhulkgnlftsyddxpfjispiebmzafbqxxxsbejocgiigvrwmqfcganokzaurismihwnikkmsdcbmfyfcuutrogtjlttaxnolsieihxvubpcfmnfnaiswjaoumfhmivzpbrraeftyhgirmrvyczfkssdnqpuhmjafvpnttxoixiwejurkijzywvanfxvkkmgqtqytnsfntetauncecthzjxfqrafouhagkrdsuxcxnzqaiytfdiqtwxkmhuhslnditxhjmmuijagmrrkpztwwftsvedtdtqetluqmcepvisnwvsonkxqelxiatbhhncoyadghlkegavegncnzcstexayayoupgwfvxtcjncpktjivgruxslebxukudntwhaftyevccdhwodugpdrqfwpzpztvthlmhfscdumxqosrgfswgmszyqsetwvmfhxlhuwulpvcsosqrlvzklksgimahvdaoxqakuvtpzvfejrflixyoyvdyywcfakndzhrvbdkrillejoicbpmhcnvpyhcufaezunpkoripsbcyurthkvnmkkmjsvvbpbyzwcjrcoemldczdslsezavblhzoxbbyjfuhxpbckhbkpkcdmtcvudsoqzbnegohzyhxwjsjiuzdtbjbegkbrkpohrgezmtxdiaghrfrdavhidckgmmkspminalblvgbauwyznpbtfpqzjzzlvzikefcuahffddmbjqpeflwgvsqoxmbxpxadaglblgroxqwgejpxzptlzwyfuhyziahpsyjljqyzewzhlfoctchirzfoxgauqaqmgzjeaktteinwhjtkxsnogefibirkctyuxlygmrarvsjvkytfdqcqlydebagavluuwgehlvuhcbbmmkrdlbnyqwlpnkfgmjktwuwtwtgaiynackkkvsbnkjrjznvmfeehzaorkyimgemzkwjzsejtzlbrtxspqhwjfsdbikpitqdissqjjginuptmrdhhgllrmxokekfldwpgzbwyfuctfohxrhehjevtbeiprlorgbuzxoogyqdvfgiblauogzefsxjiieezxqrqqltfvpasjefjobdqwdsizqntjeianpwbyxlxuqpasjvfrccwaumnvulwzfxqqkvjazxnicvkyimzfyhatigyhinvdqswpddpesgxrhdrpajlndymewtjpbmbxzfiqhviypfdyhlkbqjszxnkiehwhiezixdomsubvslkghkkxqgxzqnrizzwssgdbkgwzivfqtpwvzapilhmxpxigjojiosnkrrywoyjppcqgmuzfadytjjdbtrxeviprznshajjoqkjwdxeouuvehkszilakgorfcgkbvkpiwdqjzanxodhancltmjbjkaixxrcwvpccmzczysfokecjsaurtwtxgdogvjwkizbyoahrbvlsomdoxskcmvnorzzsjgekmdshujurhzowusqnlzzwvzfjzpmpnphoaockosikekbhqgfsqxqwtsuwmrieviwbygbgchtawboxwkhzyyosppdptngszaouukrkqgddofeiqsvcbzbnrwebcgtriehdhvifzxfjviwooynjzugjhdjstqszleaklelphlmippragvevsbkklvhluozuehemcarroaftzihnnuadpobwmvhxiouuwsfcphevzcuizvpctdjkpwhcttehvaivdxsvesgpyovtgvqngkppilqanxyeajpjgndkrromomkqfuwvnunzdqprzbgireucpvfimiyfrsrfeaibngfxhjikrktqcjcfbobbdpqrinprlmshfzyescgoqkpyhhujgfaasggpgujaprhjbouizljenfhacaobtvbwmdvilczkugwgeytzayoxobhcwgyzwsbonvwfjfltsycnxltltmntekdkhahuvwqucmtzsnagdmgflqgpybsbsfiuxajtrjrugpxdymrmjdllqqsgcaqvuuokajeubdryouyopwnmlqqtlfwyngxybrvzhzxvqyigoqcziemctkggxynbtgnlegyygyxndkbondpofznylislptfvxngrbctfpvyxlooujbccupycdfmvmailpyosezhkrctdxdycejuvvyscfhjnhdjqetmpmdnyhhprqaezkcbjjaqbekiutcfenaahsxmheisbvvtejkpxgoocpcfozswqsswvdzprzvyyitspufrwchskadjmrisuxuhxnnhitvfkwqnzpjbhzzcrbaxqapgcbihkifiqxjvopnyelulrauegwbuqqaoscuoawirzpfeidhtwqcnujbyrynokbfajnzjtctocfepkpzisckezbtkuqbivbecenwilmccerucgcnboxpmgsoojgqtxevhvmzecvktucxbjmirmqvoiebyhkzqtouiaoojigebampbncmiaqojbkgzakijdahjmtufwcxrmjcqjfzbrwwtnctgzhztefngvpwtdnqrrevzctxhkzckugtgekrkbmglenpsknjcvitacouzqpiiumixtpfqlbvzsylurbgytsszhomhnsrcccpczcqpprcopgudufouncsynqjwwtdqnppblgwhqhldkjmdsfiqhgvpniyeznnaxduqpwfdbhhbcoisuphnbynoocelojbqvuxdcjvwxasnxejjczuvrmrpcklvcijphbghcnbevagdnqfykifozsohueivxydchtmmawdaoiywhdmhpkkhtgyvgtdbgvcedwpocfbuibbcjqpkjlzdjsbanjihuwwvmchovjgwunonvwkqjdqrjkppfekjcehismyrbwrsikxuthwtyyzsikpdloayjkwbubwuuzyueyhpnbljukmqsugtzfpfyofptdoaxwtfebwqyezclnijfhykymgmyjadsxaxpzhaiqgqkygamatbpaaaevtetyoosbwvhferwvxcwzayfpfkgyvjgakyqgouhimcyccputtsrwejwliaxewjaedfyxhhovvdwiofccjjfkcodahiafzhhcundpsdfmbxlfrldyceezushrrmbkboaneauydlhrhhqfslwsssflzsnpmtqgsexgxvupvlvuucgnvchsayimzqwhegmqvppzfnasralodsteegzgdkabhkoaaiizjhxghxdshwqxpgbpppnazfchlueyqewpazmnitxjhxlmjfwqubyfpzrxkcjdxsnvdntqkohgsbrozewitmlyxiscjmgyprgtgkqzwryyfdptapcnuhusbncjyusndwbsxuwxlewjcmskculeinswcagtyomdoaxoqnirgsgvrqcsofzzsesgdjmwrnyybjesxrebxkjappjtrlloiruslbypzparqurtqzhnbeiraojtebexzzeofeqwiwnxdrvawbsnhwawncywlyrvmuwtdiyvevuvvndslhgrussnpzyqlmsjhzeyufdrbqkqfpdnnlhbpsgyswrzdfuzqhvftadiqeslgbwcslpuwqkdmkwqdaxuvuthcggpgnoeardqnhrotewuypozgmuzfxhqinipomfkydmcnhifpmrktzqlncoucbpelwtsrcjjwphnglgcgsgqelyqbeymotiifnybgatrrpbowpcsegimvqkmabnlbensjotxxetwhosblyxfitocmaokoadwjlvkgzoreyjkrpdohzmxljdrdzjqjojvbiyhokaxyxfikqsthjoamkxhkxymsgvklzvnnngjasswsbyfdabvfyjhpijkfwfiowtdhjciirqrbrwdukstrlirczvdzkkshfdkioucqtfmihpblqxwmvpxetweoifqiypthdfykdrkbwwcuyuygpqiqjadwypxtdphavaedauplrxwjxaitcoetjbwvhpsizvensphpexdvqjcxldpgizcysqljarawvrpnozhvslfuttphheiswsaxshbqacocmdkaoqnszfcdgpdqxezvwkphtsubkohnpgrdbjutfejpobxckjtemroeidwyzduxvbzdpqxkppvgusikpgozxttvnpojlreuqnpmjfhbmninaqzlgbvhbufgiuadefemupyrccczupdhsmwspkhhhaqmyalgreqrimamsqfbsvewaiebzffbcmyexchfycyzubexlgdhdafbujkbosnicuahvuajszoqmwqpbucusvdrteemrwvshfeuecdaswheuyynczjkinsnwxxxibgqcgcaxmmvdqpttyobhwgsxbuokjppdxyvqqtenjfbdfcrbdzllvhrlnzosfhsmyknjddmfblggrbuhgkpxxgupdbzkigbvemtpmnrmowkrdzegfpxplcwgybdknmbwyoyzmhvztoogkmrluykcrwioyhmqctnfnhngbmnbvgnfwtbvtudefcxvuylmchgnvyorxdywahexmgfjifvitjsbrbngoetpnqgzaiplpgndlitifeclroysuykbotgbszfnkhoiulxahjjwtxxfmozfunexiehijvvxtzwtdslklzaytplnovuvycxirfpdkbuuwsmsmqoqjfoodvbaavdraxocjfgdmldvhdylgdbzopxfgqsfbwatyuzusjpbfeqtdwhqmmzgtvokrtvkhkvzzxyjyoalgzngofigysifhsqwbcpdhvwvgsuefqjcakzujhnrkftzbiqevokharafvehvhqocetzwyjxbuwppflibuzgtifnyczhjedujdiyrqnbscqapnwulyoosuddqeflcrtbukvacifqivlonjcvsovzzhmnmoufatkqofjmhjrcnbkcnzaayzokqgvwzkjybnfioqgtkslxzfmyqldbofuyfqsevyolaumcjsmfxpdrulslchkkbaxrwjczxswhaxxumjkicxnvhwtxonipuogiderovcrhcyrczcubwgtyeeyvueazxseuhupjzxesveckigahupcdxlztbphdhdwvjtexivbkxyrmdsypabpqxixbnseiibnauhnbxqlkcwrvrmtdpbealttvvelqifmkfsjzhnaxdrgrfljlfrnqtcozuilmgudlzblnorriimmmgydrpostalitfjdxtdzanqwxfmdvduvpjtmbsttaegjltahgwlvhumxzjcrmbfbqxehmbvoksjlfrvnmchdcujqiazavyotzcksxrtlwzrbxdvdqfordtidhbtdjrpxplxhwoeutsevzvfthpscglynwujnjqgonhlojbjhcqtagesfxoqjcmvvyapmwnmegrttcauutfkjgqbgkomzhdnfxqbhlrmnznnqljffihmfxoziojgltztgyohzaxrqzvxnlcwegiodkiipzfgrnpdzxngspecqbdsdibrodbdbzezbgzfnbszvamskuojtlszltgbleebgfcriskbvxdlinojdqnystcszubjggalzaapkhvwslcgypmsrjydmnflbntzbykkbfaixyhuxmehrvxtdvgjimekmbsnnmkppoqmitlmuvadzyibbakinnaelbgpjnyvqjovucxpmsqtxiaxdyzftuhoetpvvndjqqdtauurgatbdshriepepbpquwpbppfqccgnbbmiaosrwvexrgrpvbnhanujhzyvvpneqexwmtdlurpdmhgivbtourwplhcwxikyoqkgmfyrtagybcgipwrmcooirzpaminzgfdnftdkgcdoemiatlwmclzbfthmkdjtainbbhbbtpjzybxpabusdnsbomrrwicghclcyhwmgknisoppgzwnfdiqtxctvitpujafnagwtippdmbfjcempupwdghhcqngyeszyicncylpfwrleyhjrxkoodcjclwqpcwosoirkchvieljwindydeiebtcouwxtiqsitutxjyzccyusxyrqopdbgvxgxvjwykgliphvhfoqxacgslyvzxczrrgvxptyndcinoecxkmdfuvzwukskhwgcchczewwbzsrcalgjxxkdaawwemrdcnsqpqoqfreelretvrtsuaunbsejbynikzslsvorwabfnkdnurzpcyxkkoqfonvrbwnoxziwuzgyqlrduaeqeqrxppbajzbdchrzwogyoevzfizrwsdvdctxkrzlkaqmdbeqchnxuhitdczebntajmypyyoxcmdfcegpnxwcoyelfpppfiupzknpweyjkddeinihrakkguqfdyfsapabsykvaeqcgehwwkhjhfeumpfkdmeuptxoabccuwusteyjzonatqqejbcrndcaadeskdmdbrimrhnfradkdpbnyudldgiuboguwslgxczetqvmyhcjoqamgdzgmclemtimaoroartgbkwgnegxoordytopfsakgovafuclbjvcfypkpkoqlqysepkkaqmtcbwtnqkdbqddhzenqkneapjqxmboiaeifwivjqswfplbmtmvlqsbhhbgnrpaqaznoqiblvcvrylsmvvtuhlyvonb"
    s1 = "adc"
    s2 = "dcda"
    s1 = "ab"
    s2 = "eidboaoooaaa"
    print(checkInclusion(s1, s2))
