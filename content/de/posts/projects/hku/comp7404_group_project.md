---
title: "xDeepFM für Empfehlungssysteme"
date: 2020-11-11T16:30:25+08:00
draft: false
tags: ["hku", "machine learning", "comp7404"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

eXtreme Deep Factorization Machine ([xDeepFM](https://arxiv.org/abs/1803.05170))

Diese Arbeit schlägt ein neuartiges Compressed Interaction Network (CIN) vor, das darauf abzielt, Feature-Interaktionen auf explizite Weise und auf Vektorebene zu generieren.

## GitHub-Repository

[GitHub: xDeepFM_for_Recommender_Systems](https://github.com/pseudoyu/xDeepFM_for_Recommender_Systems)

## Video-Demo

[YouTube](https://www.youtube.com/watch?v=rFEGAtTZLyQ) | [Google Drive](https://drive.google.com/file/d/1qPx6H9R1b-EDP7HZpAg5bDjkzR8QEHnR/view?usp=sharing)

## Datensätze

1. **[Criteo-Datensatz](http://labs.criteo.com/2014/02/kaggle-display-advertising-challenge-dataset/).** Es handelt sich um einen bekannten Benchmark-Datensatz der Industrie zur Entwicklung von Modellen zur Vorhersage der Klickrate von Anzeigen, der öffentlich zugänglich ist. Gegeben einem Benutzer und der Seite, die er besucht, besteht das Ziel darin, die Wahrscheinlichkeit vorherzusagen, dass er auf eine bestimmte Anzeige klickt.

## Laufzeitumgebung

Ich empfehle dringend, [Anaconda](https://www.anaconda.com) für die Implementierung dieses Projekts zu verwenden. Hier sind einige einfache Anweisungen:
1. Laden Sie eine geeignete Version ([Windows](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe)/[MacOS](https://repo.anaconda.com/archive/Anaconda3-2020.07-MacOSX-x86_64.pkg)/[Linux](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh)) für Ihr Betriebssystem herunter und installieren Sie sie (prüfen Sie die neueste Version auf [Anaconda](https://www.anaconda.com))
   1. Unter Windows oder MacOS können Sie einfach den *.exe*- oder *.pkg*-Installer verwenden und den Anweisungen folgen
   2. Unter Linux müssen Sie möglicherweise `bash ./.Anaconda3-2020.07-Linux-x86_64.sh` im selben Verzeichnis der heruntergeladenen *.sh*-Datei ausführen, um dem Installer die Initialisierung von Anaconda3 in Ihrer .bashrc zu ermöglichen
2. Erstellen Sie eine dedizierte Conda-Umgebung für dieses Projekt (dringend empfohlen)
   1. Führen Sie `conda create -n xdeepfm python=3.6` aus und geben Sie `y` ein, um die Conda-Umgebung zu erstellen
   2. Führen Sie `conda activate xdeepfm` aus, um die Projektumgebung zu aktivieren
3. Führen Sie `pip install -r requirements.txt` aus, um die Paketabhängigkeiten zu installieren
4. Jetzt können Sie den Code einfach durch `python main.py` ausführen

```zsh
cd IhrPfad/xDeepFM_for_Recommender_Systems/exdeepfm
bash ./.Anaconda3-2020.07-Linux-x86_64.sh
conda create -n xdeepfm python=3.6
conda activate xdeepfm
pip install -r requirements.txt
python main.py
```

### Abhängigkeiten
- absl-py==0.8.1
- astor==0.8.0
- gast==0.3.2
- google-pasta==0.1.7
- grpcio==1.24.3
- h5py==2.10.0
- joblib==0.14.0
- Keras-Applications==1.0.8
- Keras-Preprocessing==1.1.0
- Markdown==3.1.1
- numpy==1.17.3
- packaging==19.2
- protobuf==3.10.0
- pyparsing==2.4.2
- PyYAML==5.1.2
- scikit-learn==0.21.3
- scipy==1.3.1
- six==1.12.0
- sklearn==0.0
- tensorboard==1.14.0
- tensorflow==1.14.0
- tensorflow-estimator==1.14.0
- termcolor==1.1.0
- Werkzeug==0.16.0
- wrapt==1.11.2

## Ausführungsergebnisse

![comp7404_screenshot1](https://image.pseudoyu.com/images/comp7404_screenshot1.png)

**...**

![comp7404_screenshot2](https://image.pseudoyu.com/images/comp7404_screenshot2.png)