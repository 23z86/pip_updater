# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template
from library.classes.package_reader import PackageReader
from library.classes.jsonhandler import JSONHandler

pipup = Flask(__name__, template_folder="web", static_folder="static")
o_package_reader = PackageReader()
o_json_handler = JSONHandler()
outdated_modules = o_package_reader.run()
o_json_handler.write_modules_as_json_file(outdated_modules)


@pipup.route("/", methods=['GET'])
def index():
    return redirect(url_for("show_installed"))


@pipup.route("/installed", methods=['GET'])
def show_installed():
    return render_template("installed_modules.html")


@pipup.route("/outdated", methods=['GET'])
def show_outdated():
    return render_template("outdated_modules.html", outdated_modules=outdated_modules)


@pipup.route("/update", methods=['POST'])
def update_module():
    pass
    return redirect(url_for("show_outdated"))

if __name__ == "__main__":
    pipup.run(debug=True)
