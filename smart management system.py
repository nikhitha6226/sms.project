from tkinter import *
from tkinter import messagebox
import random
import time
import datetime
import os
import tempfile

root = Tk()
root.geometry("1700x800+0+0")
root.title("Cafe System")
root.configure(background='white')

#photo = PhotoImage(file="C:\Users\gudimalla\Desktop\icon_coffee.jpg")
#root.iconphoto(False,photo)

Tops = Frame(root, width=1700, height=20, bd=4, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=1050, height=650, bd=2, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=350, height=650, bd=2, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=1050, height=330, bd=2, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=1050, height=300, bd=2, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width=350, height=650, bd=2, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=350, height=50, bd=2, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=300, height=450, bd=2, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=450, bd=2, relief="raise")
f1ab.pack(side=RIGHT)

f1ac = Frame(f1a, width=350, height=450, bd=2, relief="raise")
f1ac.pack(side=RIGHT)

f2aa = Frame(f2a, width=525, height=200, bd=2, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=525, height=200, bd=2, relief="raise")
f2ab.pack(side=RIGHT)

lblInfo = Label(Tops, font=('calibri', 40, 'bold'),
                text="                                 CAFE MANAGEMENT SYSTEM                                            ",
                bd=10)
lblInfo.grid(row=0, column=0)


# -----------------------------------Functions------------------

def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit")
    if qExit > 0:
        root.destroy()
        return


def Reset():
    PaidTax.set("")
    CostofHotDrinks.set("")
    CostofDesserts.set("")
    CostofColdDrinks.set("")
    SubTotal.set("")
    Total.set("")
    txtReceipt.delete("1.0", END)

    E_Americano.set("0")
    E_Espresso.set("0")
    E_GreenTea.set("0")
    E_CafeLate.set("0")
    E_Doppio.set("0")
    E_LatteMachhiato.set("0")
    E_LongBlack.set("0")
    E_HotChocolate.set("0")
    E_CaramelMacciato.set("0")
    E_DrippCoffee.set("0")
    E_WhiteChocolate.set("0")
    E_BlackTea.set("0")

    E_Icecreams.set("0")
    E_DesertNaches.set("0")
    E_ApplePie.set("0")
    E_TripleChocolate.set("0")
    E_CheeseCake.set("0")
    E_Tiramisu.set("0")
    E_MeringueCheesecake.set("0")
    E_WarmApplePie.set("0")
    E_Sorbet.set("0")
    E_BananasFasterPie.set("0")
    E_ChocolateFondue.set("0")
    E_CoconutCake.set("0")

    E_CafeFrappe.set("0")
    E_Smoothie.set("0")
    E_IeedLate.set("0")
    E_OreoCappuccino.set("0")
    E_ChocMint.set("0")
    E_Cappuccino.set("0")
    E_Mocha.set("0")
    E_IeedMocha.set("0")
    E_HardRock.set("0")
    E_FrozenMacha.set("0")
    E_FrozenLatten.set("0")
    E_CreamyChocolateCoffee.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")

    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")
    var17.set("0")
    var18.set("0")
    var19.set("0")
    var20.set("0")
    var21.set("0")
    var22.set("0")
    var23.set("0")
    var24.set("0")

    var25.set("0")
    var26.set("0")
    var27.set("0")
    var28.set("0")
    var29.set("0")
    var30.set("0")
    var31.set("0")
    var32.set("0")
    var33.set("0")
    var34.set("0")
    var35.set("0")
    var36.set("0")

    # -----------------------Cofigure State

    txtAmericano.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtGreenTea.configure(state=DISABLED)
    txtCafeLate.configure(state=DISABLED)
    txtDoppio.configure(state=DISABLED)
    txtLatteMachhiato.configure(state=DISABLED)
    txtLongBlack.configure(state=DISABLED)
    txtHotChocolate.configure(state=DISABLED)
    txtCaramelMacciato.configure(state=DISABLED)
    txtDrippCoffee.configure(state=DISABLED)
    txtWhiteChocolate.configure(state=DISABLED)
    txtBlackTea.configure(state=DISABLED)

    txtIcecreams.configure(state=DISABLED)
    txtDesertNaches.configure(state=DISABLED)
    txtApplePie.configure(state=DISABLED)
    txtTripleChocolate.configure(state=DISABLED)
    txtCheeseCake.configure(state=DISABLED)
    txtTiramisu.configure(state=DISABLED)
    txtMeringueCheesecake.configure(state=DISABLED)
    txtWarmApplePie.configure(state=DISABLED)
    txtSorbet.configure(state=DISABLED)
    txtBananasFasterPie.configure(state=DISABLED)
    txtChocolateFondue.configure(state=DISABLED)
    txtCoconutCake.configure(state=DISABLED)

    txtCafeFrappe.configure(state=DISABLED)
    txtSmoothie.configure(state=DISABLED)
    txtIeedLate.configure(state=DISABLED)
    txtOreoCappuccino.configure(state=DISABLED)
    txtChocMint.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtIeedMocha.configure(state=DISABLED)
    txtHardRock.configure(state=DISABLED)
    txtFrozenMacha.configure(state=DISABLED)
    txtFrozenLatten.configure(state=DISABLED)
    txtCreamyChocolateCoffee.configure(state=DISABLED)


