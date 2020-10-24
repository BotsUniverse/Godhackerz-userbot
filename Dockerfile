FROM rohithaditya/Godhackerz-userbot:latest

#clonning repo 
RUN git clone https://github.com/rohithaditya/Godhackerz-userbot.git
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
