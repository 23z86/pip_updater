# pylint: disable=missing-docstring

from flask import Flask, redirect, url_for, render_template, request, jsonify
import subprocess

from library.classes.pipman import PipMan
from library.classes.concrete_checker import PackageChecker
from library.classes.requests_runner import RequestsRunner


class PipManAPI():
    def __init__(self):
        self.o_pipman_server = Flask(__name__, template_folder="web",
                                     static_folder="static")
        self.register_routes()
        self.register_api_endpoints()

        self.o_pipman = PipMan()
        self.o_checker = PackageChecker(RequestsRunner())

    def register_routes(self):
        self.o_pipman_server.add_url_rule(
            "/", "index", self.index, methods=["GET"])

        self.o_pipman_server.add_url_rule(
            "/main", "main", self.main, methods=["GET"])

    def register_api_endpoints(self):
        self.o_pipman_server.add_url_rule("/api/get_outdated_packages",
                                          "get_outdated_packages", self.get_outdated_packages, methods=["GET"])

        self.o_pipman_server.add_url_rule(
            "/api/search_package", "search_package", self.search_package, methods=["GET"])

        self.o_pipman_server.add_url_rule(
            "/api/update", "update_package", self.update_package, methods=["POST"])

    def set_status_message(self, data):
        return "No data found." if data == [] else "Data retrieved successfully."

    def index(self):
        return redirect(url_for("main"))

    def get_outdated_packages(self):
        outdated_packages = self.o_pipman.read_outdated_packages()

        status_message = self.set_status_message(outdated_packages)

        return jsonify({
            "status": status_message,
            "data": outdated_packages
        }), 200

    def main(self):
        return render_template("main.html")

    def search_package(self):
        package_name = request.args.get('name')
        try:
            self.o_checker.run(package_name=package_name)

            return jsonify({
                "status": "Package found.",
                "status_code": 100,
                "message": f"Package '{package_name}' found on PyPi."
            }), 200

        except ModuleNotFoundError as error:
            return jsonify({
                "status": "Package not found!",
                "status_code": 400,
                "message": str(error.msg)
            }), 200

    def update_package(self):
        package_name = request.data.decode("utf-8")

        try:
            self.o_checker.run(package_name=package_name)
            self.o_pipman.update_package(package_name)

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
        # self.o_pipup_server.run(host='0.0.0.0', port=5000)
        self.o_pipman_server.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == "__main__":
    pipman_app = PipManAPI()
    pipman_app.run()
