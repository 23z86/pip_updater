# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template, request, jsonify

from library.classes.package_reader import PackageReader
from library.classes.package_updater import PackageUpdater
from library.classes.common_update_strategy import CommonUpdateStrategy
from library.classes.pip_update_strategy import PipUpdateStrategy


class PipUpAPI():
    def __init__(self):
        self.pipup = Flask(__name__, template_folder="web",
                           static_folder="static")
        self.register_routes()

    def register_routes(self):
        self.pipup.add_url_rule("/", "index", self.index, methods=["GET"])
        self.pipup.add_url_rule("/api/get_outdated_packages",
                                "get_outdated_packages", self.get_outdated_packages, methods=["GET"])
        self.pipup.add_url_rule(
            "/outdated", "show_outdated", self.show_outdated, methods=["GET"])
        self.pipup.add_url_rule(
            "/api/update", "update_package", self.update_package, methods=["POST"])

    def index(self):
        return redirect(url_for("show_outdated"))

    def get_outdated_packages(self):
        o_package_reader = PackageReader()
        outdated_packages = o_package_reader.run()

        return jsonify({
            "status": "success",
            "data": outdated_packages
        }), 200

    def show_outdated(self):
        return render_template("outdated.html")

    def update_package(self):
        package_name = request.data.decode("utf-8")
        o_updater = PackageUpdater()
        o_updater.set_strategy(
            PipUpdateStrategy() if package_name == "pip" else CommonUpdateStrategy()
        )
        o_updater.update(package_name=package_name)

        return jsonify({
            "status": "success",
            "message": f"Package '{package_name}' updated successfully."
        }), 200

    def run(self):
        self.pipup.run(debug=True)


if __name__ == "__main__":
    pipup_app = PipUpAPI()
    pipup_app.run()
