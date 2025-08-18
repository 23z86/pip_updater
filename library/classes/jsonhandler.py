import json


class JSONHandler:
    def write_modules_as_json_file(self, modules):
        with open("outdated_modules.json", 'w', encoding='utf-8') as file:
            json.dump(modules, file, indent=4)

    def read_modules_from_json_file(self):
        try:
            with open("outdated_modules.json", 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
