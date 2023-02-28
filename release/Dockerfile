FROM public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:3.0 

COPY requirements.txt ./
COPY dockercfg.json ./
RUN pyenv global 3.7.13
RUN python -m pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
RUN mkdir awscli && cd awscli && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install
RUN curl https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip -O -L \
    && unzip aws-sam-cli-linux-x86_64.zip -d sam-installation \
    && ./sam-installation/install
RUN curl https://go.dev/dl/go1.20.1.linux-amd64.tar.gz -O -L \
    && rm -rf /usr/local/go \
    && tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz
ENV PATH=/usr/local/go/bin:$PATH
RUN which go
RUN go version
RUN go env -w GOPROXY=direct
RUN GO111MODULE=on go install github.com/aws-cloudformation/rain/cmd/rain@latest
RUN mkdir /root/.docker && cp dockercfg.json /root/.docker/config.json

# This gets ignored, we have to run it in the buildspec 
ENTRYPOINT ["/usr/local/bin/dockerd-entrypoint.sh"]

