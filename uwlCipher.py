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


def caesarEncrypt(message, key=0):
    result = ""
    for x in message:
        result += chr((ord(x) + key) % 128)

    return result


def caesarDecrypt(input, key=0):
    decrypted = ""

    for x in input:
        decrypted += chr((ord(x) - key) % 128)

    return decrypted


def uwlEncrypt(input, key=0, password=None):
    input = caesarEncrypt(input, key)

    encrypted = ''

    for x in input:
        encrypted += library[(ord(x) + key) % 128] + " "

    return encrypted


def uwlDecrypt(encrypted, key=0):
    decrypted = ''

    try:
        for x in encrypted.split():
            decrypted += chr((library.index(x) - key) % 128)
    except:
        return 'Message cannot be decrypted'

    return caesarDecrypt(decrypted, key)

    return decrypted


f = open("demoEmail.txt", "r")

encryptedEmail = uwlEncrypt(f.read(), 1)

print(encryptedEmail)

print(uwlDecrypt(encryptedEmail, 1))
