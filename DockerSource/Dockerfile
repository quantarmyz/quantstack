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
# - Dede miniconda 3 actualiza e instala git.
# - Mueve configuraciones, crea directorios e instala via conda y pip

########################################################################################

FROM continuumio/miniconda3:23.3.1-0

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends git locate ranger nodejs gcc g++ && \
    chmod 777 /opt

RUN mkdir /WorkingData
WORKDIR /WorkingData
COPY --chown=${NB_UID}:${NB_GID} req.txt /tmp/
COPY --chown=${NB_UID}:${NB_GID} overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json

RUN conda install -c conda-forge jupyterlab ta-lib nodejs jupyterlab-night
RUN pip install --no-cache-dir --requirement /tmp/req.txt 
RUN pip install nbconvert==5.6.1
RUN echo "c.Completer.use_jedi = False" >> /opt/conda/etc/jupyter/jupyter_notebook_config.py
RUN echo "c.ResourceUseDisplay.track_cpu_percent = True" >> /opt/conda/etc/jupyter/jupyter_notebook_config.py

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]