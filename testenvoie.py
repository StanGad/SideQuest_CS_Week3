import subprocess

# Commande curl
curl_command = 'curl -X POST -H "Content-Type: application/json" -d \'{"body": "Hello, 125!", "author": "Stan"}\' http://localhost:8000/chat'

# Exécutez la commande curl depuis le script Python
try:
    subprocess.run(curl_command, shell=True, check=True)
    print("Message envoyé avec succès.")
except subprocess.CalledProcessError as e:
    print(f"Échec de l'envoi du message. Code d'état : {e.returncode}")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
