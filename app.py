from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import ImmutableMultiDict
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from uuid import uuid4
from bson.json_util import dumps
import datetime
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'GoldOneDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/GoldOneDB'
app.secret_key = 'proseth123'
api = Api(app)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)


class MockProduct(Resource):
    # @jwt_required()
    def get(self):
        return {
            "categories": [
                {
                    "category_id": "001",
                    "category_name": "Desktop",
                    "asset": [{
                        "asset_model": "Acer",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Asus",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Dell",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Asus",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Dell",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    }
                    ]},
                {
                    "category_id": "002",
                    "category_name": "Laptop",
                    "asset": [{
                        "asset_model": "Asus",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Asus",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Dell",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    }
                    ]},
                {
                    "category_id": "003",
                    "category_name": "Accessory",
                    "asset": [{
                        "asset_model": "Acer",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Asus",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Dell",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Asus",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    },
                        {
                        "asset_model": "Dell",
                        "list_product": [{
                            "product_name": "Acer Aspire",
                                            "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                            "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                            "price": "1500$",
                                            "image_uri": "Desktop/ /"
                        }]
                    }
                    ]},
                {"category_id": "004",
                 "category_name": "Other",
                 "asset": [{
                     "asset_model": "Acer",
                     "list_product": [{
                         "product_name": "Acer Aspire",
                         "short_desc": "(i5 7200U / 4GB / 1TB / 15.6Inch )",
                         "long_desc": "CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                         "price": "1500$",
                         "image_uri": "Desktop/ /"
                     }]
                 }]
                 }]
        }

class Products(Resource):
    print(dir_path)
    def get(self):
        list_product_data = []
        list_asset_data = []
        data = []
        categories = mongo.db.category
        assets = mongo.db.asset
        products = mongo.db.product
        list_product = []
        for category in categories.find():
            for asset in assets.find():
                for product in products.find({'asset_id': asset['_id']}):
                    product_data = {
                        'product_id': str(product['_id']),
                        "product_name": product['product_name'],
                        "short_desc": product['short_desc'],
                        "long_desc": product['long_desc'],
                        "price": product['price'],
                        "image_uri": (dir_path + "/" + product['image_uri'])
                    }
                    list_product_data.append(product_data)

                asset_data = {
                    'asset_id': str(asset['_id']),
                    'asset_model': str(asset['asset_model']),
                    'list_product': list_product_data
                }
                list_asset_data.append(asset_data)
            
            category_data = {
                'category_id': str(category['_id']),
                'category_name': str(category['category_name']),
                'asset':list_asset_data
                }
            data.append(category_data)
                    
        return jsonify({'categories': data}) 


    def post(self):
        data = dict(request.form)
        print(data)
        category_name = data['category_name'][0]
        print(category_name)
        asset_model = data['asset_model'][0]
        product_name = data['product_name'][0]
        short_desc = data['short_desc'][0]
        long_desc = data['long_desc'][0]
        price = data['price'][0]
        files = request.files['image_uri']

        extension = os.path.splitext(files.filename)[1]
        f_name = str(uuid4()) + extension
        print(f_name)
        path = 'images/'
        UPLOAD_FOLDER = path

        categories = mongo.db.category
        assets = mongo.db.asset
        products = mongo.db.product

        if not categories.find_one({'category_name': category_name}):
            category_id = categories.insert({"category_name": category_name})
            if not assets.find_one({'asset_model': asset_model}):
                asset_id = assets.insert({"asset_model": asset_model})
                product = products.find_one({'product_name': product_name})
                product = products.find_one({'product_name': product_name})
                if products.find_one({'product_name': product_name}):
                    if (product['category_id'] == category_id) and (product['asset_id'] == asset_id):
                        return {'message': 'this product_name is existed in this category and asset', 'code': '404'}
                    elif (product['category_id'] == category_id) and not (product['asset_id'] == asset_id):
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                        return {'message': 'new product add successfully to existed category new asset', 'code': '200'}
                    elif not (product['category_id'] == category_id) and (product['asset_id'] == asset_id):
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                        return {'message': 'new product add successfully to new category existed asset', 'code': '200'}
                else:
                    image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                    files.save(image_uri)
                    product_id = products.insert({
                        'category_id': category_id,
                        'asset_id': asset_id,
                        'product_name': product_name,
                        'short_desc': short_desc,
                        'long_desc': long_desc,
                        'price': price,
                        'image_uri': image_uri
                    })
                    return {'message': 'new product add successfully to existed category and existed asset', 'code': '200'}
            elif assets.find_one({'asset_model': asset_model}):
                asset = assets.find_one({'asset_model': asset_model})
                asset_id = asset['_id']
                product = products.find_one({'product_name': product_name})
                product = products.find_one({'product_name': product_name})
                if products.find_one({'product_name': product_name}):
                    if (product['category_id'] == category_id) and (product['asset_id'] == asset_id):
                        return {'message': 'this product_name is existed in this category and asset', 'code': '404'}
                    elif (product['category_id'] == category_id) and not (product['asset_id'] == asset_id):
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                        return {'message': 'new product add successfully to existed category new asset', 'code': '200'}
                    elif not (product['category_id'] == category_id) and (product['asset_id'] == asset_id):
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                        return {'message': 'new product add successfully to new category existed asset', 'code': '200'}
                else:
                    image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                    files.save(image_uri)
                    product_id = products.insert({
                        'category_id': category_id,
                        'asset_id': asset_id,
                        'product_name': product_name,
                        'short_desc': short_desc,
                        'long_desc': long_desc,
                        'price': price,
                        'image_uri': image_uri
                    })
                    return {'message': 'new product add successfully to existed category and existed asset', 'code': '200'}

        if categories.find_one({'category_name': category_name}):
            category = categories.find_one({'category_name': category_name})
            category_id = category['_id']
            # existed category, new asset
            if not assets.find_one({'asset_model': asset_model}):
                asset_id = assets.insert({"asset_model": asset_model})
                product = products.find_one({'product_name': product_name})
                print("1111111111")
                if products.find_one({'product_name': product_name}):
                    if (product['category_id'] == category_id) and (product['asset_id'] == asset_id):
                        return {'message': 'this product_name is existed in this category and asset', 'code': '404'}
                    elif (product['category_id'] == category_id) and not (product['asset_id'] == asset_id):
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                        return {'message': 'new product add successfully to existed category new asset', 'code': '200'}
                    elif not (product['category_id'] == category_id) and (product['asset_id'] == asset_id):
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                        return {'message': 'new product add successfully to new category existed asset', 'code': '200'}
                else:
                    image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                    files.save(image_uri)
                    product_id = products.insert({
                        'category_id': category_id,
                        'asset_id': asset_id,
                        'product_name': product_name,
                        'short_desc': short_desc,
                        'long_desc': long_desc,
                        'price': price,
                        'image_uri': image_uri
                    })
                    return {'message': 'new product add successfully to existed category and existed asset', 'code': '200'}
            #existed category, existed asset
            elif assets.find_one({'asset_model': asset_model}):
                print("222221312312")
                asset = assets.find_one({'asset_model': asset_model})
                asset_id = asset['_id']
                product = products.find_one({'product_name': product_name})
                if products.find_one({'product_name': product_name}):
                    print("*****************")
                    if (product['category_id'] == category_id) and (product['asset_id'] == asset_id):
                        return {'message': 'this product_name is existed in this category and asset', 'code': '404'}
                    elif (product['category_id'] == category_id) and not (product['asset_id'] == asset_id):
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                        return {'message': 'new product add successfully to existed category new asset', 'code': '200'}
                    elif not (product['category_id'] == category_id) and (product['asset_id'] == asset_id):
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                        return {'message': 'new product add successfully to new category existed asset', 'code': '200'}
                    else:
                        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                        files.save(image_uri)
                        product_id = products.insert({
                                'category_id': category_id,
                                'asset_id': asset_id,
                                'product_name': product_name,
                                'short_desc': short_desc,
                                'long_desc': long_desc,
                                'price': price,
                                'image_uri': image_uri
                                })
                        return {'message': 'new product add successfully to existed category and existed asset', 'code': '200'}
                else:
                    print("****************-------------*")
                    image_uri = os.path.join(UPLOAD_FOLDER, f_name)
                    files.save(image_uri)
                    product_id = products.insert({
                            'category_id': category_id,
                            'asset_id': asset_id,
                            'product_name': product_name,
                            'short_desc': short_desc,
                            'long_desc': long_desc,
                            'price': price,
                            'image_uri': image_uri
                        })
                    return {'message': 'new product add successfully to existed category and existed asset', 'code': '200'}
                
class MockBlog(Resource):
    def get(self):
        return {
            "Blogs": [
                {
                    "blog_title": "Gold One's 10th Anniversary Promotion",
                    "posted_date": "03/12/2017",
                    "Author": "Chung Uong",
                    "short_desc": "In this special occasion, we are pleased to introduce a series of sale promotion, including a chance to win an iPhone X and a MSI GV62 7RC.",
                    "image_uri": "desktop"
                },
                {
                    "blog_title": "Gold One's 10th Anniversary Promotion",
                    "posted_date": "03/12/2017",
                    "Author": "Chung Uong",
                    "short_desc": "In this special occasion, we are pleased to introduce a series of sale promotion, including a chance to win an iPhone X and a MSI GV62 7RC.",
                    "image_uri": "desktop"
                },
                {
                    "blog_title": "Gold One's 10th Anniversary Promotion",
                    "posted_date": "03/12/2017",
                    "Author": "Chung Uong",
                    "short_desc": "In this special occasion, we are pleased to introduce a series of sale promotion, including a chance to win an iPhone X and a MSI GV62 7RC.",
                    "image_uri": "desktop"
                }, {
                    "blog_title": "Gold One's 10th Anniversary Promotion",
                    "posted_date": "03/12/2017",
                    "Author": "Chung Uong",
                    "short_desc": "In this special occasion, we are pleased to introduce a series of sale promotion, including a chance to win an iPhone X and a MSI GV62 7RC.",
                    "image_uri": "desktop"
                }, {
                    "blog_title": "Gold One's 10th Anniversary Promotion",
                    "posted_date": "03/12/2017",
                    "Author": "Chung Uong",
                    "short_desc": "In this special occasion, we are pleased to introduce a series of sale promotion, including a chance to win an iPhone X and a MSI GV62 7RC.",
                    "image_uri": "desktop"
                }
            ]
        }

class UserRegister(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']
        # print(pas)
        user = mongo.db.users
        pw_hash = bcrypt.generate_password_hash(password)
        print(pw_hash)
        for u in user.find():
          if u['username'] == username:
            return {'message': 'this user name is existed', 'code': '404'}
        user_id = user.insert({'username': username, 'password': pw_hash})
        new_user = user.find_one({'_id': user_id})
        print(pw_hash)
        return {'message': 'Register Success', 'code': '200'}, 200


class USerSignIn(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']
        user = mongo.db.users
        pw_hash = bcrypt.generate_password_hash(password)
        u = user.find_one({'username': username})
        print(u)
        if user.find_one({'username': username}):
            print(password)
            print(u['password'])
            print(u['username'])
            if bcrypt.check_password_hash(u['password'], str(password)):
                return {'message': 'Log In successfully', 'code': '200'}, 200
            else:
                return {'message': 'wrong password', 'code': '404'}
        return {'message': 'please check your username again', 'code': '404'}


class News(Resource):
    def get(self):
        list_blog_data = []
        blogs = mongo.db.blog
        if blogs.find():
            for blog in blogs.find():
                blog_data = {
                    "blog_id": str(blog['_id']),
                    "news_title": blog['news_title'],
                    "posted_date": blog['posted_date'],
                    "author": blog['author'],
                    "short_desc": blog['short_desc'],
                    "long_desc": blog['long_desc'],
                    "image_uri": (dir_path + '/' + blog['image_uri'])
                }
                list_blog_data.append(blog_data)
            return {"Blogs": list_blog_data}
    def post(self):
        mylist = []
        today = datetime.date.today()
        mylist.append(today)
        blog_data = dict(request.form)
        print(blog_data)
        news_title = blog_data['news_title'][0]
        author = blog_data['author'][0]
        short_desc = blog_data['short_desc'][0]
        long_desc = blog_data['long_desc'][0]
        files = request.files['image_uri']

        extension = os.path.splitext(files.filename)[1]
        f_name = str(uuid4()) + extension
        print(f_name)
        path = 'images/'
        UPLOAD_FOLDER = path


        blogs = mongo.db.blog
        if blogs.find_one({'news_title': news_title, 'author': author, 'short_desc': short_desc}):
            return {'message': 'this blogs news already have in database', 'code': '404'}, 404
        image_uri = os.path.join(UPLOAD_FOLDER, f_name)
        files.save(image_uri)
        blog_id = blogs.insert({
            "news_title": news_title,
            "posted_date": str(mylist[0]),
            "author": author,
            "short_desc": short_desc,
            "long_desc": long_desc,
            "image_uri": image_uri
        })
        return {'message': 'add blogs news success fully', 'code': '200'},201

if __name__ == '__main__':
    #product
    api.add_resource(News, '/news')
    api.add_resource(Products, '/products')
    api.add_resource(UserRegister, '/register')
    api.add_resource(USerSignIn, '/signin')
    api.add_resource(MockProduct, '/MockProduct')
    api.add_resource(MockBlog, '/MockBlog')
    app.run(port=5000, debug=True)
