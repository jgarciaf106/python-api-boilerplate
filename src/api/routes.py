"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Category, Product
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# create user
@api.route("/createuser", methods=['POST'])
def create_user():

    username = request.json.get("username", None)
    name = request.json.get("name", None)
    password = request.json.get("password", None)

    if not username:
        return jsonify({"msg": "Please provide a valid username."}), 400
    if not name:
        return jsonify({"msg": "Please provide a valid full name."}), 400
    if not password:
        return jsonify({"msg": "Please provide a valid password."}), 400
    
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return jsonify({"msg": "User already exists."}), 401
    else:
        new_user = User()
        new_user.username = username
        new_user.name = name
        new_user.password = password
        new_user.is_active = True

        db.session.add(new_user)
        db.session.commit()
    return jsonify({"msg": "User account was successfully created."}), 200

# create new product
@api.route("/createproduct", methods=["POST"])
def new_product():
    prod_code = request.json.get("prodcode", None)
    prod_cat_code= request.json.get("productcatcode", None)
    prod_description = request.json.get("description", None)
    
    if not prod_code :
        return jsonify({"msg": "Please enter a valid product code."}), 400
    if not prod_cat_code:
        return jsonify({"msg": "Please enter a valid product category code"}), 400
    if not prod_description:
        return jsonify({"msg": "Please enter a valid product description."}), 400
    else:
        new_product = Product()
        new_product.prod_code = prod_code
        new_product.cat_code = prod_cat_code
        new_product.description = prod_description

        db.session.add(new_product)
        db.session.commit()
        return jsonify({"msg": "The product has being successfully created."}), 200

# create new category
@api.route("/createcategory", methods=["POST"])
def new_category():
    cat_code = request.json.get("catcode", None)
    cat_description = request.json.get("description", None)
    
    if not cat_code :
        return jsonify({"msg": "Please enter a valid category code."}), 400
    if not cat_description:
        return jsonify({"msg": "Please enter a valid category description."}), 400
    else:
        new_category = Category()
        new_category.cat_code = cat_code
        new_category.description = cat_description

        db.session.add(new_category)
        db.session.commit()
        return jsonify({"msg": "The Category has being successfully created."}), 200
    
# update user
@api.route("/updateuser/<id>", methods=["PUT"])
def update_user(id):
    user_name = request.json.get("username", None)
    name = request.json.get("name", None)
    password = request.json.get("password", None)

    if user_name is None:
        return jsonify({"msg": "Please provide a valid user name."}), 400
    if name is None:
        return jsonify({"msg": "Please enter a valid full name."}), 400
    if password is None:
        return jsonify({"msg": "Please enter a valid password."}), 400

    update_user = User.query.filter_by(id=id).first()
    update_user.username = user_name
    update_user.name = name
    update_user.password = password

    db.session.commit()
    return jsonify({"msg": "The user has being successfully updated."}), 200

# update product
@api.route("/updateproduct/<id>", methods=["PUT"])
def update_product(id):
    prod_code = request.json.get("prodcode", None)
    prod_cat_code= request.json.get("productcatcode", None)
    prod_description = request.json.get("description", None)

    if prod_code is None:
        return jsonify({"msg": "Please provide a valid Product Code."}), 400
    if prod_cat_code is None:
        return jsonify({"msg": "Please enter a valid product category code."}), 400
    if prod_description is None:
        return jsonify({"msg": "Please enter a valid prodcut description."}), 400

    update_product = Product.query.filter_by(id=id).first()
    update_product.prod_code = prod_code
    update_product.cat_code = prod_cat_code
    update_product.description = prod_description

    db.session.commit()
    return jsonify({"msg": "The product has being successfully updated."}), 200

# update category
@api.route("/updatecategory/<id>", methods=["PUT"])
def update_category(id):
    cat_code = request.json.get("catcode", None)
    cat_description = request.json.get("description", None)

    if cat_code is None:
        return jsonify({"msg": "Please enter a valid category code."}), 400
    if cat_description is None:
        return jsonify({"msg": "Please enter a valid category description."}), 400

    update_category = Category.query.filter_by(id=id).first()
    update_category.cat_code = cat_code
    update_category.description = cat_description
    
    db.session.commit()
    return jsonify({"msg": "The category has being successfully updated."}), 200

# delete user
@api.route("/deleteuser/<id>", methods=["DELETE"])
def delete_user(id):
    del_user = User.query.get(id)
    
    if del_user is None:
        raise APIException("There is not user to delete", status_code=404)

    db.session.delete(del_user)
    db.session.commit()
    return jsonify({"msg": "The user has being successfully deleted."}), 200

# delete product
@api.route("/deleteproduct/<id>", methods=["DELETE"])
def delete_product(id):
    del_product = Product.query.get(id)
    
    if del_product is None:
        raise APIException("There is not product to delete", status_code=404)

    db.session.delete(del_product)
    db.session.commit()
    return jsonify({"msg": "The product has being successfully deleted."}), 200

# delete category
@api.route("/deletecategory/<id>", methods=["DELETE"])
def delete_category(id):
    del_category = Category.query.get(id)
    
    if del_category is None:
        raise APIException("There is not category to delete", status_code=404)

    db.session.delete(del_category)
    db.session.commit()
    return jsonify({"msg": "The category has being successfully deleted."}), 200

# get all products
@api.route('/getproducts', methods=['GET'])
def get_products():  
    products = Product.query.all()
    products = list(map(lambda prd : prd.serialize(), products))  
    
    return jsonify({"results": products, "message": "Inventory Products"}), 200


# get all categories
@api.route('/getcategories', methods=['GET'])
def get_categories():  
    categories = Product.query.all()
    categories = list(map(lambda cat : cat.serialize(), categories))  
    
    return jsonify({"results": categories, "message": "inventory Categories"}), 200