from django.shortcuts import render
import csv
import requests
from io import StringIO
# Create your views here.
def library(req):
    books =[]
    file_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQGvGyRae7ZSzI889bt78w63pVxpceEcILP-wtImvOVLfGboRtZfW7PuR88-jNrhzPPc-F8hLEuEx9Y/pub?output=csv"

    try:
        response = requests.get(file_url)
        response.raise_for_status()
        response.encoding = 'utf-8' 

        csv_data = StringIO(response.text)
        reader = csv.DictReader(csv_data)

        for row in reader:
            books.append(row)

    except Exception as e:
        print(f"Error Loading csv: {e}")
        books=[]


    return render(req, 'library.html', {'books': books})