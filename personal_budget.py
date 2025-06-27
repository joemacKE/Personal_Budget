class InvalidBudgetData(Exception):
    def __init__(self, monthly_income, expenses, months):
        message = f"Invalid budget data: Income = {monthly_income}, Expenses = {expenses}, Months = {months}. "
        if monthly_income < 0:
            message += "Salary cannot be negative. "
        if expenses > monthly_income:
            message += "Expenses cannot exceed income. "
        if months <= 0:
            message += "Months must be greater than zero. "
        super().__init__(message)


class Person:
    def __init__(self):
        self.details = {}
        self.financial_data = ()
        self.earnings = 0
        self.expenses = []
        self.expense_names = set()
        self.net_savings = 0

    def collect_details(self):
        try:
            self.details['name'] = input("Enter your name: ")
            self.details['age'] = int(input("Enter your age: "))
            self.details['occupation'] = input("Enter your occupation: ")
        except Exception as e:
            print(f"Error collecting details: {e}")

    def collect_financial_data(self):
        try:
            monthly_income = float(input("Enter your monthly income: "))
            months = int(input("Enter number of months worked: "))

            if monthly_income < 0 or months <= 0:
                raise InvalidBudgetData(monthly_income, 0, months)

            self.financial_data = (monthly_income, months)
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            self.collect_financial_data()
        except InvalidBudgetData as e:
            print(e)
            self.collect_financial_data()
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            self.collect_financial_data()

    def calculate_earnings(self):
        income, months = self.financial_data
        self.earnings = income * months

    def collect_expenses(self):
        try:
            self.expenses.clear()
            self.expense_names.clear()

            for i in range(4):
                name = input(f"Enter expense #{i + 1} name: ")
                amount = float(input(f"Enter amount for {name}: "))
                self.expenses.append({"name": name, "amount": amount})
                self.expense_names.add(name)
        except ValueError:
            print("Please enter valid numbers for expense amounts.")
            self.collect_expenses()
        except Exception as e:
            print(f"Error collecting expenses: {e}")
            self.collect_expenses()

    def deduct_expenses(self):
        try:
            total_expenses = sum(exp['amount'] for exp in self.expenses)
            self.net_savings = self.earnings - total_expenses
        except Exception as e:
            print(f"Error deducting expenses: {e}")

    def classify_saver_and_spender(self):
        try:
            total_expenses = sum(exp['amount'] for exp in self.expenses)
            if total_expenses < 0.5 * self.earnings:
                print("Category: Saver")
            elif total_expenses > 0.7 * self.earnings:
                print("Category: Spender")
            else:
                print("Category: Balanced")
        except Exception as e:
            print(f"Error classifying saver/spender: {e}")

    def print_summary(self):
        print("\n--- Summary ---")
        print(f"Name: {self.details.get('name')}")
        print(f"Age: {self.details.get('age')}")
        print(f"Occupation: {self.details.get('occupation')}")
        print(f"Earnings: {self.earnings}")
        print(f"Expenses: {[(e['name'], e['amount']) for e in self.expenses]}")
        print(f"Net Savings: {self.net_savings}")
    def to_dict(self):
        return {
            "details": self.details,
            "financial_data": self.collect_financial_data,
            "earnings": self.earnings,
            "expenses": self.expenses,
            "net_savings": self.net_savings,
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls()
        obj.details = data["details"]
        obj.financial_data = tuple(data["financial_data"])
        obj.earnings = data["earnings"]
        obj.expenses = data["expenses"]
        obj.expense_names = set(exp["name"] for exp in obj.expenses)
        obj.net_savings = data["net_savings"]
        return obj
import json
def save_to_file(persons, filename="budget_data.json"):
    try:
        with open(filename, "w") as file:
            json.dump([person.to_dict() for person in persons], file, indent=2)
        print(f"\n Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_from_dict(filename="budget_data.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [Person.from_dict(item) for item in data]
    except FileNotFoundError:
        print("Error! Data not found")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []





def main():
    people = []
    add_more = "yes"

    while add_more.lower() == "yes":
        individual = Person()
        individual.collect_details()
        individual.collect_financial_data()
        individual.calculate_earnings()
        individual.collect_expenses()
        individual.deduct_expenses()
        individual.classify_saver_and_spender()
        individual.print_summary()
        people.append(individual)
        add_more = input("Do you wish to add another person (yes/no): ")
    
    save_to_file(people)
    print("\nAll data saved successfully.")

if __name__ == "__main__":
    main()

        