def chkbutton_value():
    if (var1.get() == 1):
        txtAmericano.configure(state=NORMAL)
    elif var1.get() == 0:
        txtAmericano.configure(state=DISABLED)
        E_Americano.set("0")
    if (var2.get() == 1):
        txtEspresso.configure(state=NORMAL)
    elif var2.get() == 0:
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
    if var3.get() == 1:
        txtGreenTea.configure(state=NORMAL)
    elif var3.get() == 0:
        txtGreenTea.configure(state=DISABLED)
        E_GreenTea.set("0")
    if var4.get() == 1:
        txtCafeLate.configure(state=NORMAL)
    elif var4.get() == 0:
        txtCafeLate.configure(state=DISABLED)
        E_CafeLate.set("0")
    if var5.get() == 1:
        txtDoppio.configure(state=NORMAL)
    elif var5.get() == 0:
        txtDoppio.configure(state=DISABLED)
        E_Doppio.set("0")
    if var6.get() == 1:
        txtLatteMachhiato.configure(state=NORMAL)
    elif var6.get() == 0:
        txtLatteMachhiato.configure(state=DISABLED)
        E_LatteMachhiato.set("0")
    if var7.get() == 1:
        txtLongBlack.configure(state=NORMAL)
    elif var7.get() == 0:
        txtLongBlack.configure(state=DISABLED)
        E_LongBlack.set("0")
    if var8.get() == 1:
        txtHotChocolate.configure(state=NORMAL)
    elif var8.get() == 0:
        txtHotChocolate.configure(state=DISABLED)
        E_HotChocolate.set("0")
    if var9.get() == 1:
        txtCaramelMacciato.configure(state=NORMAL)
    elif var9.get() == 0:
        txtCaramelMacciato.configure(state=DISABLED)
        E_CaramelMacciato.set("0")
    if var10.get() == 1:
        txtDrippCoffee.configure(state=NORMAL)
    elif var10.get() == 0:
        txtDrippCoffee.configure(state=DISABLED)
        E_DrippCoffee.set("0")
    if var11.get() == 1:
        txtWhiteChocolate.configure(state=NORMAL)
    elif var11.get() == 0:
        txtWhiteChocolate.configure(state=DISABLED)
        E_WhiteChocolate.set("0")
    if var12.get() == 1:
        txtBlackTea.configure(state=NORMAL)
    elif var12.get() == 0:
        txtBlackTea.configure(state=DISABLED)
        E_BlackTea.set("0")

    if var13.get() == 1:
        txtIcecreams.configure(state=NORMAL)
    elif var13.get() == 0:
        txtIcecreams.configure(state=DISABLED)
        E_Icecreams.set("0")
    if var14.get() == 1:
        txtDesertNaches.configure(state=NORMAL)
    elif var14.get() == 0:
        txtDesertNaches.configure(state=DISABLED)
        E_DesertNaches.set("0")
    if var15.get() == 1:
        txtApplePie.configure(state=NORMAL)
    elif var15.get() == 0:
        txtApplePie.configure(state=DISABLED)
        E_ApplePie.set("0")
    if var16.get() == 1:
        txtTripleChocolate.configure(state=NORMAL)
    elif var16.get() == 0:
        txtTripleChocolate.configure(state=DISABLED)
        E_TripleChocolate.set("0")
    if var17.get() == 1:
        txtCheeseCake.configure(state=NORMAL)
    elif var17.get() == 0:
        txtCheeseCake.configure(state=DISABLED)
        E_CheeseCake.set("0")
    if var18.get() == 1:
        txtTiramisu.configure(state=NORMAL)
    elif var18.get() == 0:
        txtTiramisu.configure(state=DISABLED)
        E_Tiramisu.set("0")
    if var19.get() == 1:
        txtMeringueCheesecake.configure(state=NORMAL)
    elif var19.get() == 0:
        txtMeringueCheesecake.configure(state=DISABLED)
        E_MeringueCheesecake.set("0")
    if var20.get() == 1:
        txtWarmApplePie.configure(state=NORMAL)
    elif var20.get() == 0:
        txtWarmApplePie.configure(state=DISABLED)
        E_WarmApplePie.set("0")
    if var21.get() == 1:
        txtSorbet.configure(state=NORMAL)
    elif var21.get() == 0:
        txtSorbet.configure(state=DISABLED)
        E_Sorbet.set("0")
    if var22.get() == 1:
        txtBananasFasterPie.configure(state=NORMAL)
    elif var22.get() == 0:
        txtBananasFasterPie.configure(state=DISABLED)
        E_BananasFasterPie.set("0")
    if var23.get() == 1:
        txtChocolateFondue.configure(state=NORMAL)
    elif var23.get() == 0:
        txtChocolateFondue.configure(state=DISABLED)
        E_ChocolateFondue.set("0")
    if var24.get() == 1:
        txtCoconutCake.configure(state=NORMAL)
    elif var24.get() == 0:
        txtCoconutCake.configure(state=DISABLED)
        E_CoconutCake.set("0")

    if var25.get() == 1:
        txtCafeFrappe.configure(state=NORMAL)
    elif var25.get() == 0:
        txtCafeFrappe.configure(state=DISABLED)
        E_CafeFrappe.set("0")
    if var26.get() == 1:
        txtSmoothie.configure(state=NORMAL)
    elif var26.get() == 0:
        txtSmoothie.configure(state=DISABLED)
        E_Smoothie.set("0")
    if var27.get() == 1:
        txtIeedLate.configure(state=NORMAL)
    elif var27.get() == 0:
        txtIeedLate.configure(state=DISABLED)
        E_IeedLate.set("0")
    if var28.get() == 1:
        txtOreoCappuccino.configure(state=NORMAL)
    elif var28.get() == 0:
        txtOreoCappuccino.configure(state=DISABLED)
        E_OreoCappuccino.set("0")
    if var29.get() == 1:
        txtChocMint.configure(state=NORMAL)
    elif var29.get() == 0:
        txtChocMint.configure(state=DISABLED)
        E_ChocMint.set("0")
    if var30.get() == 1:
        txtCappuccino.configure(state=NORMAL)
    elif var30.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")
    if var31.get() == 1:
        txtMocha.configure(state=NORMAL)
    elif var31.get() == 0:
        txtMocha.configure(state=DISABLED)
        E_Mocha.set("0")
    if var32.get() == 1:
        txtIeedMocha.configure(state=NORMAL)
    elif var32.get() == 0:
        txtIeedMocha.configure(state=DISABLED)
        E_IeedMocha.set("0")
    if var33.get() == 1:
        txtHardRock.configure(state=NORMAL)
    elif var33.get() == 0:
        txtHardRock.configure(state=DISABLED)
        E_HardRock.set("0")
    if var34.get() == 1:
        txtFrozenMacha.configure(state=NORMAL)
    elif var34.get() == 0:
        txtFrozenMacha.configure(state=DISABLED)
        E_FrozenMacha.set("0")
    if var35.get() == 1:
        txtFrozenLatten.configure(state=NORMAL)
    elif var35.get() == 0:
        txtFrozenLatten.configure(state=DISABLED)
        E_FrozenLatten.set("0")
    if var36.get() == 1:
        txtCreamyChocolateCoffee.configure(state=NORMAL)
    elif var36.get() == 0:
        txtCreamyChocolateCoffee.configure(state=DISABLED)
        E_CreamyChocolateCoffee.set("0")

