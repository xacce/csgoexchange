from csgoexchange.price_list import PriceList

for item in PriceList().prices():
    print item.name, item.price
