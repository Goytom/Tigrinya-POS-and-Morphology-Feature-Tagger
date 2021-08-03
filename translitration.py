## Transiltraion to Roman Alphabet
#//

t_di = {
        '0x1200': 'ha', '0x1201': 'hu', '0x1202': 'hi', '0x1203': 'hā', '0x1204': 'hé', '0x1205': 'he', '0x1206': 'ho', 
        '0x1208': 'la', '0x1209': 'lu', '0x120a': 'li', '0x120b': 'lā', '0x120c': 'lé', '0x120d': 'le', '0x120e': 'lo',
        '0x1210': 'ḥa', '0x1211': 'ḥu', '0x1212': 'ḥi', '0x1213': 'ḥā', '0x1214': 'ḥé', '0x1215': 'ḥe', '0x1216': 'ḥo', 
        '0x1218': 'ma', '0x1219': 'mu', '0x121a': 'mi', '0x121b': 'mā', '0x121c': 'mé', '0x121d': 'me', '0x121e': 'mo', 
        '0x1220': 'śa', '0x1221': 'śu', '0x1222': 'śi', '0x1223': 'śā', '0x1224': 'śé', '0x1225': 'śe', '0x1226': 'śo', 
        '0x1228': 'ra', '0x1229': 'ru', '0x122a': 'ri', '0x122b': 'rā', '0x122c': 'ré', '0x122d': 're', '0x122e': 'ro', 
        '0x1230': 'sa', '0x1231': 'su', '0x1232': 'si', '0x1233': 'sā', '0x1234': 'sé', '0x1235': 'se', '0x1236': 'so', 
        '0x1238': 'ša', '0x1239': 'šu', '0x123a': 'ši', '0x123b': 'šā', '0x123c': 'šé', '0x123d': 'še', '0x123e': 'šo', 
        '0x1240': 'qa', '0x1241': 'qu', '0x1242': 'qi', '0x1243': 'qā', '0x1244': 'qé', '0x1245': 'qe', '0x1246': 'qo',
        '0x1248': 'Qa', '0x1249': 'Qu', '0x124a': 'Qi', '0x124b': 'Qā', '0x124c': 'Qé', '0x124d': 'Qe', '0x124e': 'Qo', 
        '0x1250': 'öa', '0x1251': 'öu', '0x1252': 'öi', '0x1253': 'öā', '0x1254': 'öé', '0x1255': 'öe', '0x1256': 'öo', 
        '0x1258': 'Öa', '0x1259': 'Öu', '0x125a': 'Öi', '0x125b': 'Öā', '0x125c': 'Öé', '0x125d': 'Öe', '0x125e': 'Öo', 
        '0x1260': 'ba', '0x1261': 'bu', '0x1262': 'bi', '0x1263': 'bā', '0x1264': 'bé', '0x1265': 'be', '0x1266': 'bo', 
        '0x1268': 'va', '0x1269': 'vu', '0x126a': 'vi', '0x126b': 'vā', '0x126c': 'vé', '0x126d': 've', '0x126e': 'vo', 
        '0x1270': 'ta', '0x1271': 'tu', '0x1272': 'ti', '0x1273': 'tā', '0x1274': 'té', '0x1275': 'te', '0x1276': 'to', 
        '0x1278': 'ča', '0x1279': 'ču', '0x127a': 'či', '0x127b': 'čā', '0x127c': 'čé', '0x127d': 'če', '0x127e': 'čo', 
        '0x1280': '*', '0x1281': '*', '0x1282': '*', '0x1283': '*', '0x1284': '*', '0x1285': '*', '0x1286': '*', 
        '0x1288': '**', '0x1289': '**', '0x128a': '**', '0x128b': '**', '0x128c': '**', '0x128d': '**', '0x128e': '**',     
        '0x1290': 'na', '0x1291': 'nu', '0x1292': 'ni', '0x1293': 'nā', '0x1294': 'né', '0x1295': 'ne', '0x1296': 'no', 
        '0x1298': 'ña', '0x1299': 'ñu', '0x129a': 'ñi', '0x129b': 'ñā', '0x129c': 'ñé', '0x129d': 'ñe', '0x129e': 'ño', 
        '0x12a0': 'ıa', '0x12a1': 'ıu', '0x12a2': 'ıi', '0x12a3': 'ıā', '0x12a4': 'ıé', '0x12a5': 'ıe', '0x12a6': 'ıo', 
        '0x12a8': 'ka', '0x12a9': 'ku', '0x12aa': 'ki', '0x12ab': 'kā', '0x12ac': 'ké', '0x12ad': 'ke', '0x12ae': 'ko', 
        '0x12b0': 'Ka', '0x12b1': 'Ku', '0x12b2': 'Ki', '0x12b3': 'Kā', '0x12b4': 'Ké', '0x12b5': 'Ke', '0x12b6': 'Ko', 
        '0x12b8': 'xa', '0x12b9': 'xu', '0x12ba': 'xi', '0x12bb': 'xā', '0x12bc': 'xé', '0x12bd': 'xe', '0x12be': 'xo',
        '0x12c0': 'Xa', '0x12c1': 'Xu', '0x12c2': 'Xi', '0x12c3': 'Xā', '0x12c4': 'Xé', '0x12c5': 'Xe', '0x12c6': 'Xo', 
        '0x12c8': 'wa', '0x12c9': 'wu', '0x12ca': 'wi', '0x12cb': 'wā', '0x12cc': 'wé', '0x12cd': 'we', '0x12ce': 'wo',
        '0x12d0': 'üa', '0x12d1': 'üu', '0x12d2': 'üi', '0x12d3': 'üā', '0x12d4': 'üé', '0x12d5': 'üe', '0x12d6': 'üo',
        '0x12d8': 'za', '0x12d9': 'zu', '0x12da': 'zi', '0x12db': 'zā', '0x12dc': 'zé', '0x12dd': 'ze', '0x12de': 'zo',
        '0x12e0': 'ža', '0x12e1': 'žu', '0x12e2': 'ži', '0x12e3': 'žā', '0x12e4': 'žé', '0x12e5': 'že', '0x12e6': 'žo',
        '0x12e8': 'ya', '0x12e9': 'yu', '0x12ea': 'yi', '0x12eb': 'yā', '0x12ec': 'yé', '0x12ed': 'ye', '0x12ee': 'yo',
        '0x12f0': 'da', '0x12f1': 'du', '0x12f2': 'di', '0x12f3': 'dā', '0x12f4': 'dé', '0x12f5': 'de', '0x12f6': 'do',
        '0x12f8': 'ğa', '0x12f9': 'ğu', '0x12fa': 'ği', '0x12fb': 'ğā', '0x12fc': 'ğé', '0x12fd': 'ğe', '0x12fe': 'ğo',
        '0x1300': 'ja', '0x1301': 'ju', '0x1302': 'ji', '0x1303': 'jā', '0x1304': 'jé', '0x1305': 'je', '0x1306': 'jo',
        '0x1308': 'ga', '0x1309': 'gu', '0x130a': 'gi', '0x130b': 'gā', '0x130c': 'gé', '0x130d': 'ge', '0x130e': 'go',
        '0x1310': 'Ga', '0x1311': 'Gu', '0x1312': 'Gi', '0x1313': 'Gā', '0x1314': 'Gé', '0x1315': 'Ge', '0x1316': 'Go',
        '0x1320': 'ṭa', '0x1321': 'ṭu', '0x1322': 'ṭi', '0x1323': 'ṭā', '0x1324': 'ṭé', '0x1325': 'ṭe', '0x1326': 'ṭo',
        '0x1328': 'ċa', '0x1329': 'ċu', '0x132a': 'ċi', '0x132b': 'ċā', '0x132c': 'ċé', '0x132d': 'ċe', '0x132e': 'ċo', 
        '0x1330': 'Pa', '0x1331': 'Pu', '0x1332': 'Pi', '0x1333': 'Pā', '0x1334': 'Pé', '0x1335': 'Pe', '0x1336': 'Po',
        '0x1338': 'ṣa', '0x1339': 'ṣu', '0x133a': 'ṣi', '0x133b': 'ṣā', '0x133c': 'ṣé', '0x133d': 'ṣe', '0x133e': 'ṣo',
        '0x1340': 'ṡa', '0x1341': 'ṡu', '0x1342': 'ṡi', '0x1343': 'ṡā', '0x1344': 'ṡé', '0x1345': 'ṡe', '0x1346': 'ṡo',
        '0x1348': 'fa', '0x1349': 'fu', '0x134a': 'fi', '0x134b': 'fā', '0x134c': 'fé', '0x134d': 'fe', '0x134e': 'fo',
        '0x1350': 'pa', '0x1351': 'pu', '0x1352': 'pi', '0x1353': 'pā', '0x1354': 'pé', '0x1355': 'pe', '0x1356': 'po',
        
        '0x1362': '.', '0x1363': ';', '0x1364': '_', '0x1365': ':', '0x1366': ':', '0x1367': '?',
    
        '0x1369': '1', '0x136a': '2', '0x136b': '3', '0x136c': '4', '0x136d': '5', '0x136e': '6', '0x136f': '7',
        '0x1370': '8', '0x1371': '9', 
        '0x1372': '10', '0x1373': '20', '0x1374': '30', '0x1375': '40', '0x1376': '50',
        '0x1377': '60', '0x1378': '70', '0x1379': '80', '0x137a': '90', '0x137b': '100', '0x137c': '10000',
        }

