# 404B Lesson 5 Class Exercise - Object Oriented Programming

## Instructions

### Split VS Code Window

You can drag `main.py` tab to the right side of the window to split the window into two panes. This will allow you to see the instructions and the code at the same time.

### Answering

You can answer the questions by writing your answers in the `main.py` file.

You can run the code by clicking the `Run` button on the top right corner of the editor.

The output will be shown in the `Terminal` tab at the bottom of the editor.

## 1

## Questions

1. Base on the program below, what are the values of x, y of p1 after line:\
    a) `p1.move_in_x(7)`\
    b) `p1.move_in_x_twice(9)`

    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def move_in_x(self, step):
            self.x += step
        
        def move_in_x_twice(self, step):
            self.x += (2*step)
        
    p1 = Point(2, 2)
    p1.move_in_x(7)
    p1.move_in_x_twice(9)
    ```

2. Create a class called ***Name*** that has the following properties:
   - First name
   - Last name

3. Following Q2, add 2 new methods to the ***Name*** class:

   - ***normal_order()***
       - returns the person’s name in order: `<first last>`
       - e.g. “John Wick”

   - ***reverse_order()***
       - returns the person’s name in reverse order: `<last first>`
       - e.g. “Wick John”

4. Create a class called ***BankAccount*** that has the following properties:
   - Name
   - Balance

5. Following Q4, add 2 new methods to the ***BankAccount*** class:

   - ***deposit(...)***
       - accepts int/float parameters
       - increase the **balance** property by the parameter
       - e.g. “Deposit: $99,  Latest balance: $999”

   - ***withdraw(...)***
       - accepts int/float parameters
       - decrease the **balance** property by the parameter
       - e.g. “Withdraw: $99,  Latest balance: $900”

6. Following Q5, add a property ***transaction_fee*** with default value ***2.0***:

   - Deduct the transaction fee money during every `withdraw()` call.

   - Make sure the balance cannot go negative during a withdrawal.

   - If the withdrawal (amount + transaction fee) would cause it to become negative, don't modify the balance at all.

7. Following Q6, add a `transfer()` method which should move money from the current bank account to another account.

    - The method accepts two parameters:
      - a second `BankAccount` to accept the money
      - a positive number to transfer

    - There is a $5.00 transferring fee.

    - The method should modify the two `BankAccount` instances such that current instance has its balance decreased by the given amount plus the $5.00 fee, and the other account's balance is increased by the given amount.

   For example:

   ```python
    ben = BankAccount()
    ben.deposit(80.00)
    
    hal = BankAccount()
    hal.deposit(20.00)
    
    ben.transfer(hal, 20.00)
   ```

## Submitting Your Work

1. Make sure the assignment repository is opened in VS Code.

2. Make sure you have completed all the tasks.

3. (First time only)
Use Command + J to open the Terminal tab and config your git username and email:

    ```bash
    git config user.name "Your Name"
    git config user.email "Your GitHub Email"
    ```

4. Click on the "Source Control" icon on the left. Source Control

    ![1](https://github.com/BlueinnoClassroom/404B-L2.1-Template/assets/155412668/2c31026e-c14d-484f-bb9e-dc87189a0216)

5. Enter a commit message and click on the "Commit" button.

6. Click on the "Sync Changes" button.