def CostofItem():
    Item1 = float(E_Americano.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_GreenTea.get())
    Item4 = float(E_CafeLate.get())
    Item5 = float(E_Doppio.get())
    Item6 = float(E_LatteMachhiato.get())
    Item7 = float(E_LongBlack.get())
    Item8 = float(E_HotChocolate.get())
    Item9 = float(E_CaramelMacciato.get())
    Item10 = float(E_DrippCoffee.get())
    Item11 = float(E_WhiteChocolate.get())
    Item12 = float(E_BlackTea.get())

    Item13 = float(E_Icecreams.get())
    Item14 = float(E_DesertNaches.get())
    Item15 = float(E_ApplePie.get())
    Item16 = float(E_TripleChocolate.get())
    Item17 = float(E_CheeseCake.get())
    Item18 = float(E_Tiramisu.get())
    Item19 = float(E_MeringueCheesecake.get())
    Item20 = float(E_WarmApplePie.get())
    Item21 = float(E_Sorbet.get())
    Item22 = float(E_BananasFasterPie.get())
    Item23 = float(E_ChocolateFondue.get())
    Item24 = float(E_CoconutCake.get())

    Item25 = float(E_CafeFrappe.get())
    Item26 = float(E_Smoothie.get())
    Item27 = float(E_IeedLate.get())
    Item28 = float(E_OreoCappuccino.get())
    Item29 = float(E_ChocMint.get())
    Item30 = float(E_Cappuccino.get())
    Item31 = float(E_Mocha.get())
    Item32 = float(E_IeedMocha.get())
    Item33 = float(E_HardRock.get())
    Item34 = float(E_FrozenMacha.get())
    Item35 = float(E_FrozenLatten.get())
    Item36 = float(E_CreamyChocolateCoffee.get())

    PriceofHotDrinks = (Item1 * 120) + (Item2 * 110) + (Item3 * 80) + (Item4 * 160) + (Item5 * 50) + (Item6 * 70) + (
                Item7 * 100) + (Item8 * 110) + (Item9 * 150) + (Item10 * 60) + (Item11 * 70) + (Item12 * 50)

    PriceofDesserts = (Item13 * 150) + (Item14 * 200) + (Item15 * 170) + (Item16 * 300) + (Item17 * 300) + (
                Item18 * 200) + (Item19 * 250) + (Item20 * 200) + (Item21 * 280) + (Item22 * 100) + (Item23 * 200) + (
                                  Item24 * 150)

    PriceofColdDrinks = (Item25 * 70) + (Item26 * 200) + (Item27 * 300) + (Item28 * 120) + (Item29 * 250) + (
                Item30 * 350) + (Item31 * 120) + (Item32 * 80) + (Item33 * 150) + (Item34 * 150) + (Item35 * 120) + (
                                    Item36 * 200)

    HotDrinksPrice = "₹", str("%.2f" % (PriceofHotDrinks))
    DessertsPrice = "₹", str("%.2f" % (PriceofDesserts))
    ColdDrinksPrice = "₹", str("%.2f" % (PriceofColdDrinks))
    CostofHotDrinks.set(HotDrinksPrice)
    CostofDesserts.set(DessertsPrice)
    CostofColdDrinks.set(ColdDrinksPrice)


    Sub = float("%.2f"%((PriceofHotDrinks + PriceofDesserts + PriceofColdDrinks) / 16.66666666))

    SubTotalofItems = "₹", str("%.2f" % (PriceofHotDrinks + PriceofDesserts + PriceofColdDrinks))
    SubTotal.set(SubTotalofItems)

    Paid = Sub
    PaidTax.set(Paid)
    TC = "₹", str("%.2f" % (PriceofHotDrinks + PriceofDesserts + PriceofColdDrinks + Paid))
    Total.set(TC)


