library = [
    'DrAliGheitasy',
    'ProfessorAmirAlani',
    'DrAnastasiaSofroniou',
    'DrAndreJesus',
    'DrApostolosGeorgakis',
    'DrChangfengFu',
    'DrChekfoungTan',
    'DrMalteRessin',
    'EdwardPark',
    'MrsEdytaKrol',
    'DrEfcharisBalodimou',
    'DrElaheKani-Zabihi',
    'ProfessorFabioTosti',
    'FehmidaMohamedali',
    'HyeonsookKim',
    'DrIbrahimShaaban',
    'DrIkramUrRehman',
    'IndiraChauhan',
    'DrIraklisGiannakis',
    'DrJohnMoore',
    'JonathanHubert',
    'ProfessorJonathanLoo',
    'DrJoséAbdelnourNocera',
    'DrJunaidArshad',
    'DrKevinJ.Munisami',
    'ProfessorKonstantinNikolic',
    'DrKouroshBehzadian',
    'DrLadenHusamaldin',
    'DrLiangChen',
    'LizSokolowski',
    'DrMahtabAkhavanFarshchi',
    'ProfessorMassoudZolgharni',
    'DrMuhammadNaveed',
    'DrNaghamSaeed',
    'DrNasserMatoorian',
    'NinoAuricchio',
    'ParisaSaadati',
    'DrSamaAleshaiker',
    'DrScottYang',
    'DrShamilNaoum',
    'ShanyuTang',
    'DrThomasMadsen',
    'DrWaqarAsif',
    'DrWeiJie',
    'DrYingZhang',
    'DrYu-ChunPan',
    'DrA.DeirdreRobson',
    'AbyMitchell',
    'AdelaideAduboffour',
    'DrAgathaGrela',
    'AggieBak',
    'AhmedDickinsonCardenas',
    'AlbertoTesta',
    'DrAlejandroPostigo',
    'AlexLoveless',
    'AlexMarker',
    'DrAlexanderAidan',
    'ProfessorAlexandrosParaskevas',
    'ProfessorAliBahadori-Jahromi',
    'AlisonGordon',
    'AlisonTingle',
    'ProfessorAlisonWakefield',
    'DrAmaliaTsiami',
    'AmeliaAu-Yeung',
    'AmyYardley',
    'AndreaAras-Payne',
    'DrAndrewBourbon',
    'AndrewWebster',
    'AndrewYork',
    'DrAndyFox',
    'AndyReynolds',
    'AneeqaAli',
    'ProfessorAngelaRoper',
    'AngusLuscombe',
    'DrAnilPadhra',
    'MsAnna-MariaHesse',
    'ProfessorAnneManyande',
    'DrAnnitaVentouris',
    'DrAnoushMargaryan',
    'MrAnthonyDavie',
    'AnthonyDoran',
    'DrAnthonyOlden',
    'AntoinetteUrwick',
    'AntonioCastells-Delgado',
    'AnyaHamilton',
    'AqbalMohindroo',
    'ArianeLengyel',
    'AshMistry',
    'MrAshleyGarlick',
    'AundreaFudge',
    'MsBarbaraHoyle',
    'DrBartoszSzafranski',
    'BenChristopherson',
    'BenDunning',
    'DrBenHine',
    'BenPearce',
    'MrBenWhiting',
    'BernadetteRowe',
    'DrBernadineIdowu',
    'BerylMatthews',
    'BillTipping',
    'ProfessorBobGates',
    'DrBobLockie',
    'BrianHook',
    'BronachHughes',
    'BryonyWilliams',
    'MrCarlRohumaa',
    'CarlSchoenfeld',
    'CarolJollie',
    'CarolineGrainger',
    'ProfessorCarolineLafarge',
    'CarolineSmales',
    'CarolynnGreene',
    'DrCatalinBrylla',
    'DrCatarinaLelis',
    'MsCatherineCrampton',
    'CatherineLynch',
    'CathyRowan',
    'CharlotteBramanis',
    'CharmagneBarnes',
    'ChiaraBaiocchi',
    'ChiedzaKudita',
    'ProfessorChin-BunTse',
    'DrChrisBrown',
    'MrChrisHadland',
    'ChristineHankin',
    'ChristopherClarke',
    'ClaireAnderson',
]

def caeserEncrypt(message, key):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgijklmnopqrstuvwxyz123456789*-+"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def caeserDecrypt(message, key):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgijklmnopqrstuvwxyz123456789*-+"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def uwlEncrypt(input, shift = 0):
    message = caeserEncrypt(input, 10)

    encrypted = ''

    for x in message:
        encrypted += library[(ord(x) + shift) % 128] + " "

    return encrypted

def uwlDecrypt(encrypted, key = 0):
    decrypted = ''

    try:
        for x in encrypted.split():
            decrypted += chr((library.index(x) - key) % 128)
    except:
        return 'Message cannot be decrypted'

    return caeserDecrypt(decrypted, 10)

message = 'ABC 123 *'
key = 447

secret = uwlEncrypt(message, key)

print('ABC 123 * encrypted:')
print(secret)

print('ABC 123 * decrypted:')
print(uwlDecrypt(secret, key))
