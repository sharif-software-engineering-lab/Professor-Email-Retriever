from model.professor import Professor


class Mapper:
    PROFESSORS = [
        Professor("Mohammad Ali Abam", r"آبام|ابام|abam", "abam@sharif.edu"),
        Professor("Morteza Amini", r"امینی|amini", "amini@sharif.edu"),
        Professor("Mohsen Ansari", r"انصاری|ansari", "ansari@sharif.edu"),
        Professor("Hossein Asadi", r"اسدی|asadi", "asadi@sharif.edu"),
        Professor("Hamid Beigy", r"بیگی|beigi|beigy", "beigy.sharif.edu"),
        Professor("Alireza Ejlali", r"اجلالی|ejlali", "ejlali@sharif.edu"),
        Professor("MohammadAmin Fazli", r"فضلی|fazli", "fazli@sharif.edu"),
        Professor("Gholamreza Ghassem-Sani", r"قاسم ثانی|قاسمثانی|ghasemsani|ghasem sani", "sani@sharif.edu"),
        Professor("Maziar Goudarzi", r"گودرزی|goudarzi|godarzi", "goudarzi@sharif.edu"),
        Professor("Jafar Habibi", r"حبیبی|habibi", "jhabibi@sharif.edu"),
        Professor("Shaahin Hessabi", r"حسابی|hesabi", "hesabi@sharif.edu"),
        Professor("Abbas Heydarnoori", r"حیدرنوری|حیدر نوری|heidarnoori|heydarnoori", "heydarnoori@sharif.edu"),
        Professor("Mohammad Izadi", r"ایزدی|izadi", "izadi@sharif.edu"),
        Professor("Mahdi Jafari Siavoshani", r"جعفری|jafari", "mjafari@sharif.edu"),
        Professor("Amir Hossein Jahangir", r"حهانگیر|jahangir", "jahangir@sharif.edu"),
        Professor("Rasool Jalili", r"جلیلی|jalili", "jalili@sharif.edu"),
        Professor("Shohreh Kasaei", r"کسایی|کسائی|kasaei", "kasaei@sharif.edu"),
        Professor("Mehdi Kharrazi", r"خرازی|kharrazi|kharazi", "kharrazi@sharif.edu"),
        Professor("Somayyeh Koohi", r"کوهی|koohi", "koohi@sharif.edu"),
        Professor("Mohammad Taghi Manzuri", r"منظوری|manzuri|manzouri", "manzuri@sharif.edu"),
        Professor("Seyed-Hassan Mirian-Hosseinabadi", r"میریان|mirian", "mirian@sharif.edu"),
        Professor("Seyed Abolfazl Motahari", r"مطهری|motahari|mottahari", "motahari@sharif.edu"),
        Professor("Ali Movaghar", r"موقر|movaghar", "movaghar@sharif.edu"),
        Professor("Hamid Reza Rabiee", r"ربیعی|rabiee", "rabiee@sharif.edu"),
        Professor("Raman Ramsin", r"رامسین|ramsin", "ramsin@sharif.edu"),
        Professor("Mohammad Hossein Rohban", r"رهبان|rohban", "rohban@sharif.edu"),
        Professor("Bardia Safaei", r"صفایی|صفائی|safaei", "safaei@sharif.edu"),
        Professor("Hossein Sameti", r"صامتی|sameti", "sameti@sharif.edu"),
        Professor("Hamid Sarbazi-Azad", r"سربازی|sarbazi", "azad@sharif.edu"),
        Professor("Mahdieh Soleymani Baghshah", r"سلیمانی|soleymani", "soleymani@sharif.edu"),
        Professor("Hamid Zarrabi-Zadeh", r"ضرابی|zarrabi|zarabi", "zarrabi@sharif.edu"),
    ]

    def get(message):
        results = []
        for professor in Mapper.PROFESSORS:
            if professor.match(message):
                results.append(str(professor))
        return "\n".join(results)

