from fpdf import FPDF #had to 'pip install fpdf'
import pandas as pd
import sys

if len(sys.argv) != 2:
    print("Not enough arguments entered. Exiting.")
    sys.exit()


with open(sys.argv[1]) as csvfile:
    df = pd.read_csv(csvfile) 
df = df.sort_values(by=[df.columns[0]])



class PDF(FPDF):

    def table(self):
        try:
            #self.set_right_margin(10)
            num_cols = len(df.columns)

            self.add_page()
            if(num_cols < 10):
                self.set_font('Times', '', 10.0)
            else:
                self.set_font('Times', '', 20-(num_cols+.5))
            epw = pdf.w - (pdf.l_margin*2)
            col_width = epw/num_cols
            
            #heads = df.columns.values.tolist()
            data = df.values.tolist()
            data.insert(0, df.columns.values.tolist())
            text_height = pdf.font_size
            count = 0
            self.set_text_color(0, 0, 0)
            self.set_fill_color(255, 255, 255)
            for row in data:
                count += 1
                datum_counter = 0
                switch = False
                for datum in row:
                    if count == 1:
                        self.set_fill_color(51, 153, 255)
                        #self.set_font('Times', '', 10)
                        self.cell(col_width, 2*text_height, str(datum), border=1, align='L', fill=1)
                        datum_counter += 1
                    else:
                        if (datum_counter == 0) and (datum % 2 == 0):
                            self.set_fill_color(153, 153, 255)
                            #print('yo')
                            self.cell(col_width, 2*text_height, str(datum), border=1, align='L', fill=1)
                            switch = True
                        else:
                            if switch:
                                self.cell(col_width, 2*text_height, str(datum), border=1, align='L', fill=1)
                            else:
                                self.cell(col_width, 2*text_height, str(datum), border=1, align='L', fill=0)
                        #self.set_font('Times', '', 11)
                        datum_counter += 1

                self.ln(2 * text_height)
            self.ln(2* text_height)
            
        except Exception as e:
            print(f"Exception {e}")

pdf = PDF()
pdf = PDF(orientation='P', unit='mm', format='A4')
pdf.table()
pdf.output('CSV_to_PDF.pdf', 'F')
