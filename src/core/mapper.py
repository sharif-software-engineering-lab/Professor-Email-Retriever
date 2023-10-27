from model.professor import Professor


class Mapper:
    PROFESSORS = [
        Professor("Mehdi Kharrazi", r"خرازی|kharrazi|kharazi", "kharrazi@sharif.edu"),
    ]

    def get(message):
        results = []
        for professor in Mapper.PROFESSORS:
            if professor.match(message):
                results.append(professor)
        return results

