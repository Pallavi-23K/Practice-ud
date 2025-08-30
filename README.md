
# Arithmetic Logger  

A simple **Python Logger project** demonstrating the use of the built-in `logging` module.  
This program logs arithmetic operations (**addition, subtraction, multiplication, division**) with timestamps, log levels, and outputs logs both to **console** and a **file (`app1.log`)**.  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Features
- Uses Python’s built-in **logging** module  
- Multiple log levels: `DEBUG`, `ERROR`  
- Logs include timestamps and log source name  
- Logs are written to both **console** and **file (`app1.log`)**  
- Demonstrates logging in real-world arithmetic functions  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠 Requirements
- Python 3.x  

No external libraries required.  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  How to Run
1. Open the terminal.  
2. Navigate to the project directory:  
   ```bash
   cd path/to/Arithmetic-Logger
``'

3. Run the script:

   ```bash
   python logs.py
   ```
4. Logs will be displayed in the console and also saved in **`app1.log`**.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧾 Example Code

```python
add(10,15)
subtract(15,10)
multiply(10,20)
divide(20,0)
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 📜 Sample Output (console & app1.log)

2025-08-30 17:20:45 - ArithmethicApp - DEBUG - Adding 10 + 15 = 25
2025-08-30 17:20:45 - ArithmethicApp - DEBUG - Subtracting 15 - 10 = 5
2025-08-30 17:20:45 - ArithmethicApp - DEBUG - Multiplying 10 * 20 = 200
2025-08-30 17:20:45 - ArithmethicApp - ERROR - Division by zero error

--------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 📂 Project Structure

```
Arithmetic-Logger/
│── logs.py           # Main program
│── app1.log          # Log file generated after execution
│── README.md         # Documentation
```


