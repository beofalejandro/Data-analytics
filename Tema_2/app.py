import recomender as rc # Recommendation system class
from flask import Flask as fk, render_template as rt, request as rq

app = fk(__name__)

@app.route('/')
def index():
    return rt('index.html')

@app.route('/recomendar_pelicula', methods=['POST'])
def movie_rec():
    pelicula = str(rq.form['pelicula'])
    recomendaciones = rc.recomendar(pelicula)

    if not recomendaciones:
        recomendaciones_texto = []
    else:
        recomendaciones_texto = recomendaciones

    return rt('index.html', movie_recomended=recomendaciones_texto)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)