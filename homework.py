import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.date_format = '%d.%m.%Y'
        self.date_now = dt.datetime.now().date()
        self.last_week = (self.date_now - dt.timedelta(days=7))

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        for record in self.records:
            date = dt.datetime.strptime(record.date, self.date_format).date()
            if date == self.date_now:
                today_stats += record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        for record in self.records:
            date = dt.datetime.strptime(record.date, self.date_format).date()
            if self.last_week <= date <= self.date_now:
                week_stats += record.amount
        return week_stats


class CashCalculator(Calculator):
    def get_today_cash_remained(self,currency):
        USD_RATE = 80
        EURO_RATE = 100
        currency_dict = {
            'usd': ['USD', USD_RATE],
            'eur': ['Euro', EURO_RATE],
            'rub': ['руб', 1]
        }
        today_stats = super().get_today_stats()
        today_currency_stats = today_stats / currency_dict[currency][1]
        today_remainder = abs(today_stats-self.limit) / currency_dict[currency][1]

        if today_stats < self.limit:
            return f'На сегодня осталось {today_currency_stats} {currency_dict[currency][0]}'
        elif today_stats == self.limit:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {today_remainder} {currency_dict[currency][0]}'

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stats = super().get_today_stats()
        last_calorie = self.limit - today_stats
        return f'«Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более' \
               f' {last_calorie} кКал»' if today_stats < self.limit else 'Хватит есть!'

class Record:
    def __init__(self, amount, comment, date=str(dt.datetime.now().date())):
        self.amount = amount
        self.date = date
        self.comment = comment


# для CashCalculator
r1 = Record(amount=1450, comment="Безудержный шопинг", date="08.12.2020")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="07.12.2020")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")
# r33 =Record(amount=691, comment="Катание на такси")
# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
print(cash_calculator.get_today_cash_remained('rub'))


# calories_calculator = CaloriesCalculator(1000)
# calories_calculator.add_record(r1)
# calories_calculator.add_record(r2)
# print(calories_calculator.get_calories_remained())
# cash_calculator.add_record(Record(amount=145, comment="кофе"))
# # и к этой записи тоже дата должна добавиться автоматически
# cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# # а тут пользователь указал дату, сохраняем её
# cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
#
# print(cash_calculator.get_today_cash_remained("rub"))

# calc.add_record(r33)
