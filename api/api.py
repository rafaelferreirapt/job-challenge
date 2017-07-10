from flask import Flask
from settings import PORT, ALLOWED_HOSTS
from views.emails.views import app as emails

app = Flask(__name__)
app.register_blueprint(emails, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(port=PORT, host=ALLOWED_HOSTS, threaded=True)
