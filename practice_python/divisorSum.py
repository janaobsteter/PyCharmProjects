number = 5

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum([x for x in range(1, n+1) if n % x == 0])


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)


###################3
#bubblesort


import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
a = [9,6,3,8,2,4]
a = [1, 2, 3]
a = [3, 2, 1]

a = list(map(int, "20575 445572 1708621 1167822 1848497 368822 1991809 713975 779379 1713665 769795 1630226 619700 1170561 1249206 430935 1553461 409575 1112872 34499 397053 442700 920008 1345791 579413 1985080 1002982 929295 1413444 507373 1865470 453801 1783244 1754044 587196 254889 927813 1394100 827622 157860 671442 598269 458877 941543 760807 29570 1758915 515614 90008 1586368 902867 720999 121927 774574 1051776 305103 367313 1522503 13043 619663 1551743 76712 1443856 1359703 295480 452699 1917061 606296 1619250 1090245 1425464 917841 805860 1570069 1158443 1806110 278264 1053288 321682 1217558 1070245 154644 1926802 1505560 1787564 1030416 766430 1106180 1826816 1265026 1591109 807224 205171 327960 529694 935180 125954 770999 1614689 1119123 1334617 1664174 1769814 933936 702326 1201217 126539 357166 908139 423534 504236 812442 1306898 201062 378107 1676252 408497 1206620 95216 1804927 1529739 1989826 267237 540066 1366255 213356 904524 474391 271669 1228981 1135809 1116943 627353 311245 152584 1492386 406093 1362276 1942281 702064 204099 635157 798118 665594 12180 1221046 1429479 1609301 556627 1409115 239841 1029401 337264 529382 1088947 1723967 1779033 181200 1878564 152240 386876 1382793 1107695 1994569 199339 977774 1209885 1599783 1772126 683337 507831 434469 928321 986517 214917 1044458 1282540 353972 218106 1169845 1260528 1801853 59618 1448806 1107624 13792 1065529 352130 469140 65392 181796 1780516 493922 1681381 402453 1907093 1357727 1714234 1966326 1950879 820324 976236 1048543 1248383 523610 981594 1184929 1818994 1613744 76364 519469 1079851 512524 1634357 158865 200399 1387792 749414 399998 1616104 1382084 1277014 1625476 385376 1154709 256295 314738 250450 1428274 1659800 152755 1115694 883941 695080 1992404 1478673 1490954 928907 1716418 369914 1572265 1235269 177795 1923694 1422371 1443470 1324721 152459 771578 1065418 988082 1152976 939234 1954810 257880 1570798 1019626 417598 790226 805474 341903 978096 158725 494296 1716780 56400 146316 1797330 466550 1648453 1907582 1575472 1826169 1747587 806485 784855 267023 948729 379977 64706 241188 323391 282020 675341 53914 208532 1665693 899339 533209 1096798 962305 349093 402464 248895 268026 1050130 85968 992207 1813393 1248273 401966 1714935 993149 771663 1250707 787522 1887508 1679044 969965 353200 1493833 1760403 1295102 1170849 251213 1245492 1110253 1895262 1235077 634296 1035520 1281289 399856 1626040 1073561 1824296 751298 945243 1596543 1002368 1081851 419496 316738 550821 472777 173953 700764 423297 1292966 1975455 1396692 1392413 763145 1601635 561305 230083 1821173 1094140 694468 1016209 1877678 911863 1646710 1984440 1051775 1800885 904108 88387 1630597 924450 435619 946314 286980 911219 886811 278065 1528897 714552 401241 972679 62031 198741 50692 358764 1473338 615697 518860 352018 358684 287440 1588015 266607 1246602 207182 579277 700128 1661765 198321 401347 340569 1471090 717503 428913 1614925 920960 1343872 1426599 197818 496537 449870 160649 327942 347124 1434603 480346 490767 123478 1878594 1516975 931065 435110 1737192 1784482 1165730 1288416 1747784 397456 352993 1885635 1624206 1187880 604165 539117 671770 1005929 1486163 1488387 1530138 1792832 1290121 241970 1679456 395098 617985 670270 44937 677367 1267398 577682 864239 1783032 650465 1865380 1169134 1584653 1306033 1208308 637920 477223 115432 469475 1602716 419558 1931781 1526137 736798 592319 863651 1778989 1281085 395821 1603125 1004221 1805057 1538004 585451 1987168 898894 256612 1452175 1243610 475543 662305 1658044 509181 921640 1620388 1305161 1534021 765675 361143 1042516 1507286 467508 1989648 169576 798867 1089517 4842 1504518 797548 230975 612676 188817 157671 153091 1842827 1385022 558746 687926 1657085 1725951 1389057 834664 466937 1324118 126901 1786943 1135951 1640459 786064 402713 1651912 1657470 312785 1299713 218210 566243 1188835 266683 176976 1890605 1763116 1301115 1123947 669943 1064752 1400618".split(" ")))


swap=0
order = False
while order == False:
    order = True
    for place in range(0, len(a)-1):
        print(place)
        f = a[place]
        s = a[place + 1]
        if f > s:
           swap += 1
           order = False
           a[place] = s
           a[place + 1] = f
