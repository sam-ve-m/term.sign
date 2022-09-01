#!/bin/bash
fission spec init
fission env create --spec --name term-sign-env --image nexus.sigame.com.br/fission-async:0.1.7 --builder nexus.sigame.com.br/fission-builder-3.8:0.0.1
fission fn create --spec --name term-sign-fn --env term-sign-env --src "./func/*" --entrypoint main.terms_sign --executortype newdeploy --maxscale 1
fission route create --spec --name term-sign-rt --method POST --url /term/sign --function term-sign-fn