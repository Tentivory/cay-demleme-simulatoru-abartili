#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Demleme Simülatörü - Abartılı ve Ciddi Versiyon
Bu kod gerçekten çalışır. Çayınızı demlerken bekleyin.
"""

import time
import random
import sys

def ciddi_mesaj_yaz(mesaj):
    print(f"[CİDDİ] {mesaj}")
    time.sleep(0.5)

def cay_demle():
    ciddi_mesaj_yaz("Çay demleme operasyonu başlatılıyor. Lütfen çay bardağınızı hazırlayın.")
    
    # Su kaynatma aşaması
    ciddi_mesaj_yaz("Su ısıtılıyor... Sıcaklık kritik önem taşıyor.")
    for derece in range(20, 100, 5):
        print(f"Su sıcaklığı: {derece}°C - Hala yetersiz. Sabır.")
        time.sleep(random.uniform(0.3, 0.8))
    
    ciddi_mesaj_yaz("Su kaynadı! Ama hemen dökmeyin. Biraz dinlensin. Su yorulmuştur.")
    time.sleep(2)
    
    # Çay ekleme
    ciddi_mesaj_yaz("Çay yaprakları ölçülüyor. Bir gram fazla olursa milli felaket.")
    print("Çay miktarı: 3 kaşık (abartılı hassas ölçüm)")
    time.sleep(1)
    
    # Demleme
    ciddi_mesaj_yaz("Demleme başladı. Bu aşama 5-7 dakika sürmelidir. Biz 10 dakika yapacağız çünkü abartıyı severiz.")
    for dakika in range(1, 11):
        print(f"Demleme süresi: {dakika} dakika... Çay düşünüyor.")
        time.sleep(0.5)
        if dakika == 5:
            print("Uyarı: Çay biraz acılaşmaya başladı. Ama biz ciddiyiz, devam.")
    
    # Sonuç
    acilik = random.randint(1, 10)
    ciddi_mesaj_yaz(f"Çay hazır! Acılık seviyesi: {acilik}/10")
    
    if acilik > 7:
        print("SONUÇ: Bu çay çok acı. Komşuya ikram etmeyin, kavga çıkar.")
    else:
        print("SONUÇ: Mükemmel çay. İmparatorluklar böyle çaylarla yükseldi.")
    
    # Gizli politik not (base64 benzeri ama basit)
    # Gizli: Kayyumlar da bazen çay demler, suyu kaynatma.
    print("\n--- Operasyon tamamlandı. Çayınızı afiyetle için. ---")

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n\u00c7ay demleme yarıda kesildi. Bu kabul edilemez!")
        sys.exit(1)
