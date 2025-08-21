# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template, request, jsonify
from library.classes.package_reader import PackageReader
from library.classes.package_updater import PackageUpdater
from library.classes.common_update_strategy import CommonUpdateStrategy
from library.classes.pip_update_strategy import PipUpdateStrategy

pipup = Flask(__name__, template_folder="web", static_folder="static")


@pipup.route("/", methods=['GET'])
def index():
    return redirect(url_for("show_outdated"))


@pipup.route("/api/get_outdated_packages", methods=['GET'])
def get_outdated_packages():
    o_package_reader = PackageReader()
    outdated_packages = o_package_reader.run()

    return jsonify({
        "status": "success",
        "data": outdated_packages
    }), 200


@pipup.route("/outdated", methods=['GET'])
def show_outdated():
    return render_template("outdated.html")


@pipup.route("/api/update", methods=['POST'])
def update_package():
    package_name = request.data.decode("utf-8")

    o_updater = PackageUpdater()
    o_updater.set_strategy(
        PipUpdateStrategy() if package_name == "pip" else CommonUpdateStrategy())
    o_updater.update(package_name)

    return jsonify({
        "status": "success",
        "message": f"Package '{package_name}' updated successfully."
    }), 200


if __name__ == "__main__":
    pipup.run(debug=True)
