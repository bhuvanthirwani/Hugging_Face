FROM ollama/ollama:latest

ENV OLLAMA_HOST=0.0.0.0:7860
EXPOSE 7860

ENV OLLAMA_ORIGINS="*"
ENV OLLAMA_NUM_PARALLEL=1
ENV OLLAMA_MAX_LOADED_MODELS=1
ENV OLLAMA_KEEP_ALIVE=0

ENV GOMAXPROCS=2

ENV OLLAMA_MODELS=/.ollama/models
RUN mkdir -p /.ollama/models && chmod -R 777 /.ollama

RUN ollama serve & \
    sleep 10 && \
    ollama pull llama3.2:1b-instruct-q4_K_M && \
    pkill ollama

CMD ["serve"]