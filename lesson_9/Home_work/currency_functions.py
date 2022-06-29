import json


class DATA_READER:

    file_exchange = "lesson_9/Home_work/exchange_rate.json"
    file_laptops = "lesson_9/Home_work/laptop_pricies.json"

    def read_json_file(file_json_name):
        with open(file_json_name, "r") as file:
            data = json.load(file)
        return data

    def search_price_of_laptop(my_market, my_laptop, data=read_json_file(file_laptops)):
        result = []
        for dicts in data:
            if dicts["market"] == my_market:
                for second_level_dicts in dicts["make_price"]:
                    if second_level_dicts["name"] == my_laptop:
                        result.append(second_level_dicts["price"])
                        result.append(dicts["currency"])
        return result

    def search_exchange_rate(currency="USD", data=read_json_file(file_exchange)):
        for dicts in data:
            if dicts["from"] == currency:
                exchange_rate = dicts["value"]
        return exchange_rate


class DATA_EXCHANGE_LOGIC(DATA_READER):
    def make_currency_conversion(option, price, laptop_details, exchange_reader):
        if option == "UA":
            laptop = price
        elif option == "US":
            exchange_rate = exchange_reader()
            laptop = price * exchange_rate
        else:
            exchange_rate = exchange_reader(laptop_details[1])
            exchange_rate_2 = exchange_reader()
            laptop = price * exchange_rate * exchange_rate_2
        return laptop

    def calculate_dif_or_sum(option, price_1, price_2):
        if option == "SUM":
            result = price_1 + price_2
        else:
            result = price_1 - price_2
        return result
