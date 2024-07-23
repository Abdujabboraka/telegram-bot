import requests
from telebot import types
america = "\U0001F1FA\U0001F1F8"
uzbekistan = "\U0001F1FA\U0001F1FF"
russia = "\U0001F1F7\U0001F1FA"

path = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
usd = float(requests.get(path).json()[0]["Rate"])
rubl = float(requests.get(path).json()[2]["Rate"])
def valyutalar(path="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"):
    fayl = requests.get(path).json()
    usd = float(fayl[0]["Rate"])
    rubl = float(fayl[2]["Rate"])

    return (f"Bugungi  valyutalar:\n \n{russia}1 Rossiya rubli: {rubl} Uzs{uzbekistan}\n{america}1 AQSH dollari: {usd} Uzs{uzbekistan}"
            f"\n\n\n{america}100 $ -{usd*100}{uzbekistan}\n{russia}100 ₽-{rubl*100}{uzbekistan}")

def barcha_valyutalar(index = -1,barchasi ="",path = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"):
    fayl = requests.get(path).json()
    for currency in fayl:
        barchasi+=f"{1} {fayl[index]["CcyNm_UZ"]} ---- {fayl[index]["Rate"]} So'm.   "
        barchasi+="\n"
        index += 1
    return barchasi
fayl = requests.get(path).json()
barchasi = barcha_valyutalar()+f"\nESLATMA: \nma'lumotlar O'zbekiston Respublikasi Markaziy bankining ma'lumotlariga  ko'ra taqdim etilyapti\nsana: {fayl[0]["Date"]}"




