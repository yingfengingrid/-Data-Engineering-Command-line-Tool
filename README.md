This command line tool can be used to perform polynomial fitting experiments as well as polynomial overfitting experiments. Optionally, a *.txt file containing two columns of data can be provided or the fitting experiments can be performed by choosing to generate simulated random data.


To use the Comand line tools

To print this command in terminal
1. "cd ML_CLT"
2. "bash init.sh"

3. cd Polynomial_Fitting

The comand line tools has two mode to poly fit

4.use "python3 poly_fit.py fit --filename data.txt 2 3 4" to perform 2,3,4 order poly fit of the data from data.txt

5. use "python3 poly_fit.py fit 2 3 4" to perform 2,3,4 order poly fit of the data generate random.


use python3 poly_fit.py fit --h to check help.
