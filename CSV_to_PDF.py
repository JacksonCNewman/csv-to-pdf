from fpdf import FPDF #had to 'pip install fpdf'
import pandas as pd
import sys
import matplotlib as mpl #had to 'pip install matplotlib'
from pathlib import Path
from matplotlib.afm import AFM
import math
afm_path = Path(mpl.get_data_path(), 'fonts', 'afm', 'ptmr8a.afm')

with afm_path.open('rb') as fh:
    afm = AFM(fh)


if len(sys.argv) != 2:
    print("Not enough arguments entered. Exiting.")
    sys.exit()

with open(sys.argv[1]) as csvfile:
    df = pd.read_csv(csvfile) 
df = df.sort_values(by=[df.columns[0]])

heads = df.columns.values.tolist()
col_dict = dict.fromkeys(heads)


# this code creates a dictionary with the df's heads stored as keys and their columns' max length data cell stored as their values
# this is for mathmatical work later on
# it is ghetto i know ;_;
dict_iterator = 0
col_list = []
max_len = 0
for column_name, column in df.transpose().iterrows():
    col_list = list(column)
    for i in col_list:
        if isinstance(i, int):
            temp_str = str(i)
            if afm.string_width_height(temp_str)[0]*.01 > max_len:
                max_len = afm.string_width_height(temp_str)[0]*.01
        elif afm.string_width_height(i)[0]*.01 > max_len:
            max_len = afm.string_width_height(i)[0]*.01
    col_dict[heads[dict_iterator]] = max_len
    dict_iterator += 1
    max_len = 0
# END OF DICT CREATING ##########
#col_dict['student name'] = 34.5
#print(afm.string_width_height('A'))

min_cell_width = 0
for x in heads:
    min_cell_width += col_dict[x]

# so now i need to mess with this basic ui and tell the user what orientation should be used
# in order to fit the rows or warn the that they have too many rows even for landscape.
# after this i need to give the user the option to change the font size if their csv is too wide


orientation = input("Enter the orientation of the paper as L for landscape or P for portrait (Landscape is suggested for when more than 10 columns are present): ")
orientation = str(orientation.upper())
if orientation == 'Q':
    sys.exit()
if orientation != 'L' and orientation != 'P':
    orientation = input("Your input was not valid, please enter a valid input. Type L for landscape or P for portrait.")
    orientation = str(orientation.upper())
    if orientation == 'Q':
        sys.exit()
    if orientation != 'L' and orientation != 'P':
        print("Input is not valid. Portrait is selected by default.")
        orientation = 'P'

class PDF(FPDF):

    def table(self):
        try:
            num_cols = len(df.columns)

            self.add_page()
            self.set_font('Times', '', 10.0)

            actual_page_width = pdf.w - (pdf.l_margin*2)
            col_width = actual_page_width/num_cols

            data = df.values.tolist()
            data.insert(0, heads)
            text_height = pdf.font_size
            count = 0 
            self.set_text_color(0, 0, 0)
            self.set_fill_color(255, 255, 255)
            
            #this calculates the total min cell width passed in 

            space_left = actual_page_width - min_cell_width
            addi_width = space_left/len(heads)

            

            for index, row in df.iterrows():
                row_count = 0
                count += 1
                datum_counter = 0
                switch = False
                for i in row:
                    if count == 1:
                        self.set_fill_color(51, 153, 255)
                        #self.set_font('Times', '', 10)
                        self.cell(col_dict[heads[row_count]] + addi_width, 2*text_height, str(i), border=1, align='C', fill=1)
                        datum_counter += 1
                        row_count += 1
                    else:
                        if (datum_counter == 0) and (i % 2 == 0):
                            self.set_fill_color(153, 153, 255)
                            #print('yo')
                            self.cell(col_dict[heads[row_count]] + addi_width, 2*text_height, str(i), border=1, align='C', fill=1)
                            switch = True
                        else:
                            if switch:
                                self.cell(col_dict[heads[row_count]] + addi_width, 2*text_height, str(i), border=1, align='C', fill=1)
                            else:
                                self.cell(col_dict[heads[row_count]] + addi_width, 2*text_height, str(i), border=1, align='C', fill=0)
                        row_count += 1
                        datum_counter += 1
                
                self.ln(2 * text_height)
            self.ln(2* text_height)
            
        except Exception as e:
            print(f"Exception {e}")



pdf = PDF()
pdf = PDF(orientation=orientation, unit='pt', format='A4')
pdf.table()
pdf.output('CSV_to_PDF.pdf', 'F')