def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t' + Receipt_Ref.get() + '\t' + DateofOrder.get() + '\n')
    txtReceipt.insert(END, "Items\t\t\t" + "Quantity\t\n")
    txtReceipt.insert(END, "Americano-₹120\t\t\t" + E_Americano.get() + "\n")
    txtReceipt.insert(END, "Espresso-₹110\t\t\t" + E_Espresso.get() + "\n")
    txtReceipt.insert(END, "Green Tea-₹80\t\t\t" + E_GreenTea.get() + "\n")
    txtReceipt.insert(END, "Cafe Late-₹160\t\t\t" + E_CafeLate.get() + "\n")
    txtReceipt.insert(END, "Doppio-₹50\t\t\t" + E_Doppio.get() + "\n")
    txtReceipt.insert(END, "Late Machhiato-₹70\t\t\t" + E_LatteMachhiato.get() + "\n")
    txtReceipt.insert(END, "Long Black-₹100\t\t\t" + E_LongBlack.get() + "\n")
    txtReceipt.insert(END, "Hot Chocolate-₹110\t\t\t" + E_HotChocolate.get() + "\n")
    txtReceipt.insert(END, "Caramel Macciato-₹150\t\t\t" + E_CaramelMacciato.get() + "\n")
    txtReceipt.insert(END, "Dripp Coffee-₹60\t\t\t" + E_DrippCoffee.get() + "\n")
    txtReceipt.insert(END, "White Chocolate-₹70\t\t\t" + E_WhiteChocolate.get() + "\n")
    txtReceipt.insert(END, "Black Tea-₹50\t\t\t" + E_BlackTea.get() + "\n")

    txtReceipt.insert(END, "Ice Creams-₹150\t\t\t" + E_Icecreams.get() + "\n")
    txtReceipt.insert(END, "Desert Naches-₹200\t\t\t" + E_DesertNaches.get() + "\n")
    txtReceipt.insert(END, "Apple Pie-₹170\t\t\t" + E_ApplePie.get() + "\n")
    txtReceipt.insert(END, "Triple Chccolate-₹300\t\t\t" + E_TripleChocolate.get() + "\n")
    txtReceipt.insert(END, "Cheese Cake-₹300\t\t\t" + E_CheeseCake.get() + "\n")
    txtReceipt.insert(END, "Tiramisu-₹200\t\t\t" + E_Tiramisu.get() + "\n")
    txtReceipt.insert(END, "Meringue Cake-₹250\t\t\t" + E_MeringueCheesecake.get() + "\n")
    txtReceipt.insert(END, "Warm Apple Pie-₹200\t\t\t" + E_WarmApplePie.get() + "\n")
    txtReceipt.insert(END, "Sorbet-₹280\t\t\t" + E_Sorbet.get() + "\n")
    txtReceipt.insert(END, "Bananas Faster Pie-₹100\t\t\t" + E_BananasFasterPie.get() + "\n")
    txtReceipt.insert(END, "Chocolate Fondue-₹200\t\t\t" + E_ChocolateFondue.get() + "\n")
    txtReceipt.insert(END, "Coconut Cake-₹150\t\t\t" + E_CoconutCake.get() + "\n")

    txtReceipt.insert(END, "Cafe Frappe-₹70\t\t\t" + E_CafeFrappe.get() + "\n")
    txtReceipt.insert(END, "Smoothie-₹200\t\t\t" + E_Smoothie.get() + "\n")
    txtReceipt.insert(END, "Ieed Late-₹300\t\t\t" + E_IeedLate.get() + "\n")
    txtReceipt.insert(END, "Oreo Cappuccino-₹120\t\t\t" + E_OreoCappuccino.get() + "\n")
    txtReceipt.insert(END, "Choc Mint-₹250\t\t\t" + E_ChocMint.get() + "\n")
    txtReceipt.insert(END, "Cappuccino-₹350\t\t\t" + E_Cappuccino.get() + "\n")
    txtReceipt.insert(END, "Mocha-₹120\t\t\t" + E_Mocha.get() + "\n")
    txtReceipt.insert(END, "Ieed Mocha-₹80\t\t\t" + E_IeedMocha.get() + "\n")
    txtReceipt.insert(END, "Hard Rock-₹150\t\t\t" + E_HardRock.get() + "\n")
    txtReceipt.insert(END, "Frozen Macha-₹150\t\t\t" + E_FrozenMacha.get() + "\n")
    txtReceipt.insert(END, "Frozen Latten-₹120\t\t\t" + E_FrozenLatten.get() + "\n")
    txtReceipt.insert(END, "Creamy Choco Cake-₹200\t\t\t" + E_CreamyChocolateCoffee.get() + "\n")

    txtReceipt.insert(END, "Cost of Hot Drinks:\t\t\t" + CostofHotDrinks.get() + "\n")
    txtReceipt.insert(END, "Cost of Desserts:\t\t\t" + CostofDesserts.get() + "\n")
    txtReceipt.insert(END, "Cost of Cold Drinks\t\t\t" + CostofColdDrinks.get() + "\n")
    txtReceipt.insert(END, "Total Cost\t\t\t" + Total.get() + "\n")


