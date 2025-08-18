# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template, request
from library.classes.package_reader import PackageReader
from library.classes.package_updater import PackageUpdater
from library.classes.common_update_strategy import CommonUpdateStrategy
from library.classes.pip_update_strategy import PipUpdateStrategy

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


@pipup.route("/update", methods=['POST'])
def update_package():
    module_name = request.data.decode("utf-8")

    o_updater = PackageUpdater()
    o_updater.set_strategy(
        PipUpdateStrategy() if module_name == "pip" else CommonUpdateStrategy())
    o_updater.update(module_name)

    return "You have successfully updated the package: " + module_name


if __name__ == "__main__":
    pipup.run(debug=True)
