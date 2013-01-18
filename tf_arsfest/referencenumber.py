#!/usr/bin/env python
# -*- coding: utf-8 -*-
# viitenumero.py

# Original code from: http://www.ohjelmointiputka.net/koodivinkit/26782-viitenumerolaskuri

def viitenumeron_tarkiste(viitenumero_raaka):
    """palauta annetun tarkisteettoman viitenumeron perään kuuluva tarkistenumero"""
    kertoimet = (7, 3, 1)
    viitenumero_raaka = viitenumero_raaka.replace(' ', '')
    nrot_kaanteinen = map(int, viitenumero_raaka[::-1])
    tulosumma = sum(kertoimet[i % 3] * x for i, x in enumerate(nrot_kaanteinen))
    return (10 - (tulosumma % 10)) % 10

def viitenumero_ok(viitenumero):
    """tarkista vastaako lopun tarkistenumero viitenumeron alkuosaa"""
    return viitenumeron_tarkiste(viitenumero[:-1]) == int(viitenumero[-1])

def jaa_ryhmiin_oikealta(s, n):
    """palauta merkkijono s eroteltuna n merkin ryhmiin, välilyönti erottaa

    Ryhmittely aloitetaan oikeasta reunasta.
    Esimerkki: s='1234567890', n=4 palauttaa '12 3456 7890'

    """
    kaannetty = s[::-1]
    osat = [(' ' if i and i % n == 0 else '') + c for i, c in enumerate(kaannetty)]
    return ''.join(osat)[::-1]

def testit():
    assert viitenumeron_tarkiste('1662') == 5
    assert viitenumero_ok('16625')
    assert jaa_ryhmiin_oikealta('966846848', 5) == '9668 46848'
    print('testit ok')

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        # oleta argumentiksi viitenumero ilman tarkistetta, tulosta tarkisteen kanssa
        viite_raaka = argv[-1]
        tarkiste = viitenumeron_tarkiste(viite_raaka)
        viite = viite_raaka + str(tarkiste)
        print(jaa_ryhmiin_oikealta(viite, 5))
    else:
        testit()
        print('Anna argumenttina viitenumero ilman tarkistetta')