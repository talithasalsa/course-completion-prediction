def calculate_total_and_status():
    nilai = {}
    nilai["LC1"] = float(input("Masukkan nilai LC1: "))
    nilai["GC1"] = float(input("Masukkan nilai GC1: "))
    nilai["LC2"] = float(input("Masukkan nilai LC2: "))
    nilai["GC2"] = float(input("Masukkan nilai GC2: "))
    nilai["LC3"] = float(input("Masukkan nilai LC3: "))
    nilai["GC3"] = float(input("Masukkan nilai GC3: "))
    nilai["presentasi"] = float(input("Masukkan nilai presentasi: "))
    nilai["M1"] = float(input("Masukkan nilai M1: "))

    bobot = {
        "Graded Challenges": 0.20,
        "Live Codes": 0.30,
        "Milestone": 0.35,
        "presentasi": 0.15
    }

    graded_challenges = (nilai["GC1"] + nilai["GC2"] + nilai["GC3"]) / 3 * bobot["Graded Challenges"]
    live_codes = (nilai["LC1"] + nilai["LC2"] + nilai["LC3"]) / 3 * bobot["Live Codes"]
    milestone = nilai["M1"] * bobot["Milestone"]
    presentasi = nilai['presentasi'] * bobot["presentasi"]

    total_nilai = graded_challenges + live_codes + milestone + presentasi

    def get_status(total_nilai):
        if total_nilai < 70:
            return "Nice try bestie, tetap semangat!!!"
        elif 70 <= total_nilai < 80:
            return "Participant"
        elif 80 <= total_nilai < 90:
            return "Graduate"
        elif 90 <= total_nilai <= 95:
            return "Honors"
        else:
            return "Teacher's Award"

    status = get_status(total_nilai)

    return total_nilai, status

total_nilai, status = calculate_total_and_status()
print("Total Nilai:", total_nilai)
print("Predikat:", status)