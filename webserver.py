import picoweb
import ure as re

lockstatus = "unlocked"

app = picoweb.WebApp(__name__)

# note /static/ route is implicit.


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    print(req.path)
    yield from app.render_template(resp, "home.html", (req,))

@app.route(re.compile("/*"))
def serve(req, resp):
    yield from picoweb.start_response(resp)
    print(req.path)
    yield from app.render_template(resp, req.path, (req,))

@app.route("/api/status")
def getStatus(req, resp):
    pass #TODO

@app.route("/api/status", methods=['POST'])
def postStatus(req, resp):
    pass #TODO

@app.route("/api/unlocks")
def getUnlocks(req, resp):
    pass #TODO

@app.route("/api/hwstatus")
def getHardwareStatus(req, resp):
    pass #TODO


import ulogging as logging
logging.basicConfig(level=logging.INFO)

app.run(debug=False)

