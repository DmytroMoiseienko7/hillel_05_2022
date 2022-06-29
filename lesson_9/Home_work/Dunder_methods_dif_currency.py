from currency_functions import DATA_EXCHANGE_LOGIC, DATA_READER


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __str__(self) -> str:
        return f"result is {self.amount} in {self.currency} "

    def __add__(self, other):
        instance = Price((self.amount + other.amount), self.currency)
        return instance

    def __sub__(self, other):
        instance = Price((self.amount - other.amount), self.currency)
        return instance

    def __mul__(self, other):
        instance = Price((self.amount * other), "UAH")
        return instance

    def __round__(self, number=2):
        return round(self.amount, 2)


def main():
    data_reader = DATA_READER
    data_exchange = DATA_EXCHANGE_LOGIC

    option_1 = input("Where would you like to search laptop UA/PL/US/DE/GB ==>  ")
    option_2 = input("What kind of laptop would you like select DELL/ASUS/HP/==> ")

    laptop_details_1 = data_reader.search_price_of_laptop(option_1, option_2)

    print(f"{option_2} price is {laptop_details_1[0]} {laptop_details_1[1]}")

    price_1 = Price(laptop_details_1[0], laptop_details_1[1])

    laptop_1 = round(
        data_exchange.make_currency_conversion(
            option_1, price_1, laptop_details_1, data_reader.search_exchange_rate
        )
    )

    price_1 = Price(laptop_1, "UAH")

    print("Conversion", price_1)

    option_3 = input("Where would you like to search laptop UA/PL/US/DE/GB ==> ")
    option_4 = input("What kind of laptop would you like select DELL/ASUS/HP/==>  ")

    laptop_details_2 = data_reader.search_price_of_laptop(option_3, option_4)

    print(f"{option_4} price is {laptop_details_2[0]} {laptop_details_2[1]}")

    price_2 = Price(laptop_details_1[0], laptop_details_1[1])

    laptop_2 = round(
        data_exchange.make_currency_conversion(
            option_3, price_2, laptop_details_2, data_reader.search_exchange_rate
        )
    )

    price_2 = Price(laptop_2, "UAH")

    print("Conversion", price_2)

    option_5 = input(
        "If you want to see a sum of selected laptops- type SUM/if you want to see difference in prices- type DIF ==>  "
    )
    total_price = data_exchange.calculate_dif_or_sum(option_5, price_1, price_2)

    print("Total", total_price)


if __name__ == "__main__":
    main()
