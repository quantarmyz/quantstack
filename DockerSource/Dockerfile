##  ████████▄   ███    █▄     ▄████████ ███▄▄▄▄       ███        ▄████████     ███        ▄████████  ▄████████    ▄█   ▄█▄ 
##  ███    ███  ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███ ▀█████████▄   ███    ███ ███    ███   ███ ▄███▀ 
##  ███    ███  ███    ███   ███    ███ ███   ███    ▀███▀▀██   ███    █▀     ▀███▀▀██   ███    ███ ███    █▀    ███▐██▀   
##  ███    ███  ███    ███   ███    ███ ███   ███     ███   ▀   ███            ███   ▀   ███    ███ ███         ▄█████▀    
##  ███    ███  ███    ███ ▀███████████ ███   ███     ███     ▀███████████     ███     ▀███████████ ███        ▀▀█████▄    
##  ███    ███  ███    ███   ███    ███ ███   ███     ███              ███     ███       ███    ███ ███    █▄    ███▐██▄   
##  ███  ▀ ███  ███    ███   ███    ███ ███   ███     ███        ▄█    ███     ███       ███    ███ ███    ███   ███ ▀███▄ 
##  ▀██████▀▄█ ████████▀    ███    █▀   ▀█   █▀     ▄████▀    ▄████████▀     ▄████▀     ███    █▀  ████████▀    ███   ▀█▀ 
##                                                                                                             ▀         

### QUANTARMY STACK 3.1
### 2024 - JCX@QUANTARMY.COM
### QUANTARMY.COM - PYTHONPARATRADING.COM
#################################

# Dockerfile.
# - Como se construye la imagen.
########################################################################################

FROM continuumio/miniconda3:23.3.1-0

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends git nodejs gcc g++ exa nano && \
    chmod 777 /opt

RUN mkdir /WorkingData
WORKDIR /WorkingData

COPY --chown=${NB_UID}:${NB_GID} req.txt /tmp/
COPY --chown=${NB_UID}:${NB_GID} overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json

RUN conda install -c conda-forge jupyterlab ta-lib nodejs jupyterlab-night
RUN pip install --no-cache-dir --requirement /tmp/req.txt 

RUN echo "c.Completer.use_jedi = False" >> /opt/conda/etc/jupyter/jupyter_notebook_config.py
RUN echo "c.ResourceUseDisplay.track_cpu_percent = True" >> /opt/conda/etc/jupyter/jupyter_notebook_config.py
COPY --chown=${NB_UID}:${NB_GID} extension.py /root/.zipline/extension.py
COPY --chown=${NB_UID}:${NB_GID} qa_datalake.py /opt/conda/lib/python3.10/site-packages/zipline/data/bundles/qa_datalake.py
COPY --chown=${NB_UID}:${NB_GID} .env /root/.env
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]