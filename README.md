# csv-to-pdf
Python program that converts csv files to pdf.
This project is meant to take a CSV file and convert its contents into a pdf that is easy to read.
This version is primitive. It currently sorts the rows by the first row. In order for the pdf to look proper, put the bin numbers in the first row of the csv file.
In order to run the program, in your terminal, navigate to the directory where the python file is stored and make sure that the csv file that is being used is in the same directory. 
Enter the command 'python CSV_to_PDF.py your_csv.csv' where 'your_csv.csv' is replaced by your actual csv file. (There are a few test CSV files I included to show the dynamic ablity.)
In the same directory, a pdf should appear named 'CSV_to_PDF.pdf'. By going to this in your file explorer and double clicking on it, you should now have your csv file in pdf form! 
I have included basic csv files that was used for testing. The bin numbers are out of order on purpose. The program should sort them and color code them so that every even bin number's row is a different color from white. 
