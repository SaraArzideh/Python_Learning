class IConverter():
    def convert(amount,currency):
        pass

class DollarConverter(IConverter):
    def convert(self, amount, currency):
        if currency == "euro":
            return amount * 1.07
        if currency == "yen":
            return amount * 0.0068
        return amount

class EuroConverter(IConverter):
    def convert(self, amount, currency):
        if currency == "dollar":
            return amount * 0.93
        if currency == "yen":
            return amount * 0.0064
        return amount
    
class YenConverter(IConverter):
    def convert(self, amount, currency):
        if currency == "euro":
            return amount * 157.39
        if currency == "dollar":
            return amount * 146.78
        return amount

def Factory(currency= "dollar"):
    currencyconverters={
        "dollar": DollarConverter,
        "euro": EuroConverter,
        "yen": YenConverter,      
    }
    return currencyconverters[currency]()

def main():
    """
    converters= []
    converters.append(Factory("dollar"))
    converters.append(Factory("euro"))
    converters.append(Factory("yen"))
    """
    currencies=["dollar", "euro", "yen"]
    for currency in currencies:
        converters=Factory(currency)

        if currency == "dollar":
            print ("One dollar is equal to " + str(converters.convert(1, "dollar")) + " dollar(s)")
            print ("One euro is equal to " + str(converters.convert(1, "euro")) + " dollar(s)")
            print ("One yen is equal to " + str(converters.convert(1, "yen")) + " dollar(s)")
        elif currency == "euro":
            print ("One dollar is equal to " + str(converters.convert(1, "dollar")) + " euro(s)")
            print ("One euro is equal to " + str(converters.convert(1, "euro")) + " euro(s)")
            print ("One yen is equal to " + str(converters.convert(1, "yen")) + " euro(s)")
        elif currency == "yen":
            print ("One dollar is equal to " + str(converters.convert(1, "dollar")) + " yen(s)")
            print ("One euro is equal to " + str(converters.convert(1, "euro")) + " yen(s)")
            print ("One yen is equal to " + str(converters.convert(1, "yen")) + " yen(s)")

if __name__ == "__main__":
    main()