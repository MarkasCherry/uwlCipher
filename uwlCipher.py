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


def uwlEncrypt(message, locks=[0]):
    for key in locks:
        encrypted = ''
        for char in message:
            encrypted += library[(ord(char) + key) % 128] + " "
        message = encrypted
    return encrypted


def uwlDecrypt(encrypted, locks=[0]):
    try:
        for key in locks[::-1]:
            decrypted = ''
            for word in encrypted.split():
                decrypted += chr((library.index(word) - key) % 128)
            encrypted = decrypted
    except:
        return 'error'

    return decrypted

f = open("demoEmail.txt", "r")

encryptedEmail = uwlEncrypt(f.read(), [3, 8, 9])

print(encryptedEmail)

print(uwlDecrypt(encryptedEmail, [3, 8, 9]))


# BRUTE FORCE HACKING
# import time
#
# start = time.time()
# for i in range(128):
#     for j in range(128):
#         for k in range(128):
#             print(uwlDecrypt(encryptedEmail, [i, j, k]))
#             print('--------------------------------------------------------')
#             print('Time took to decrypt:', time.time() - start)
#             print('Keys used:', i, ', ', j, ', ', k)
#             print('--------------------------------------------------------')
