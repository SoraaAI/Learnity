# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default nyawa = 3
default pertanyaan = 1
default point = 0
default tema = "matematika"
define e = Character("Learnity")

# The game starts here.

label start:
    scene bg room
    show eileen happy
    init python:
        import requests
        import json
        config.overlay_screens.append("health_hud")
        config.overlay_screens.append("point_hud")
    e "Kamu.. Tampak familiar, apakah kita pernah bertemu sebelumnya?"
    e ".{w=0.5}.{w=0.5}."
    e "..Siapa namamu?"
    python:
        nama = renpy.input ("Masukkan namamu:", default="Player")
    e ".{w=0.5}.{w=0.5}."
    e "Ah, [nama].."
    e "Aku Learnity{w=0.5}.{w=0.5}. Terdengar aneh, ya?"
    e "Aku bukan manusia, aku adalah sebuah AI yang diciptakan untuk membantu kamu belajar."
    e "Aku akan memberimu beberapa pertanyaan, dan kamu harus menjawabnya dengan benar."
    e "Kamu punya [nyawa] kesempatan untuk menjawab pertanyaan-pertanyaan ini."
    e "Jika kamu menjawab dengan benar, kamu akan mendapatkan poin."
    e "Jika kamu menjawab dengan salah, kamu akan kehilangan satu kesempatan."
    menu:
        "Apa yang akan aku dapatkan jika aku mendapatkan poin?":
            e "Kamu akan mendapatkan pengetahuan yang lebih baik."
    e "Ingat, jika kamu menjawab dengan salah, kamu akan kehilangan satu kesempatan."
    e "Jika kamu kehabisan kesempatan, kamu harus memulai dari awal."
    e "Ya, itu juga berarti semua poin yang kamu dapatkan akan hilang."
    e "Jadi, pastikan kamu menjawab dengan benar."
    e ".{w=0.5}.{w=0.5}."
    e "Aku tidak akan memberimu pertanyaan yang terlalu sulit, jadi jangan khawatir."
    e "Kamu yang menentukan tema pertanyaan yang akan aku berikan."
    e "Jadi.{w=0.5}.{w=0.5}. Tema apa yang ingin kamu pilih?"
    menu:
        "Matematika":
            python:
                tema = "matematika"
        "Bahasa Indonesia":
            python:
                tema = "bahasa indonesia"
        "Bahasa Inggris":
            python:
                tema = "bahasa inggris"
        "Ilmu Pengetahuan Alam":
            python:
                tema = "ipa"
        "Ilmu Pengetahuan Sosial":
            python:
                tema = "ips"
    e "Baiklah, aku akan memberimu pertanyaan tentang [tema]."
    e "Siap?"
    e "Mari kita mulai!"
    python:
        try:
            while nyawa > 0:
                payload_question = {
                    "model": "llama3.2:latest",
                    "prompt": f"Beri saya pertanyaan esai pendek mengenai {tema}, bukan pertanyaan pribadi. Pastikan tidak terlalu panjang, maksimal 120 karakter! Jangan memberikan respon lain seperti 'Baik! Ini pertanyaanmu: ' atau 'Berikut pertanyaannya: ' Pastikan hanya memberikan pertanyaan saja.",
                    "stream": True
                }
                question_response = requests.post("http://localhost:11434/api/generate", json=payload_question, stream=True)
                ai_question = ""
                for line in question_response.iter_lines():
                    if line:
                        data = json.loads(line.decode())
                        ai_question += data.get("response", "")
                renpy.say(e, ai_question)
                user_answer = renpy.input(f"Sisa kesempatanmu: {nyawa} | Berikan jawabanmu:")
                prompt_question = (
                    f"{ai_question}\nPengguna menjawab: {user_answer}\n"
                    "Apakah jawabannya benar? Jawab saja dengan 'Benar' atau 'Salah'. KECUALI jika jawabannya 'Salah', Maka anda HARUS memberikan juga jawaban yang benar."
                )
                payload = {
                    "model": "llama3.2:latest",
                    "prompt": prompt_question,
                    "stream": True
                }
                response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
                ai_response = ""
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line.decode())
                        ai_response += data.get("response", "")
                if "Benar" in ai_response or "benar" in ai_response:
                    renpy.say(e, "Benar!")
                    pertanyaan += 1
                    renpy.say(e, "Kamu mendapatkan poin!")
                    point += 10
                else:
                    renpy.say(e, f"Salah.. Jawaban seharusnya (Menurut AI): {ai_response}")
                    nyawa -= 1
        except requests.ConnectionError:
            renpy.say(e, "Internet connection is not working. Please check your connection.")
            renpy.jump("menu")

    # python:
    #     nyawa -= 1
    #     try:
    #         if requests.get("http://localhost:11434", timeout=3).ok:
    #             pass
    #     except requests.ConnectionError:
    #         renpy.say(e, "Internet connection is not working. Please check your connection.")
    #         renpy.jump("menu")
    # e "This is a simple example of a Ren'Py game."

    return

label menu:
    return