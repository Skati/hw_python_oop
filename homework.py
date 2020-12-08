import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.date_now = dt.datetime.now().date()
        self.last_week = (self.date_now - dt.timedelta(days=7))

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        for record in self.records:
            if record.date == self.date_now:
                today_stats += record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        for record in self.records:
            if self.last_week <= record.date <= self.date_now:
                week_stats += record.amount
        return week_stats


class CashCalculator(Calculator):
    USD_RATE = float(60)
    EURO_RATE = float(70)
    def get_today_cash_remained(self,currency):
        currency_dict = {
            'usd': ['USD', CashCalculator.USD_RATE],
            'eur': ['Euro', CashCalculator.EURO_RATE],
            'rub': ['руб', 1]
        }
        today_stats = super().get_today_stats()
        today_currency_stats = round(today_stats / currency_dict[currency][1],2)
        today_remainder = round(abs(today_stats-self.limit) / currency_dict[currency][1],2)

        if today_stats < self.limit:
            return f'На сегодня осталось {today_remainder} {currency_dict[currency][0]}'
        elif today_stats == self.limit:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {today_remainder} {currency_dict[currency][0]}'

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stats = super().get_today_stats()
        last_calorie = self.limit - today_stats
        return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более' \
               f' {last_calorie} кКал' if today_stats < self.limit else 'Хватит есть!'

class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment


# для CashCalculator
r1 = Record(amount=145, comment="Безудержный шопинг", date="08.12.2020")
r2 = Record(amount=156, comment="Наполнение потребительской корзины", date="08.12.2020")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")
r33 =Record(amount=691, comment="Катание на такси")
# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
print(cash_calculator.get_today_cash_remained('rub'))



