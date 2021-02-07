with open("final.csv", encoding="utf8") as chib:
    cu = chib.read()

    changes = cu.split("\n")

    outlist = []


    def corrections(text):
        for x in changes:
            xlist = x.split(",")
            # print(xlist)

            xlist[1] = xlist[1].replace("Language", "ID_in_Source")
            xlist[1] = xlist[1].replace("Mískito", "Mi")
            xlist[1] = xlist[1].replace("Ika", "Ica")
            xlist[1] = xlist[1].replace("Arhuaco", "Ica")

            xlist[1] = xlist[1].replace("Chimila", "Chi")
            xlist[1] = xlist[1].replace("Chibcha", "Mu")
            xlist[1] = xlist[1].replace("Barí", "Ba")
            xlist[1] = xlist[1].replace("Buglere", "Boc")
            xlist[1] = xlist[1].replace("Boruca", "Bor")
            xlist[1] = xlist[1].replace("Bribri", "Bri")
            xlist[1] = xlist[1].replace("Buglere", "Boc")
            xlist[1] = xlist[1].replace("Cabécar", "Cab")
            xlist[1] = xlist[1].replace("Central Tunebo", "Tun")
            xlist[1] = xlist[1].replace("Cogui", "Co")
            xlist[1] = xlist[1].replace("Cogui", "Co")
            xlist[1] = xlist[1].replace("Dorasque", "Dor")
            xlist[1] = xlist[1].replace("Damana", "Da") # Malayo
            xlist[1] = xlist[1].replace("Maléku Jaíka", "Gua")
            xlist[1] = xlist[1].replace("Ngäbere", "Mo")
            xlist[1] = xlist[1].replace("Rama", "Ra")
            xlist[1] = xlist[1].replace("Pech", "Pa")  # Pech
            xlist[1] = xlist[1].replace("Paya", "Pa")  # Pech
            xlist[1] = xlist[1].replace("San Blas Kuna", "Cu")
            xlist[1] = xlist[1].replace("Teribe", "Te")
            xlist[1] = xlist[1].replace("Kankuamo", "At")

            xlist[1] = xlist[1].replace("Atanque", "At")
            xlist[1] = xlist[1].replace("Lenca-Salvador", "LS")
            xlist[1] = xlist[1].replace("Lenca-Honduras", "LH")
            xlist[1] = xlist[1].replace("Cacaopera", "Ca")
            xlist[1] = xlist[1].replace("Mayangna", "Su")
            xlist[1] = xlist[1].replace("Ulua", "Ul") # Ulwa
            xlist[1] = xlist[1].replace("Ulwa", "Ul") # Ulwa


            xlist = ",".join(xlist)
            outlist.append(xlist)

        return outlist

    corrections(changes)
    exhst = "\n".join(outlist)
    print(exhst)
    f = open("new_final.csv", "w",  encoding="utf-8")
    f.write("" + exhst)
