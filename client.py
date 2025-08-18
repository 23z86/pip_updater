# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template
from library.classes.package_reader import PackageReader

pipup = Flask(__name__, template_folder="web", static_folder="static")


@pipup.route("/", methods=['GET'])
def index():
    return redirect(url_for("show_outdated"))


@pipup.route("/get_outdated_modules", methods=['GET'])
def get_outdated_modules():
    o_package_reader = PackageReader()
    outdated_modules = o_package_reader.run()

    return outdated_modules


@pipup.route("/outdated", methods=['GET'])
def show_outdated():
    return render_template("outdated_modules.html")


if __name__ == "__main__":
    pipup.run(debug=True)
