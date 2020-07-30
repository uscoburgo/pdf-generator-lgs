from fpdf import FPDF 
import pandas as pd
from sendEmail import enviaMail


df = pd.read_csv("beaches.csv", index_col = 0)
x = 2
beach_name = df.iloc[x]["Name"]
address = df.iloc[x]["Address"]
direction = df.iloc[x]["Direction"]
experience = df.iloc[x]["Experience"]
bottom = df.iloc[x]["Bottom"]
best_wind = df.iloc[x]["Best wind"]
best_swell = df.iloc[x]["Best swell"]
latlong = df.iloc[x]["latlong"]
swell_height = df.iloc[x]["Swell Height"]
swell_direction = df.iloc[x]["Swell direction"]
swell_period = df.iloc[x]["Swell period"]
wind_speed = df.iloc[x]["Wind speed"]
wind_direction = df.iloc[x]["Wind direction"]
water_temp = df.iloc[x]["Water temperature"]
weather = df.iloc[x]["Weather Description"]

# FPDF('P', 'mm', 'A4')
pdf = FPDF()
pdf.add_page()


#Titulo de PDF
#pdf.set_font("Arial", "B", 35)
#pdf.text(50,30, " Let's Go Surfing! ")
#pdf.set_xy(0,35)
pdf.image("images/theboyz.JPG", x = 30, y = 10, w = 150, h = 100, type = '', link = '')

#Nombre de Report y nombre de Playa
pdf.set_xy(10,105)
pdf.set_font("Courier", "", 24)
pdf.cell(w=0, h = 20 , txt = f" Forecast report for {beach_name} ", border = 0, ln = 0, align = 'C', fill = False)

# Subtitulo con el nivel recomendado del surfero
pdf.set_xy(10,115)
pdf.set_font("Courier", "B", 16)
pdf.cell(w=0, h = 20 , txt = f" Recommended surfer experience: {experience} ", border = 0, ln = 0, align = 'C', fill = False)

pdf.set_xy(1,140)
pdf.set_font("Courier", "", 14)
pdf.cell(w=208, h = 20 , txt = f" Direction: {direction}     Water Temp Cº: {water_temp}     Seabed: {bottom} ", border = 0, ln = 0, align = 'C', fill = False)
pdf.image("images/right_arrow.png", x = 30, y = 160, w = 20, h = 20, type = '', link = '')
pdf.image("images/warm.png", x = 100, y = 160, w = 13, h = 25, type = '', link = '')
pdf.image("images/beach_break.png", x = 160, y = 160, w = 20, h = 20, type = '', link = '')
#pdf.set_xy(1,150)
##pdf.set_font("Courier", "", 14)
#pdf.cell(w=208, h = 20 , txt = f" Water temp Cº: {water_temp} ", border = 1, ln = 0, align = 'C', fill = False)

#pdf.set_xy(1,150)
#pdf.set_font("Courier", "", 14)
#pdf.cell(w=208, h = 20 , txt = f" Seabed: {bottom} ", border = 1, ln = 0, align = 'R', fill = False)

#pdf.set_xy(10,140)
#pdf.set_font("Courier", "", 14)
#pdf.cell(w=0, h = 20 , txt = f" Ideal wind direction at this beach: {best_wind} ", border = 0, ln = 0, align = 'L', fill = False)

pdf.set_xy(1,190)
pdf.set_font("Courier", "", 14)
pdf.cell(w=208, h = 20 , txt = f" Weather: {weather}     Swell Height: {swell_height} ", border = 0, ln = 0, align = 'C', fill = False)
#pdf.cell(w=208, h = 20 , txt = f" Wind direction: {wind_direction}     Wind speed: {wind_speed} kph ", border = 0, ln = 0, align = 'C', fill = False)


pdf.set_xy(1,250)
pdf.set_font("Courier", "B", 14)
pdf.multi_cell(w=200, h = 10 , txt = f" ADDITIONAL INFO: Swell Direction = {swell_direction}, Wind Direction = {wind_direction}, Wind Speed = {wind_speed} kph ", border = 0,  align = 'C', fill = False)


#pdf.set_xy(1,230)
#pdf.set_font("Courier", "", 14)
#pdf.cell(w=208, h = 20 , txt = f" Weather: {weather} ", border = 0, ln = 0, align = 'C', fill = False)

pdf.set_xy(0,275)
pdf.set_font("Courier", "", 12)
pdf.multi_cell(w=200, h = 10 , txt = f" Address: {address} ", border = 0,  align = 'C', fill = False)

# fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
#pdf.cell(0, h=10, txt = 'Lets Go Surfing', border = 1, ln = 2, align = 'C', fill = False, link = '')

#df = pd.read_csv("beaches.csv", index_col = 0)
#data = df.iloc[1]
#pdf.text(10,10,f"{data}")
#pdf.text(10,15,"Hola, Mundillo!")

pdf.output("forecastPDF.pdf")
#enviaMail()

"""
# fpdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
#pdf.image(poke_data["evolution_chain"][poke_data["id"]]["sprite"],pdf.get_x()+35.001,pdf.get_y() 
"""
