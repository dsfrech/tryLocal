""" Exercise 9-6 using Restaurant from 9-1"""

class Restaurant:
    """Restaurant Class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize values for a restaurant"""
        self.r_name = restaurant_name
        self.r_cuisine = cuisine_type

    def describe_restuarant(self):
        """Print out the values for a restaurent"""
        print("Restaurant name:", self.r_name)
        print("Cuisine Type:   ", self.r_cuisine)

class IceCreamStand(Restaurant):
    """Ice Cream Stand"""

    def __init__(self, restaurant_name):
        """Set up the ICS"""
        super().__init__( restaurant_name, "Ice Cream Shop")
        self.flavors = []

    def icecreamflavors(self, flavors):
        """Set flavors from list"""
        self.flavors = flavors

    def describe_restuarant(self):
        """describe the icecreamshop"""
        super().describe_restuarant()
        print("Flavors:        ", self.flavors)

handynasty = Restaurant("Han Dynasty", "Sichuan")
handynasty.describe_restuarant()

turkeyhill = IceCreamStand("Turkey Hill")
turkeyhill.icecreamflavors(["vanilla", "chocolate", "strawberry"])
turkeyhill.describe_restuarant()
