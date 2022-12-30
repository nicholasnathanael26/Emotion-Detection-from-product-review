from flask import Flask, render_template, request, redirect
from textblob import TextBlob
import text2emotion as te
import pygal
import cairo
from matplotlib import pyplot as plt

app = Flask(__name__)

# function index ini akan di load pertama oleh halaman index.html, ketika flask dijalankan
# maka akan menjalankan alamat url http://127.0.0.1:5000/
@app.route("/")
def index():
    #akan mereturn template index.html yang ada di folder templates
    return render_template('index.html')

#disini tempat function yang menerima data dari index.html
@app.route("/emotion-detection", methods=['POST'])
def detection():
    #mengecek apakah method yang di pakai di form index.html yaitu POST atau bukan
    if request.method == 'POST':
        # mengambil data inputan komentar dan di simpan dalam varibel komentar
        komentar = request.form['komentar']

        # textblob sentiment polarity akan menghasilkan angka 1 atau -1
        # bila 1 komentar tersebut positif, bila -1 komentar tersebut negatif
        feedback_polarity = TextBlob(komentar).sentiment.polarity
        if feedback_polarity > 0:
            result = 'positif'
        else:
            result = 'negatif'
    #inisialisasi varibael data yang isinya list
    data = list()
    # Call to the function
    # variabel dict_emotion dan percent_emotion menyimpan hasil dari analisis kalimat
    dict_emotion = te.get_emotion(komentar)
    percent_emotion = te.get_percent_emotion(komentar)
    # perulangan ini untuk mendapatkan value dari dictionary {"Happy": 0.5, "Angry": 0, "Surprise": 3.5, "Sad": 0, "Fear": 0}
    for key, value in dict_emotion.items():
        #disini akan masuk ke list data value dari happy dan surprise
        data.append(value)

    #membuat hasil menjadi gambar
    pie_chart = pygal.Pie()
    pie_chart.title = 'Pie chart'

    pie_chart.add('Happy', percent_emotion['Happy'])
    pie_chart.add('Angry', percent_emotion['Angry'])
    pie_chart.add('Surprise', percent_emotion['Surprise'])
    pie_chart.add('Sad', percent_emotion['Sad'])
    pie_chart.add('Fear', percent_emotion['Fear'])
    pie_chart = pie_chart.render_data_uri()


    return render_template("index.html", hasil=result,chart = pie_chart, komen=komentar, percent_emotion=percent_emotion)


if __name__ == "__main__":
    app.run(debug=True)