def Print():
    q = txtReceipt.get("1.0", "end-1c")
    r = str(q)
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(r)
    os.startfile(filename, "print")


# -----Hot Drinks Variables

E_Americano = StringVar()
E_Espresso = StringVar()
E_GreenTea = StringVar()
E_CafeLate = StringVar()
E_Doppio = StringVar()
E_LatteMachhiato = StringVar()
E_LongBlack = StringVar()
E_HotChocolate = StringVar()
E_CaramelMacciato = StringVar()
E_DrippCoffee = StringVar()
E_WhiteChocolate = StringVar()
E_BlackTea = StringVar()

# ------Desserts

E_Icecreams = StringVar()
E_DesertNaches = StringVar()
E_ApplePie = StringVar()
E_TripleChocolate = StringVar()
E_CheeseCake = StringVar()
E_Tiramisu = StringVar()
E_MeringueCheesecake = StringVar()
E_WarmApplePie = StringVar()
E_Sorbet = StringVar()
E_BananasFasterPie = StringVar()
E_ChocolateFondue = StringVar()
E_CoconutCake = StringVar()

# ------Cold Drinks

E_CafeFrappe = StringVar()
E_Smoothie = StringVar()
E_IeedLate = StringVar()
E_OreoCappuccino = StringVar()
E_ChocMint = StringVar()
E_Cappuccino = StringVar()
E_Mocha = StringVar()
E_IeedMocha = StringVar()
E_HardRock = StringVar()
E_FrozenMacha = StringVar()
E_FrozenLatten = StringVar()
E_CreamyChocolateCoffee = StringVar()

DateofOrder = StringVar()
CostofHotDrinks = StringVar()
CostofDesserts = StringVar()
CostofColdDrinks = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
Total = StringVar()
Receipt_Ref = StringVar()

# --------------------------------------Variables-------------------------------------

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()

var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()

var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()
var31 = IntVar()
var32 = IntVar()
var33 = IntVar()
var34 = IntVar()
var35 = IntVar()
var36 = IntVar()

DateofOrder.set(time.strftime("%d/%m/%Y"))

E_Americano.set("0")
E_Espresso.set("0")
E_GreenTea.set("0")
E_CafeLate.set("0")
E_Doppio.set("0")
E_LatteMachhiato.set("0")
E_LongBlack.set("0")
E_HotChocolate.set("0")
E_CaramelMacciato.set("0")
E_DrippCoffee.set("0")
E_WhiteChocolate.set("0")
E_BlackTea.set("0")

E_Icecreams.set("0")
E_DesertNaches.set("0")
E_ApplePie.set("0")
E_TripleChocolate.set("0")
E_CheeseCake.set("0")
E_Tiramisu.set("0")
E_MeringueCheesecake.set("0")
E_WarmApplePie.set("0")
E_Sorbet.set("0")
E_BananasFasterPie.set("0")
E_ChocolateFondue.set("0")
E_CoconutCake.set("0")

E_CafeFrappe.set("0")
E_Smoothie.set("0")
E_IeedLate.set("0")
E_OreoCappuccino.set("0")
E_ChocMint.set("0")
E_Cappuccino.set("0")
E_Mocha.set("0")
E_IeedMocha.set("0")
E_HardRock.set("0")
E_FrozenMacha.set("0")
E_FrozenLatten.set("0")
E_CreamyChocolateCoffee.set("0")

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")

var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")
var17.set("0")
var18.set("0")
var19.set("0")
var20.set("0")
var21.set("0")
var22.set("0")
var23.set("0")
var24.set("0")

var25.set("0")
var26.set("0")
var27.set("0")
var28.set("0")
var29.set("0")
var30.set("0")
var31.set("0")
var32.set("0")
var33.set("0")
var34.set("0")
var35.set("0")
var36.set("0")

