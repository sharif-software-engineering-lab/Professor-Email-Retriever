from model.professor import Professor
import json


class Mapper:
    PROFESSORS_FILE = "Professors.json"

    with open(PROFESSORS_FILE ) as f:
        PROFESSORS = json.loads(f.read(), object_hook=lambda x: Professor(x["name"], x["pattern"], x["email"]))

    def get(message):
        results = []
        for professor in Mapper.PROFESSORS:
            if professor.match(message):
                results.append(str(professor))
        return "\n".join(results)
