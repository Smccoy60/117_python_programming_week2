Purpose:
This is for someone to be able to enter their expenses one by one and end up with a total expense reimbursement at the end. 

Code Explanation: 
The first line of the code tells the program to start with 0.

Then I want to prompt the user to enter the first expense amount.  I entered the code as a float to get the valued entered to equal a number instead of a string value. 

Once their first value is entered, then the logic says that if the entry is not equal to 0, print the Beginning total and the amount that was added to give a new total.  I used an f-string because it allowed me to be able to put  the variables that I wanted to use into the print line such as total and expenses which were defined in the two lines of code above the print line. I added the .2f into the lines to make sure that the output would be to two decimal places after the decimal.  I changed it to 3 just to play with it a bit and then it went out to 3 decimal places.  In my world, two is the most common use. 

I added the print(), so it would print a blank line before giving the user a final total.

The loop ends once the user enters a "0", which was defined in the expense variable definition in the 2nd line of the coding. 

One of the many things, I was missing at first, was the indentation of the last print.  I had it indented to be in line with the rest of the code and was then seeing that it was printing Final Total above every line whenever I would run the program.  I moved the line back so it wasn't indented and that fixed the problem. 