# -----------------------------------------Hot Drinks--------------------------------------------

lblHot = Label(f1aa, font=('arial', 16, 'bold'), text='          Hot Drinks      ')
lblHot.grid(row=0, sticky=W)
lblHot = Label(f1aa, font=('arial', 14, 'bold'), text='-----------------------------')
lblHot.grid(row=1, sticky=W)

Americano = Checkbutton(f1aa, text="Americano  ", variable=var1, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                        command=chkbutton_value).grid(row=2, sticky=W)
Espresso = Checkbutton(f1aa, text="Espresso ", variable=var2, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=3, sticky=W)
GreenTea = Checkbutton(f1aa, text="Green Tea", variable=var3, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=4, sticky=W)
CafeLate = Checkbutton(f1aa, text="Cafe Late ", variable=var4, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=5, sticky=W)
Doppio = Checkbutton(f1aa, text="Doppio ", variable=var5, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                     command=chkbutton_value).grid(row=6, sticky=W)
LatteMachhiato = Checkbutton(f1aa, text="Latte Machhiato ", variable=var6, onvalue=1, offvalue=0,
                             font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=7, sticky=W)
LongBlack = Checkbutton(f1aa, text="Long Black ", variable=var7, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                        command=chkbutton_value).grid(row=8, sticky=W)
HotChocolate = Checkbutton(f1aa, text="Hot Chocolate ", variable=var8, onvalue=1, offvalue=0,
                           font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=9, sticky=W)
CaraemelMacciato = Checkbutton(f1aa, text="Caramel Macciato", variable=var9, onvalue=1, offvalue=0,
                               font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=10, sticky=W)
DrippCoffee = Checkbutton(f1aa, text="Dripp Coffee ", variable=var10, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                          command=chkbutton_value).grid(row=11, sticky=W)
WhiteChocolate = Checkbutton(f1aa, text="White Chocolate", variable=var11, onvalue=1, offvalue=0,
                             font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=12, sticky=W)
BlackTea = Checkbutton(f1aa, text="Black Tea ", variable=var12, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=13, sticky=W)

# ----------------------------------------Desserts--------------------------------------------

lblHot = Label(f1ac, font=('arial', 16, 'bold'), text='          Desserts      ')
lblHot.grid(row=0, sticky=W)
lblHot = Label(f1ac, font=('arial', 14, 'bold'), text='---------------------------------')
lblHot.grid(row=1, sticky=W)

Icecreams = Checkbutton(f1ac, text="Icecreams ", variable=var13, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                        command=chkbutton_value).grid(row=2, sticky=W)
DesertNaches = Checkbutton(f1ac, text="Desert Naches", variable=var14, onvalue=1, offvalue=0,
                           font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=3, sticky=W)
ApplePie = Checkbutton(f1ac, text="Apple Pie ", variable=var15, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=4, sticky=W)
TripleChocolate = Checkbutton(f1ac, text="Triple Chocolate ", variable=var16, onvalue=1, offvalue=0,
                              font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=5, sticky=W)
CheeseCake = Checkbutton(f1ac, text="Cheese Cake", variable=var17, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                         command=chkbutton_value).grid(row=6, sticky=W)
Tiramisu = Checkbutton(f1ac, text="Tiramisu ", variable=var18, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=7, sticky=W)
MeringueCheeseCake = Checkbutton(f1ac, text="Meringue Cheese Cake", variable=var19, onvalue=1, offvalue=0,
                                 font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=8, sticky=W)
WarmApplePie = Checkbutton(f1ac, text="Warm Apple Pie  ", variable=var20, onvalue=1, offvalue=0,
                           font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=9, sticky=W)
Sorbet = Checkbutton(f1ac, text="Sorbet ", variable=var21, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                     command=chkbutton_value).grid(row=10, sticky=W)
BananasFasterPie = Checkbutton(f1ac, text="Bananas Faster Pie   ", variable=var22, onvalue=1, offvalue=0,
                               font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=11, sticky=W)
ChocolateFondue = Checkbutton(f1ac, text="Chocolate Fondue ", variable=var23, onvalue=1, offvalue=0,
                              font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=12, sticky=W)
CoconutCake = Checkbutton(f1ac, text="Coconut Cake ", variable=var24, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                          command=chkbutton_value).grid(row=13, sticky=W)

# ----------------------------------------Cold Drinks-------------------------------------------------

lblHot = Label(f1ab, font=('arial', 16, 'bold'), text='          Cold Drinks      ')
lblHot.grid(row=0, sticky=W)
lblHot = Label(f1ab, font=('arial', 14, 'bold'), text='-------------------------------')
lblHot.grid(row=1, sticky=W)

CafeFrappe = Checkbutton(f1ab, text="Cafe Frappe ", variable=var25, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                         command=chkbutton_value).grid(row=2, sticky=W)
Smoothie = Checkbutton(f1ab, text="Smoothie", variable=var26, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=3, sticky=W)
IeedLate = Checkbutton(f1ab, text="Ieed Late ", variable=var27, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=4, sticky=W)
OreoCappuccino = Checkbutton(f1ab, text="Oreo Cappuccino ", variable=var28, onvalue=1, offvalue=0,
                             font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=5, sticky=W)
