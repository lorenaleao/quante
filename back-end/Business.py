# Standard import
from datetime import datetime as dt
from datetime import timedelta
from collections import Counter

# Local application import
from Collections import *
from Objects import IObject, Client, Review, Product

class BusinessBase():
    def __init__(self, collection):
        self.collection = collection()
    
    def post(self, obj):
        return self.collection.post(obj)

    def get(self, _id):
        return self.collection.get(_id)

    def get_by_name(self, name: str):
        return self.collection.get_by_name(name)

    def get_by_substring(self, name: str):
        return self.collection.get_by_substring(name)

    def get_list(self):
        return self.collection.get_list()

    def put(self, obj):
        return self.collection.put(obj)

    def delete(self, _id):
        return self.collection.delete(_id)


class ClientBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ClientCollection)
        
    def email_already_registered(self, email):
        return self.collection.get_by_email(email) != None

    def get_by_email_password(self, email, password):
        client = self.collection.get_by_email(email)
        if client is None or client.password != password:
            return None
        else:
            return client
        
        
class CompanyBusiness(BusinessBase):
    def __init__(self):
        super().__init__(CompanyCollection)

    def email_already_registered(self, email):
        return self.collection.get_by_email(email) != None

    def get_by_email_password(self, email, password):
        company = self.collection.get_by_email(email)
        if company is None or company.password != password:
            return None
        else:
            return company

class ProductBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ProductCollection)

    def __to_datetime(self, x):
        if isinstance(x, dt):
            return x
        else:
            return dt.strptime(x, "%Y-%m-%d %H:%M:%S.%f")
    
    def __prices_n_days_ago(self, prices, d = 14):
        return [i[1] for i in prices if (dt.now() - timedelta(days = d)) <= self.__to_datetime(i[0]) <= dt.now()]

    def update_price(self, id_company, id_product, new_price):
        product = self.collection.get(id_product)
        product.price_history.append((dt.now(), new_price)) # Add in history
        if id_company in product.prices:
            product.prices[id_company][1].append((dt.now(), new_price))
            recent_prices = self.__prices_n_days_ago(product.prices[id_company][1], 14)# Get new prices of the last two weeks ago
            n_prices = len(recent_prices)
            if n_prices > 5:
                c = Counter([i for i in recent_prices[n_prices-5:n_prices]])
                product.prices[id_company][0] = c.most_common(1)[0][0]
        else:
            product.prices[id_company] = (new_price, [(dt.now(), new_price)])
        return self.collection.put(product)

    
class ReviewBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ReviewCollection)

    def post(self, obj):
        productBusiness = ProductBusiness()
        product = productBusiness.get(obj["product_id"])
        obj = Review.convert(obj).__dict__

        if len(product["relevant_reviews"]) < 10:
            product["relevant_reviews"].append(obj)

        productBusiness.put(product)
        return super().post(obj)

    def put(self, obj):
        productBusiness = ProductBusiness()
        product = productBusiness.get(obj["product_id"])
        obj = Review.convert(obj).__dict__

        i = 0;
        index = -1
        for review in product["relevant_reviews"]:
            if review["_id"] == obj["_id"]:
                index = i
            i += 1
        
        product["relevant_reviews"][index] = obj
        productBusiness.put(product)
        return super().put(obj)
