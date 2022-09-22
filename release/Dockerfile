FROM public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0 

COPY requirements.txt ./
RUN yum install -y python3.7
RUN python3.7 -m pip install --upgrade pip 
RUN python3.7 -m pip install -r requirements.txt
