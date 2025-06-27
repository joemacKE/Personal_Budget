# Personal_Budget


## 🧠 **PROJECT TITLE: PERSONAL BUDGET MANAGER**

---

### 📘 **Concepts Covered**

* OOP principles (encapsulation, inheritance, polymorphism)
* Input/output handling
* Custom exception classes
* List/dictionary manipulation
* Conditional logic
* Data persistence (save/load JSON)

---

### 📋 **HIGH-LEVEL TASK**

Build a system where users can register themselves, input their income and monthly expenses, and the system will evaluate their spending, classify them, and offer simple budgeting advice.

---

### 🧱 **BREAKDOWN BLOCKS**

---

### 1. **Create the Base Class `Person`**

* Attributes:

  * `name`, `age`, `occupation`
* Methods:

  * Input personal details with validation
  * Print a summary of the person's identity

---

### 2. **Create Derived Classes: `Saver`, `Spender`**

* Inherit from `Person`
* Override a method to classify the person based on spending ratio
* Use `polymorphism` for classification logic

---

### 3. **Create a Custom Exception `InvalidBudgetData`**

* Trigger if:

  * Income is less than zero
  * Expenses are unreasonable (e.g., more than 150% of income)

---

### 4. **Add Method to Collect Financial Data**

* Ask for:

  * Monthly income
  * Number of months
  * At least 3 monthly expense items (name + amount)
* Store as a dictionary in `self.expenses`

---

### 5. **Implement Calculations**

* Total income over the period
* Total expenses
* Net savings
* Weekly allowance (based on total savings and months)
* Expense-to-income ratio

---

### 6. **Classify Financial Health**

* Use polymorphism in `Saver` and `Spender` to define:

  * Saver if expenses < 50% of income
  * Spender if expenses > 70%
  * Else, Balanced
* Display category to the user

---

### 7. **Implement Save and Load Methods**

* Convert object to dictionary
* Save to JSON
* Load from JSON using a class method

---

### 8. **Main Flow**

* While user wants to continue:

  * Ask what kind of user: saver/spender/other
  * Instantiate the correct object
  * Run all collection and calculation steps
  * Save data to file
  * Ask if user wants to enter another

---

### 🚀 BONUS IDEAS

* Add a method to recommend cost-cutting based on top 3 largest expenses
* Track multiple months and visualize change in savings

---

Would you also like a similar [Django version of this project](f), an [assignment focused on data validation and error handling](f), or a [version that integrates file uploads and graphs](f)?
