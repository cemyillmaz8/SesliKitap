import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def pdf_metini_cikart(pdf_yolu):
    metin = ""
    pdf_okuyucu = PyPDF2.PdfReader(open(pdf_yolu, 'rb'))

    # PDF'deki toplam sayfa sayısı
    for sayfa_num in range(len(pdf_okuyucu.pages)):
        metin += pdf_okuyucu.pages[sayfa_num].extract_text()
    return metin

# Metni sese çeviren fonksiyon
def metni_sese_cevir(metin, cikti_dosyasi):
    sesli_cevirici = gTTS(text=metin, lang='tr')  # 'tr' dil kodunu string olarak düzelt
    sesli_cevirici.save(cikti_dosyasi)

# Dosya seçme fonksiyonu
def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("PDF dosyaları", "*.pdf")])  # filetypes list formatı düzeltildi
    if dosya_yolu:
        pdf_metin = pdf_metini_cikart(dosya_yolu)
        metni_sese_cevir(pdf_metin, "kaydet.mp3")
        # Sisteme göre mp3 dosyasını oynat
        if os.name == 'nt':  # Windows
            os.system("start kaydet.mp3")
        elif os.name == 'posix':  # Linux/MacOS
            os.system("xdg-open kaydet.mp3")

# Tkinter arayüzü
app = tk.Tk()
app.title("Sesli Kitap Uygulaması")
app.geometry("250x150")

secim_butonu = tk.Button(app, text="PDF seç", command=dosya_sec, padx=20, pady=20)
secim_butonu.pack(pady=20)

app.mainloop()