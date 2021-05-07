# csv-to-pdf
Python program that converts csv files to pdf.
This project is meant to take a CSV file and convert its contents into a pdf that is easy to read.
This version is primitive. It currently sorts the rows by the first row. In order for the pdf to look proper, put the bin numbers in the first row of the csv file.
The pdf begins to become hard to read when more than around 10 columns are input, so keep this in mind.
In order to run the program, in your terminal, navigate to the directory where the python file is stored and make sure that the csv file that is being used is in the same directory. 
Enter the command 'python CSV_to_PDF.py your_csv.csv' where 'your_csv.csv' is replaced by your actual csv file.
In the same directory, a pdf should appear named 'CSV_to_PDF.pdf'. By going to this in your file explorer and double clicking on it, you should now have your csv file in pdf form! 
I have included a basic csv file that was used for testing. The bin numbers are out of order on purpose. The program should sort them and color code them so that every even bin number's row is a different color from white. 
As stated before, this version is very new and there will be future changes made to it so that the user can customize their pdf more, as well as make it more usable in general. 