ChocMint = Checkbutton(f1ab, text="Choc Mint ", variable=var29, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=6, sticky=W)
Cappuccino = Checkbutton(f1ab, text="Cappuccino ", variable=var30, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                         command=chkbutton_value).grid(row=7, sticky=W)
Mocha = Checkbutton(f1ab, text="Mocha ", variable=var31, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                    command=chkbutton_value).grid(row=8, sticky=W)
IeedMocha = Checkbutton(f1ab, text="Ieed Mocha", variable=var32, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                        command=chkbutton_value).grid(row=9, sticky=W)
HardRock = Checkbutton(f1ab, text="Hard Rock   ", variable=var33, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                       command=chkbutton_value).grid(row=10, sticky=W)
FrozenMacha = Checkbutton(f1ab, text="Frozen Macha ", variable=var34, onvalue=1, offvalue=0, font=('arial', 14, 'bold'),
                          command=chkbutton_value).grid(row=11, sticky=W)
FrozenLattenLatten = Checkbutton(f1ab, text="Frozen Latten ", variable=var35, onvalue=1, offvalue=0,
                                 font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=12, sticky=W)
CreamyChocolateCoffee = Checkbutton(f1ab, text="Creamy Chocolate ", variable=var36, onvalue=1, offvalue=0,
                                    font=('arial', 14, 'bold'), command=chkbutton_value).grid(row=13, sticky=W)

# --------------------------------------Entry for Hot Drinks-------------------------------------------


txtAmericano = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Americano,
                     state=DISABLED)
txtAmericano.grid(row=2, column=1)
txtEspresso = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Espresso,
                    state=DISABLED)
txtEspresso.grid(row=3, column=1)
txtGreenTea = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_GreenTea,
                    state=DISABLED)
txtGreenTea.grid(row=4, column=1)
txtCafeLate = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_CafeLate,
                    state=DISABLED)
txtCafeLate.grid(row=5, column=1)
txtDoppio = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Doppio,
                  state=DISABLED)
txtDoppio.grid(row=6, column=1)
txtLatteMachhiato = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                          textvariable=E_LatteMachhiato, state=DISABLED)
txtLatteMachhiato.grid(row=7, column=1)
txtLongBlack = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_LongBlack,
                     state=DISABLED)
txtLongBlack.grid(row=8, column=1)
txtHotChocolate = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_HotChocolate,
                        state=DISABLED)
txtHotChocolate.grid(row=9, column=1)
txtCaramelMacciato = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                           textvariable=E_CaramelMacciato, state=DISABLED)
txtCaramelMacciato.grid(row=10, column=1)
txtDrippCoffee = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_DrippCoffee,
                       state=DISABLED)
txtDrippCoffee.grid(row=11, column=1)
txtWhiteChocolate = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                          textvariable=E_WhiteChocolate, state=DISABLED)
txtWhiteChocolate.grid(row=12, column=1)
txtBlackTea = Entry(f1aa, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_BlackTea,
                    state=DISABLED)
txtBlackTea.grid(row=13, column=1)

# ---------------------------------------Entry for Deserts-----------------------------------------


txtCafeFrappe = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_CafeFrappe,
                      state=DISABLED)
txtCafeFrappe.grid(row=2, column=1)
txtSmoothie = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Smoothie,
                    state=DISABLED)
txtSmoothie.grid(row=3, column=1)
txtIeedLate = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_IeedLate,
                    state=DISABLED)
txtIeedLate.grid(row=4, column=1)
txtOreoCappuccino = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                          textvariable=E_OreoCappuccino, state=DISABLED)
txtOreoCappuccino.grid(row=5, column=1)
txtChocMint = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_ChocMint,
                    state=DISABLED)
txtChocMint.grid(row=6, column=1)
txtCappuccino = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Cappuccino,
                      state=DISABLED)
txtCappuccino.grid(row=7, column=1)
txtMocha = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Mocha, state=DISABLED)
txtMocha.grid(row=8, column=1)
txtIeedMocha = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_IeedMocha,
                     state=DISABLED)
txtIeedMocha.grid(row=9, column=1)
txtHardRock = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_HardRock,
                    state=DISABLED)
txtHardRock.grid(row=10, column=1)
txtFrozenMacha = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_FrozenMacha,
                       state=DISABLED)
txtFrozenMacha.grid(row=11, column=1)
txtFrozenLatten = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_FrozenLatten,
                        state=DISABLED)
txtFrozenLatten.grid(row=12, column=1)
txtCreamyChocolateCoffee = Entry(f1ab, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                                 textvariable=E_CreamyChocolateCoffee, state=DISABLED)
txtCreamyChocolateCoffee.grid(row=13, column=1)
# ------------------------------------Others---------------------------------------


txtIcecreams = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Icecreams,
                     state=DISABLED)
