from flask import Flask, render_template, request

app = Flask(__name__)

inventory = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_item", methods=["POST"])
def add_item_route():
    item_name = request.form["item_name"]
    quantity = int(request.form["quantity"])
    add_item(inventory, item_name, quantity)
    return "Товар успешно добавлен"

@app.route("/remove_item", methods=["POST"])
def remove_item_route():
    item_name = request.form["item_name"]
    quantity = int(request.form["quantity"])
    remove_item(inventory, item_name, quantity)
    return "Товар успешно удален"

def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def remove_item(inventory, item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            if inventory[item_name] == 0:
                del inventory[item_name]
        else:
            return "На складе недостаточно товара"
    else:
        return "Товар не найден на складе"

if __name__ == "__main__":
    app.run(debug=True)
