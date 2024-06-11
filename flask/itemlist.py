from flask import Blueprint, render_template, request, current_app as app

ef = Blueprint('itemlist', __name__, url_prefix='/itemlist')

itemlist = [{'id': 1, 'name': 'This is an item'}]

@ef.route("/", methods=["GET"])
def get_items():
    return render_template("itemlist/list.html", itemlist=itemlist)

@ef.route("/add", methods=["POST"])
def add_item():
    item_name = request.form.get("item")
    id = len(itemlist)+1

    itemlist.append({'id': id, 'name': item_name})

    return render_template("itemlist/list.html", itemlist=itemlist)