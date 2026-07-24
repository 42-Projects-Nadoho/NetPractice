import time
import sys
import subprocess
import os


def jouer_alarme(fichier_audio):
    """
    Essaie plusieurs lecteurs audio natifs sous Linux.
    """
    if not os.path.exists(fichier_audio):
        print(f"\n⚠️ Fichier '{fichier_audio}' introuvable.")
        print("\a\a\a")
        return

    lecteurs = [
        ["paplay", fichier_audio],
        ["ffplay", "-nodisp", "-autoexit", fichier_audio],
        ["cvlc", "--play-and-exit", fichier_audio]
    ]

    for commande in lecteurs:
        try:
            subprocess.run(
                commande,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
            return
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue

    print(
        "\n🔊 Alarme ! (Aucun lecteur audio compatible trouvé en arrière-plan)"
    )
    print("\a\a\a")


def countdown_timer(minutes, seconds=0):
    total_seconds = minutes * 60 + seconds

    print("⏳ Minuteur démarré...")

    try:
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            time_format = f"{mins:02d}:{secs:02d}"

            print(f"\rTemps restant : {time_format}", end="", flush=True)
            time.sleep(1)
            total_seconds -= 1

        print("\r✅ C'est terminé ! L'heure est écoulée.    ")
        jouer_alarme("alarm.wav")

    except KeyboardInterrupt:
        print("\n🛑 Minuteur annulé.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            minutes = int(sys.argv[1])
            countdown_timer(minutes)
        except ValueError:
            print("Veuillez entrer un nombre valide en argument.")
    else:
        try:
            m = int(input("Combien de minutes ? "))
            countdown_timer(m)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
