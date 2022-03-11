FROM pytorch/pytorch:1.8.0-cuda11.1-cudnn8-runtime


WORKDIR /app

RUN  apt-get update && apt-get install git -y

COPY setup_new_env_1.sh ./

RUN chmod 777 -R setup_new_env_1.sh && bash setup_new_env_1.sh


COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" , "app.py"]