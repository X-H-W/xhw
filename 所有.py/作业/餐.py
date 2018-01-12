class Restaurant(object):
    def __ini__(self):
        self.restaurant_name = '刀削面'
        self.cuisine_type = '中餐'
    def descibe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine)
    def open_restaurant(self):
        print('正在营业')

restaurant = Restaurant()
print(restaurant.restaurant_name,restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restanurant()
