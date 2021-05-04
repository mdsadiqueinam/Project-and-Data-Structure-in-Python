class Category:
    
    def __init__(self, name) :
        self.name = name
        self.ledger = list()
        self.available_balance = 0.00
        self.spend = 0

    def check_funds(self, amount) :
        if amount>self.available_balance : return False
        return True

    def deposit(self, amount, description="") :
        self.ledger.append({"amount": amount, "description": description})
        self.available_balance+=amount
    
    def withdraw(self, amount, description="") :
        if self.check_funds(amount) :
            self.ledger.append({"amount": amount*-1, "description": description})
            self.available_balance-=amount
            self.spend+=amount
            return True
        return False
    
    def get_balance(self) :
        return self.available_balance
    
    def transfer(self, amount, category) :
        if self.check_funds(amount) :
            self.withdraw(amount, "Transfer to {}".format(category.name))
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        return False
    
    def __str__(self) :
        strlist = list()
        strlist.append(self.name.center(30, '*'))
        for object in self.ledger :
            strlist.append(object["description"].ljust(23, ' ')[:23] + "{0:.2f}".format(object["amount"]).rjust(7, ' '))
        strlist.append("Total: {}".format(str(self.available_balance)))
        return ("\n".join(strlist))
def get_percent(total_spend, spend) :
    spend = int((spend/total_spend)*100)
    if spend%10>5 :
        return ((spend-(spend%10))+10)
    return (spend-(spend%10))

def create_spend_chart(categories):
    total_spend = 0
    largest_str_len = 0
    percent_list = []
    chart = 'Percentage spent by category\n'
    for value in categories :
        total_spend += value.spend
        largest_str_len = max(largest_str_len, len(value.name))

    for i in range(len(categories)) :
        percent_list.append(get_percent(total_spend, categories[i].spend))
        categories[i].name = categories[i].name.ljust(largest_str_len, ' ')

    for x in range(100, -1, -10) :
        y = str(x).rjust(3,' ')+'|'
        for i in range(len(percent_list)) :
            if x>percent_list[i] : y = y + '   '
            else : y = y + ' o '
        chart = chart + y + ' \n'
        
    chart = chart + ('-'*((len(categories)*3)+1)).rjust(14,' ') + '\n'

    for i in range(largest_str_len) :
        y = "    "
        for v in categories :
            y = y + v.name[i].center(3,' ')
        chart = chart + y + ' \n'
    
    chart = chart[:len(chart)-1]
    return chart