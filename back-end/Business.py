# Standard import
from datetime import datetime as dt
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

    def put(self, obj):
        return self.collection.put(obj)

    def delete(self, _id):
        return self.collection.delete(_id)


class ClientBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ClientCollection)
        
    def email_already_registered(self, email):
        return self.collection.get_by_email(email) != None


class CompanyBusiness(BusinessBase):
    def __init__(self):
        super().__init__(CompanyCollection)

    def email_already_registered(self, email):
        return self.collection.get_by_email(email) != None


class ProductBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ProductCollection)

    def __price_history_n_days_ago(self, price_history, d = 14):
        two_weeks = dt.now() - dt.timedelta(days = d)
        return [i for i in price_history if two_weeks <= i[0] <= dt.now()]

    def update_price(self, _id, new_price):
        product = self.collection.get(_id)
        
        # Get new prices of the last two weeks ago
        prices = self.__price_history_n_days_ago(product.price_history, 14)

        product.price_history.append((dt.now(), new_price))
        
        if len(prices) > 5:
            n_prices = len(prices)
            Counter([i[1] for i in prices[n_prices-5:n_prices]])
        
        return self.collection.update_price(_id, new_price)
    
class ReviewBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ReviewCollection)
