"""
This is the entry point for the Lacquer UI application. This python file hosts the UI and preforms
the necessary functions to display the UI and authenticate the user.

Author: G.Meeser (grant.meeser@xneelo.com)
Date: Oct 2024
"""
import secrets
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, abort
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

# Create the flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.update({'SECRET_KEY': secrets.token_hex(64)})
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_port=1, x_proto=1)
CORS(app)


@app.route('/app', methods=['GET'])
@app.route('/app/<path:text>', methods=['GET'])
def web_app(text=''): # pylint: disable=unused-argument
	'''
	Renders the app page.

	This function is mapped to two routes:
	- '/app' which handles GET requests without any additional path.
	- '/app/<path:text>' which handles GET requests with an additional path parameter.

	Parameters:
		text (str): Optional path parameter. This parameter is intended to pass a route to the
		React app. Defaults to an empty string.

	Returns:
		Response: Rendered HTML page for the app.
	'''
	return render_template('app.html')


@app.route('/', methods=['GET'])
def index():
	'''
	redirects the the root page to the app page. This is the entry point for the application.
	'''
	return redirect(url_for('web_app'))

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8081, debug=True)
