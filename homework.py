import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.date_now = dt.date.today()

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = sum(record.amount for record in self.records
                          if record.date == self.date_now)
        return today_stats

    def get_week_stats(self):
        last_week = (self.date_now - dt.timedelta(days=7))
        week_stats = 0
        for record in self.records:
            if last_week < record.date <= self.date_now:
                week_stats += record.amount
        return week_stats


class CashCalculator(Calculator):
    USD_RATE = float(60)
    EURO_RATE = float(70)

    def get_today_cash_remained(self, currency):
        currency_dict = {
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE),
            'rub': ('руб', 1)
        }
        today_stats = self.get_today_stats()
        today_remainder = round(abs(self.limit - today_stats)
                                / currency_dict[currency][1], 2)

        if today_stats < self.limit:
            return (f'На сегодня осталось {today_remainder} '
                    f'{currency_dict[currency][0]}')
        elif today_stats == self.limit:
            return 'Денег нет, держись'
        return (f'Денег нет, держись: твой долг - '
                f'{today_remainder} {currency_dict[currency][0]}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stats = self.get_today_stats()
        last_calorie = self.limit - today_stats
        phrase = ('Сегодня можно съесть что-нибудь ещё,'
                  ' но с общей калорийностью не более')
        return (f'{phrase} {last_calorie} кКал'
                if today_stats < self.limit else 'Хватит есть!')


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.date = (dt.date.today() if date is None
                     else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment
