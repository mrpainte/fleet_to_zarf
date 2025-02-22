FROM ubuntu

# nvm requirements
RUN apt-get update
RUN echo "y" | apt-get install curl
# nvm env vars
RUN mkdir -p /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
# IMPORTANT: set the exact version
ENV NODE_VERSION v20.15.1
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"
# add node and npm to the PATH
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/bin
ENV PATH $NODE_PATH:$PATH
RUN npm -v
RUN node -v
RUN npm install -g @angular/cli

# FROM ubuntu
# RUN apt-get update
# RUN apt-get upgrade -y
# RUN apt-get install -y curl

# ENV NVM_DIR ~/.nvm #, depending


# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash \
#     && . ~/.nvm/nvm.sh \
#     && nvm install --lts \
#     && nvm alias default node \
#     && npm install -g @angular/cli
# RUN bash -l -c "source /root/.bashrc"
