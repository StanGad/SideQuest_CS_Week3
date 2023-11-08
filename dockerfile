FROM python:3
#image de base = ubunut

#si on part pas d'un image ubunutu par exempl
#on install python3 dans l'image
#yes pour repondre oui au question d'installation

WORKDIR /

ADD . .
#ajoute chaque fichier a l'image 

RUN pip install uvicorn
RUN pip install fastapi


#RUN uvicorn API:app --reload 
ENTRYPOINT ["uvicorn", "./chatroom/API:app", "--host", "0.0.0.0", "--port", "8000"]
#modification du port d'ecoute quand run -> docker run -p 8000:8000  a13e76c6c8b8 
#"0.0.0.0" accept all conection incoming from any ip adress

RUN echo "Hello it is running"




