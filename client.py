# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template

pipup = Flask(__name__, template_folder="web", static_folder="static")


@pipup.route("/", methods=['GET'])
def index():
    return redirect(url_for("show_installed"))


@pipup.route("/installed", methods=['GET'])
def show_installed():
    return render_template("installed_modules.html")


@pipup.route("/outdated", methods=['GET'])
def show_outdated():
    return render_template("outdated_modules.html")


if __name__ == "__main__":
    pipup.run(debug=True)
