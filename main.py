# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template, request, jsonify

from library.classes.pipup import PipUp
from library.classes.concrete_reader import ConcreteReader
from library.classes.concrete_updater import ConcreteUpdater
from library.classes.subprocess_runner import SubprocessRunner


class PipUpAPI():
    def __init__(self):
        self.o_pipup_server = Flask(__name__, template_folder="web",
                                    static_folder="static")
        self.register_routes()
        o_subprocess = SubprocessRunner()
        o_reader = ConcreteReader(o_subprocess)
        o_updater = ConcreteUpdater()

        self.o_pipup = PipUp(reader=o_reader, updater=o_updater)

    def register_routes(self):
        self.o_pipup_server.add_url_rule(
            "/", "index", self.index, methods=["GET"])
        self.o_pipup_server.add_url_rule("/api/get_outdated_packages",
                                         "get_outdated_packages", self.get_outdated_packages, methods=["GET"])
        self.o_pipup_server.add_url_rule(
            "/outdated", "show_outdated", self.show_outdated, methods=["GET"])
        self.o_pipup_server.add_url_rule(
            "/api/update", "update_package", self.update_package, methods=["POST"])

    def set_status_message(self, data):
        return "No data found." if data == [] else "Data retrieved successfully."

    def index(self):
        return redirect(url_for("show_outdated"))

    def get_outdated_packages(self):
        outdated_packages = self.o_pipup.read_outdated_packages()

        status_message = self.set_status_message(outdated_packages)

        return jsonify({
            "status": status_message,
            "data": outdated_packages
        }), 200

    def show_outdated(self):
        return render_template("outdated.html")

    def update_package(self):
        package_name = request.data.decode("utf-8")
        self.o_pipup.update_package(package_name)

        return jsonify({
            "status": "Update successfully executed.",
            "message": f"Package '{package_name}' updated successfully."
        }), 200

    def run(self):
        self.o_pipup_server.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == "__main__":
    pipup_app = PipUpAPI()
    pipup_app.run()
