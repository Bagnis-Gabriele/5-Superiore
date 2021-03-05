import semaforo #classe semaforo
from flask import Flask, render_template, request #flask mi serve per la connessione, render template per le pagine html e request per il form
import time #per calcolare il tempo del semaforo (pausa tra colori)
import sqlite3 #necessario per collegare il database
import datetime #necessario per reperire data e ora

app = Flask(__name__) 

#semaforo
s = semaforo.semaforo()

#parametri del semaforo (configurabili)
t_verde = 1
t_giallo = 1
t_rosso = 1
acceso = 2
intervallo = 1

#pagina di test
@app.route('/test')
def test():
    #importo i parametri di configurazione
    global t_verde
    global t_giallo
    global t_rosso
    global acceso
    global intervallo
    global s
    if (acceso == 1):
        #il semaforo è acceso, quindi faccio un test del giro di colori
        s.rosso(t_rosso)
        s.verde(t_verde)
        s.giallo(t_giallo)
    else:
        #il semaforo è spento, provo l'intervallo
        for _ in range(3):
            s.giallo(intervallo)
            s.luci_spente(intervallo)
    return 'TEST ESEGUITO!'

#pagina di configurazione
@app.route('/config', methods=['GET', 'POST'])
def config():
    #importo i parametri di configurazione
    global t_verde
    global t_giallo
    global t_rosso
    global acceso
    global intervallo
    error = None
    #leggo i valori passati tramite POST dal form in html
    if request.method == 'POST':
        t_verde = int(request.form['verde'])
        t_giallo = int(request.form['giallo'])
        t_rosso = int(request.form['rosso'])
        intervallo = int(request.form['intervallo'])
        acceso = int(request.form['stato'])-1

    #Scrittura su Database
    conn = sqlite3.connect("static/semaforo.db")
    cur= conn.cursor()
    data = datetime.datetime.now()
    query=(f'INSERT INTO Semaforo(Data,Ora,t_verde,t_giallo,t_rosso,intervallo,acceso) VALUES ("{data.strftime("%x")}","{data.strftime("%X")}",{t_verde},{t_giallo},{t_rosso},{intervallo},{acceso})')
    cur.execute(query)
    conn.commit() #necessario per salvare le modifiche
    conn.close()

    return render_template('config.html', error=error)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')