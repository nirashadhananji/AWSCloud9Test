{"filter":false,"title":"app.py","tooltip":"/flask-request-app/app.py","undoManager":{"mark":26,"position":26,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":56},"action":"insert","lines":["from flask import Flask,render_template","","app = Flask(__name__)","","@app.route(\"/\")","def hello_world():","    return  render_template('index.html')","","if __name__ == '__main__':","    app.run(debug = True, host='127.0.0.1', port='8080')"],"id":1}],[{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"remove","lines":["7"],"id":2},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"remove","lines":["2"]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"remove","lines":["1"]}],[{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["0"],"id":3}],[{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"remove","lines":["1"],"id":4}],[{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["0"],"id":5}],[{"start":{"row":0,"column":39},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":6},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"remove","lines":["e"]},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"remove","lines":["t"]},{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"remove","lines":["a"]},{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"remove","lines":["l"]},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"remove","lines":["p"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"remove","lines":["m"]},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"remove","lines":["e"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"remove","lines":["t"]}],[{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"remove","lines":["_"],"id":7},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"remove","lines":["r"]},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"remove","lines":["e"]},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["d"]},{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"remove","lines":["n"]}],[{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"remove","lines":["e"],"id":8},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"remove","lines":["r"]},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"remove","lines":[","]}],[{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"remove","lines":[")"],"id":9},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"remove","lines":["'"]},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"remove","lines":["l"]},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"remove","lines":["m"]},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"remove","lines":["t"]}],[{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"remove","lines":["h"],"id":10},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"remove","lines":["."]},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"remove","lines":["x"]},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"remove","lines":["e"]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"remove","lines":["d"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"remove","lines":["n"]},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"remove","lines":["i"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["'"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["("]}],[{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"remove","lines":["e"],"id":11},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"remove","lines":["t"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["a"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["l"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["p"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["m"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["e"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["t"]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"remove","lines":["_"],"id":12},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"remove","lines":["r"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"remove","lines":["e"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"remove","lines":["d"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"remove","lines":["n"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["e"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"remove","lines":["r"]}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"remove","lines":[" "],"id":13},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"remove","lines":[" "]}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":[" "],"id":14},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["<"]}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["p"],"id":15},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":[">"]}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["H"],"id":16},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["e"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["l"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["l"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["<"],"id":17},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["/"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["p"]}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":[">"],"id":18}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["\""],"id":19}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["\""],"id":20}],[{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"remove","lines":["'"],"id":21}],[{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"remove","lines":["'"],"id":22}],[{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"remove","lines":[","],"id":23}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":40},"action":"remove","lines":["host='0.0.0.0'"],"id":24}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":[" "],"id":25}],[{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":[","],"id":26}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":50},"action":"insert","lines":["host='0.0.0.0'"],"id":27}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":99,"selection":{"start":{"row":4,"column":18},"end":{"row":4,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1702781939943,"hash":"5caf9214403ceaa2bb7e79ee274019b0aa1c3385"}