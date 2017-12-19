from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_pymongo import PyMongo
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'API'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/API'
app.secret_key = 'proseth123'
api = Api(app)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

class Product(Resource):
   
    # @jwt_required()
    def get(self):
        
        return {
                    "categories":[
                                    {
                                    "category_id":"001",
                                    "category_name":"Desktop",
                                    "asset":[{
                                                "asset_model":"Acer",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Asus",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Dell",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Asus",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Dell",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                }
                                ]},
                                {
                                    "category_id":"002",
                                    "category_name":"Laptop",
                                    "asset":[{
                                                "asset_model":"Asus",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Asus",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Dell",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                }
                                ]},
                                {
                                    "category_id":"003",
                                    "category_name":"Accessory",
                                    "asset":[{
                                                "asset_model":"Acer",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Asus",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Dell",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Asus",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                },
                                                {
                                                "asset_model":"Dell",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                }
                                ]},
                                    {"category_id":"004",
                                        "category_name":"Other",
                                        "asset":[{
                                                "asset_model":"Acer",
                                                "list_product":[{
                                                                "product_name":"Acer Aspire",
                                                                "short_desc":"(i5 7200U / 4GB / 1TB / 15.6Inch )",
                                                                "long_desc":"CPU: Intel Dual-Core i5 7200U Processor, ( 2.5GHz Max 3.1GHz ) RAM: 4GB DDR4 Storage: 1TB HDD Optical Drive: N/A Display: 15.6 Inch HD 16:9 (1366 x 768) Graphic: Intel HD Graphics 620 Wifi: 802.11ac Bluetooth: 4.0 Camera: HD Web Camera Interface: 1x USB 3.0 2x USB 2.0 Network (RJ-45) HDMI Output Battery: 2-cell 4810 mAh Li-Polymer Weight:2.0kg OS: DOS",
                                                                "price":"1500$",
                                                                "image_uri":"Desktop/ /"
                                                                }]
                                                }]
                                    }]
                }
    
    # def post(self, name):
    #     if next(filter(lambda x: x['name'] == name, items), None) is not None:
    #         return {'message': "An item with name '{}' already exists".format(name)}, 400
    #     data = Item.parser.parse_args()
    #     item = {'name': data['name'], 'price': data['price']}
    #     items.append(item)
    #     return item, 201

    # def delete(self, name):
    #     global items
    #     items = list(filter(lambda x: x['name'] != name, items))
    #     return {'message': 'item deleted'}
    
    # def put(self, name):
    #     data = Item.parser.parse_args()
    #     item = next(filter(lambda x: x['name'] == name, items), None)
    #     if item is None:
    #         item = {
    #             'name': name,
    #             'price': data['price']
    #         }
    #         items.append(item)
    #     else:
    #         item.update(data)
    #     return item

class Blog(Resource):
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
        }
        ,{
        "blog_title": "Gold One's 10th Anniversary Promotion",
        "posted_date": "03/12/2017",
        "Author": "Chung Uong",
        "short_desc": "In this special occasion, we are pleased to introduce a series of sale promotion, including a chance to win an iPhone X and a MSI GV62 7RC.",
        "image_uri": "desktop"
        }
        ,{
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
        return {'message': 'Register Success','code': '200'}, 200


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
        return {'message': 'please check your username again','code': '404'}

if __name__ == '__main__':
    api.add_resource(UserRegister, '/register')
    api.add_resource(USerSignIn, '/signin')
    api.add_resource(Product, '/Product')
    api.add_resource(Blog, '/Blog')
    app.run(port = 5000, debug=True)
