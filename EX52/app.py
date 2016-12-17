from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        session['scene'] = generic_death
        return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            session['scene'] = generic_death
            return render_template('you_died.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                session['scene'] = generic_death
                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)

    else:
        session['scene'] = map.generic_death
        return render_template('you_died.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redierect the browser to the url for game_get

app.secret_key = 'abcabcabc'

if __name__ ==  "__main__":
    app.run()
