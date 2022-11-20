from flask import Flask, render_template, redirect, url_for, request
from pyscrs.getProducts import getRandomProducts, getProductInfo


app = Flask("__name__")
app.secret_key = "437437437437"

@app.route("/")
def mainPage():
    numProdsToGet = 8
    randProds, prodCosts, prodType, prdName = getRandomProducts(num=numProdsToGet)
    return render_template("home.html", numPrds=numProdsToGet, prods=randProds,
                                        costs=prodCosts, prdType=prodType, prdName=prdName
    )

@app.route("/placeorder/<prodId>")
def placeOrder(prodId):
    prdCost, prdType, prdName, prdDesc, decLen = getProductInfo(int(prodId))
    return render_template("placeOrder.html", id=prodId,
                            prdCost=prdCost, prdType=prdType, prdName=prdName, prdDesc=prdDesc, decLen=decLen
    )

@app.route("/orderPlaced", methods=["GET", "POST"])
def orderPlaced():
    if request.method == "POST":
        prdId = request.form["PRDID"]
        prdType = request.form["TYPE"]
        prdName = request.form["NAME"]
        usrName = request.form["USRNAME"]
        usrAddr = request.form["ADDRESS"]
        usrPhno = request.form["PHNO"]
        usrEmil = request.form["EMAILID"]
        prdCost = request.form["PRDCOST"]
        return render_template("orderPlaced.html", prdCost=prdCost, prdId=prdId, prdName=prdName, prdType=prdType,
                                                    usrName=usrName, usrAddr=usrAddr, usrPhno=usrPhno, usrEmil=usrEmil
        )

@app.route("/products")
def allProducts():
    numProdsToGet = 14
    randProds, prodCosts, prodType, prdName = getRandomProducts(num=numProdsToGet)
    return render_template("allProducts.html", numPrds=numProdsToGet, prods=randProds,
                                        costs=prodCosts, prdType=prodType, prdName=prdName
    )


if '__main__' == __name__:
    app.run(debug=True)