# Docker Tag Images, Using Python Slim Buster.
FROM vckyouuu/geezprojects:buster
# ==========================================
#              CyberDyne - Userbot
# ==========================================
RUN git clone -b CyberDyne-Userbot https://github.com/aryazakaria01/CyberDyne-Userbot /home/CyberDyne-Userbot \
    && chmod 777 /home/CyberDyne-Userbot \
    && mkdir /home/CyberDyne-Userbot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/CyberDyne-Userbot/

WORKDIR /home/CyberDyne-Userbot/

# Finishim
CMD ["python3","-m","userbot"]
