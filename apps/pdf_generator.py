from fpdf import FPDF
from datetime import date
import matplotlib.pyplot as plt


def hist_plot(data, column, title=''):
    plt.figure(figsize=(8, 6))
    hist = plt.hist(data[column], bins=30, color='red')
    plt.title(title, fontsize=18)
    plt.savefig(f'../images/{column}.png')
    return hist


def montly_plot(data):
    ax = data.groupby('city')['montly_rent'].mean().plot(kind='bar',
                                                         color='r',
                                                         figsize=(6, 2),
                                                         rot=0)
    plt.title('AVG MONTLY RENT PER CITY - €', fontsize=6)
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=6)
    labels = ['Berlin', 'Munich', 'Dusseldorf', 'Cologne', 'Dortmund',
              'Frankfurt', 'Nuremberg', 'Stuttgart', 'Hamburg',
              'Hanover', 'Leipzig']
    if len(data['city'].unique()) == 11:
        ax.set_xticklabels(labels=labels)
    plt.savefig(f'../images/montly_rent_barplot.png', dpi=100)


def m2_plot(data):
    ax = data.groupby('city')['m2_value'].mean().plot(kind='bar',
                                                 color='r',
                                                 figsize=(6, 2),
                                                 rot=0)
    plt.title('AVG M² PRICE PER CITY - €', fontsize=6)
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=6)
    labels = ['Berlin', 'Munich', 'Dusseldorf', 'Cologne', 'Dortmund',
              'Frankfurt', 'Nuremberg', 'Stuttgart', 'Hamburg',
              'Hanover', 'Leipzig']
    if len(data['city'].unique()) == 11:
        ax.set_xticklabels(labels=labels)
    plt.savefig(f'../images/m2_barplot.png', dpi=100)


def pet_plot(data):
    data['pets'].value_counts().plot(kind='bar',
                                     color='r',
                                     figsize=(6, 2),
                                     rot=0)
    plt.title('PETS', fontsize=10)
    plt.xticks(fontsize=5)
    plt.savefig(f'../images/pet_plot.png', dpi=100)
    return None


def pdf_creator(data):
    '''receive some data and create a pdf report with a summary of information'''
    width = 210
    today = date.today()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # header display
    pdf.image('../images/germany_flag1.png')
    pdf.image('../images/header_pdf.png', 70, 10)
    #pdf.cell(f'Date: {today}')

    # descriptive text
    pdf.set_font('Arial', 'BU', 18)
    pdf.cell(0.1, 20, 'Data Resume:')
    pdf.set_font('Arial', 'BU', 12)
    pdf.cell(0.1, 40, f'Number of Houses:')
    pdf.set_font('Arial', size=12)
    pdf.cell(0.1, 55, f'{data.shape[0]} houses')

    pdf.set_font('Arial', 'BU', 12)
    pdf.cell(0.1, 70, f'Rent Price:')
    pdf.set_font('Arial', size=12)
    pdf.cell(0.1, 85, f'AVG - {data["montly_rent"].mean():.2f} EUR')
    pdf.cell(0.1, 95, f'MAX - {data["montly_rent"].max():.2f} EUR')
    pdf.cell(70, 105, f'MIN - {data["montly_rent"].min():.2f} EUR')

    pdf.set_font('Arial', 'BU', 12)
    pdf.cell(0.1, 70, 'Size:')
    pdf.set_font('Arial', size=12)
    pdf.cell(0.1, 85, f'AVG - {data["size"].mean():.2f}m²')
    pdf.cell(0.1, 95, f'MAX - {data["size"].max():.2f}m²')
    pdf.cell(60, 105, f'MIN - {data["size"].min():.2f}m²')

    pdf.set_font('Arial', 'BU', 12)
    pdf.cell(0.1, 70, 'Pets:')
    pdf.set_font('Arial', size=12)
    pdf.cell(0.1, 85, f'Not Allowed - {len(data[data["pets"] == "Pets not allowed"])} houses')
    pdf.cell(0.1, 95, f'Negotiable - {len(data[data["pets"] == "Pets negotiable"])} houses')
    pdf.cell(-132, 105, f'Allowed - {len(data[data["pets"] == "Pets allowed"])} houses')

    # histograms
    pdf.set_font('Arial', 'BU', 18)
    pdf.cell(0.1, 126, 'Data Histograms:')

    # first histplot
    hist_plot(data, 'montly_rent', 'MONTLY RENT')
    pdf.image('../images/montly_rent.png', 4, 126, width/2)

    # second histplot
    hist_plot(data, 'size', 'SIZE')
    pdf.image('../images/size.png', width/2, 126, width/2)

    # third histplot
    hist_plot(data, 'm2_value', 'M² VALUE')
    pdf.image('../images/m2_value.png', 4, 200, width/2)

    # fourth histplot
    hist_plot(data, 'pets', 'PETS')
    pdf.image('../images/pets.png', width/2, 200, width/2)

    # second page
    pdf.add_page()
    # header display
    pdf.image('../images/germany_flag1.png')
    pdf.image('../images/header_pdf.png', 70, 10)

    #====================
    # graphs
    #====================
    pdf.set_font('Arial', 'BU', 18)
    pdf.cell(0.1, 20, 'Data Graphs:')

    pdf.ln(20)
    montly_plot(data)
    pdf.image('../images/montly_rent_barplot.png', x=0, h=70)

    pdf.ln(5)
    m2_plot(data)
    pdf.image('../images/m2_barplot.png', x=0, h=70)

    pdf.ln(2)
    pet_plot(data)
    pdf.image('../images/pet_plot.png', x=25, h=55)

    pdf.set_author('Felipe Demenech Vasconcelos')
    pdf.close()
    pdf.output('../reports/rent_houses_germany.pdf', 'F')

    return pdf.output(dest='S')
