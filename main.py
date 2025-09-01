# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template, request, jsonify
import subprocess

from library.classes.pipup import PipUp
from library.classes.concrete_checker import PackageChecker


class PipUpAPI():
    def __init__(self):
        self.o_pipup_server = Flask(__name__, template_folder="web",
                                    static_folder="static")
        self.register_routes()

        self.o_pipup = PipUp()
        self.o_checker = PackageChecker()

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

        try:
            self.o_checker.run(package_name=package_name)
            self.o_pipup.update_package(package_name)

            return jsonify({
                "status": "Update successfully executed.",
                "status_code": 100,
                "message": f"Package '{package_name}' updated successfully."
            }), 200

        except ModuleNotFoundError as error:
            return jsonify({
                "status": "Update failed!",
                "status_code": 400,
                "message": str(error.msg)
            }), 200
            
        except subprocess.CalledProcessError as error:
                return jsonify({
                    "status_code": error.returncode,
                    "status": "Update failed!",
                    "message": f"Error in subprocess with code {error.returncode}."
                }), 500
    def run(self):
        self.o_pipup_server.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == "__main__":
    pipup_app = PipUpAPI()
    pipup_app.run()
