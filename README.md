# MtG-HighRes-ProxyMaker
High resolution proxy card generator script for Magic: The Gathering

ProxyMaker.py generates .pdf files of magic cards based on a list of cards for the purpose of proxying cubes or magic decks. Unlike other proxy making tools, this script will always grab the highest quality card version.

ProxyMaker.py creates one pdf file with 9 cards per page.

ProxyMaker.py requires one file in the same folder named proxy_list.txt with the following format:

1x Sol Ring (c19)
3x Seven Dwarves (eld)
1x Fire // Ice (mb1)
etc.

This is the same format as the 3rd option available in exporting a deck from https://archidekt.com/ (1x Card Name (code) *F*.....). Please use this option to avoid any strange behaviour (the api requests do some string manipulation which might break if the format is not what is expected).

Please remove any accents from card names (For example Barad-dûr should be enetered as Barad-dur), the scryfall API seems to poorly handle these.

Requirements:
Python 3.11.4
Scrython 1.11.0 (may break if Scryfall changes their API)
fpdf 1.7.2

