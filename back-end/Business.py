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

    def __prices_n_days_ago(self, prices, d = 14):
        return [i[1] for i in prices if dt.now() - timedelta(days = d) <= i[0] <= dt.now()]

    def update_price(self, id_company, id_product, new_price):
        product = self.collection.get(id_product)
        
        # Add in history
        product.price_history.append((dt.now(), new_price))
        
        if id_company in product.prices:
            product.prices[id_company][1].append((dt.now(), new_price))
            
            # Get new prices of the last two weeks ago
            recent_prices = self.__prices_n_days_ago(product.prices[id_company][1], 14)

            # Change the product price, if satisfy the rule
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