latin_letters = ['h','l','ḥ','m','ś','r','s','š','q','Q','ö','Ö','b',
'v','t','č','n','ñ','ı','k','K','x','X','w','ü','z','ž','y','d','ğ',
'j','g','G','ṭ','ċ','P','ṣ','ṡ','f','p']

vowels = ['a', 'u', 'i', 'ā', 'é', 'e', 'o']

t_di_keys = t_di.keys()
t_di_values = t_di.values()
revers_t_di =  dict(zip(t_di_values, t_di_keys))

## Translitration to latin alphabet

def translit(text):
    new_word = ''
    for letter in text:
        new_letter = ''
        if str(hex(ord(letter))) in t_di:
            new_letter = t_di[str(hex(ord(letter)))]
        else:
            new_letter = letter
        new_word += new_letter
        
    return new_word

## Revrse translitration to Geez alphabet

def revers_translit(text):

    new_word = ''
    kk = 0
    while kk < len(text):
        letter = text[kk]
        new_letter = ''        
        if letter in latin_letters:
            letter_posi = text.index(letter, kk)
            phrase = text[letter_posi:letter_posi + 2]
            new_letter = chr(int(revers_t_di[phrase][2:], 16))
            
        elif letter in vowels:
            pass
    
        else:
            new_letter = letter
        new_word += new_letter
        kk += 1

    return new_word

text = """ዓመታት"""
#print(translit(text))

#print(translit(text))
#print(revers_translit('meleketāte'))
#print(translit( 
"""ብዙሕ መንእሰይ ትግራይ፣ ኣባላት ፖሊስን መከላኸሊ ሃገርን ዝነበሩ፣ ኣብ ዝተፈላለዩ ሞያታት
  ዝነበሩ ፍሉጣት ተጋሩ ብውልቃዊ ውሳንኦም ናብ ዕጥቃዊ ቃልሲ እናተጸምበሩ ይርከቡ።"""
#  ))
