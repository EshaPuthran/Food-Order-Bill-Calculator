#  Food Order & Bill Calculator

A beginner-friendly **Food Order & Bill Calculator** built using **Python and Streamlit**.

This project was created as a mini project after learning the basic concepts of Python, including variables, data types, user input, operators, conditional statements, and output formatting.

## Live Application

 **Live Demo:**
[https://food-order-bill-calculator.streamlit.app](https://food-order-bill-calculator.streamlit.app/)



## Project Overview

The Food Order & Bill Calculator allows users to select a food item, enter the quantity, and automatically calculate the total bill.

The application also applies a discount based on the total order amount and displays the final bill.

The project demonstrates how basic Python concepts can be used to create a simple real-world application.

##  Features

*  Enter customer name
*  Select a food item from the menu
*  Enter the quantity
*  Automatically calculate the total amount
*  Apply discounts based on the bill amount
*  Display the final bill
*  Access the application through a web browser

##  Menu

| Food Item       | Price |
| --------------- | ----: |
|  Burger       |  ₹120 |
|  Pizza        |  ₹250 |
|  Sandwich     |  ₹100 |
|  French Fries |   ₹80 |

##  Discount Rules

| Total Amount | Discount    |
| ------------ | ----------- |
| ₹500 or more | 10%         |
| ₹300 – ₹499  | 5%          |
| Below ₹300   | No discount |

##  Calculation

The application calculates the bill using:

**Total Amount = Price × Quantity**

**Final Bill = Total Amount − Discount**

##  Python Concepts Used

This project uses the basic Python concepts learned during the hands-on session:

* Variables
* Data types
* `input()`
* `print()`
* Type conversion using `int()`
* Arithmetic operators
* Comparison operators
* `if`
* `elif`
* `else`
* Basic calculations
* Formatted output

##  Project Structure

```text
Food-Order-Bill-Calculator/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

### File Description

**`app.py`**
Contains the basic Python console version of the Food Order & Bill Calculator.

**`streamlit_app.py`**
Contains the web-based version of the application built using Streamlit.

**`requirements.txt`**
Contains the Python dependency required to run the Streamlit application.

**`README.md`**
Contains the project documentation.

##  Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/EshaPuthran/Food-Order-Bill-Calculator.git
```

### 2. Open the project folder

```bash
cd Food-Order-Bill-Calculator
```

### 3. Install Streamlit

```bash
pip install streamlit
```

Or install the dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

The application will open in your web browser.

##  Console Version

The original Basic Python version can be run using:

```bash
python app.py
```

This version runs directly in the VS Code terminal.

##  Deployment

The web version of this project is deployed using **Streamlit Community Cloud**.

The application is connected to the GitHub repository and uses:

```text
Repository: Food-Order-Bill-Calculator
Branch: main
Main file: streamlit_app.py
```


##  Learning Objective

The main objective of this project is to apply basic Python programming concepts to a simple real-world problem.

The project follows the basic programming flow:

```text
Input
  ↓
Store Data
  ↓
Process Data
  ↓
Make Decisions
  ↓
Display Result
```

##  Future Improvements

The project can be extended in the future by adding:

* Multiple food items in a single order
* Shopping cart functionality
* Order summary
* Tax calculation
* Different payment methods
* Order history
* Downloadable bills
* More interactive UI features

##  Author

**Esha Puthran**

GitHub:
https://github.com/EshaPuthran

##  License

This project is created for educational and learning purposes.
