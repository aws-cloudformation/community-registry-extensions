FROM public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:3.0 

COPY requirements.txt ./
RUN pyenv global 3.7.13
RUN python -m pip install --upgrade pip 
RUN python -m pip install -r requirements.txt