txtIcecreams.grid(row=2, column=1)
txtDesertNaches = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_DesertNaches,
                        state=DISABLED)
txtDesertNaches.grid(row=3, column=1)
txtApplePie = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_ApplePie,
                    state=DISABLED)
txtApplePie.grid(row=4, column=1)
txtTripleChocolate = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                           textvariable=E_TripleChocolate, state=DISABLED)
txtTripleChocolate.grid(row=5, column=1)
txtCheeseCake = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_CheeseCake,
                      state=DISABLED)
txtCheeseCake.grid(row=6, column=1)
txtTiramisu = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Tiramisu,
                    state=DISABLED)
txtTiramisu.grid(row=7, column=1)
txtMeringueCheesecake = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                              textvariable=E_MeringueCheesecake, state=DISABLED)
txtMeringueCheesecake.grid(row=8, column=1)
txtWarmApplePie = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_WarmApplePie,
                        state=DISABLED)
txtWarmApplePie.grid(row=9, column=1)
txtSorbet = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_Sorbet,
                  state=DISABLED)
txtSorbet.grid(row=10, column=1)
txtBananasFasterPie = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                            textvariable=E_BananasFasterPie, state=DISABLED)
txtBananasFasterPie.grid(row=11, column=1)
txtChocolateFondue = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left',
                           textvariable=E_ChocolateFondue, state=DISABLED)
txtChocolateFondue.grid(row=12, column=1)
txtCoconutCake = Entry(f1ac, font=('arial', 14, 'bold'), bd=4, width=6, justify='left', textvariable=E_CoconutCake,
                       state=DISABLED)
txtCoconutCake.grid(row=13, column=1)

# ---------------------------------Information---------------------------------------

lblReceipt = Label(ft2, font=('arial', 14, 'bold'), text='Receipt:', bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, font=('arial', 14, 'bold'), bd=3, width=200)
txtReceipt.grid(row=1, column=0)

# ------------------------------Cost Item Information--------------------------------

lblCostofHotDrinks = Label(f2aa, font=('arial', 16, 'bold'), text='Cost of Hot Drinks', bd=8)
lblCostofHotDrinks.grid(row=0, column=0, sticky=W)
txtCostofHotDrinks = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify='left', textvariable=CostofHotDrinks)
txtCostofHotDrinks.grid(row=0, column=1, sticky=W)

lblCostofDesserts = Label(f2aa, font=('arial', 16, 'bold'), text='Cost of Desserts   ', bd=8)
lblCostofDesserts.grid(row=1, column=0, sticky=W)
txtCostofDesserts = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify='left', textvariable=CostofDesserts)
txtCostofDesserts.grid(row=1, column=1, sticky=W)

lblCostofColdDrinks = Label(f2aa, font=('arial', 16, 'bold'), text='Cost of Cold Drinks', bd=8)
lblCostofColdDrinks.grid(row=2, column=0, sticky=W)
txtCostofColdDrinks = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify='left', textvariable=CostofColdDrinks)
txtCostofColdDrinks.grid(row=2, column=1, sticky=W)

# -------------------------------Payment Information------------------------------

lblPaidTax = Label(f2ab, font=('arial', 16, 'bold'), text='Paid Tax   (₹6%)', bd=8)
lblPaidTax.grid(row=0, column=0, sticky=W)
txtPaidTax = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, justify='left', textvariable=PaidTax)
txtPaidTax.grid(row=0, column=1, sticky=W)

lblSubTotal = Label(f2ab, font=('arial', 16, 'bold'), text='Sub Total', bd=8)
lblSubTotal.grid(row=1, column=0, sticky=W)
txtSubTotal = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=1, column=1, sticky=W)

lblTotal = Label(f2ab, font=('arial', 16, 'bold'), text='Total', bd=8)
lblTotal.grid(row=2, column=0, sticky=W)
txtTotal = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, justify='left', textvariable=Total)
txtTotal.grid(row=2, column=1, sticky=W)

# ---------------------------------Button---------------------------------------------

btnTotal = Button(fb2, padx=8, pady=1, bd=2, fg='black', font=('arial', 16, 'bold'), width=5, command=CostofItem,
                  text="Total")
btnTotal.grid(row=0, column=0)
btnReceipt = Button(fb2, padx=8, pady=1, bd=2, fg='black', font=('arial', 16, 'bold'), width=5, command=Receipt,
                    text="Receipt")
btnReceipt.grid(row=0, column=1)
btnReset = Button(fb2, padx=8, pady=1, bd=2, fg='black', font=('arial', 16, 'bold'), width=5, command=Reset,
                  text="Reset")
btnReset.grid(row=0, column=2)
btnPrint = Button(fb2, padx=8, pady=1, bd=2, fg='black', font=('arial', 16, 'bold'), width=5, command=Print,
                  text="Print")
btnPrint.grid(row=0, column=3)
btnExit = Button(fb2, padx=8, pady=1, bd=2, fg='black', font=('arial', 16, 'bold'), width=5, command=qExit, text="Exit")
btnExit.grid(row=0, column=4)


root.mainloop()