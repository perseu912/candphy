
<h1 align='center'>Toddy</h1>
<p align='center'>
<img height='150px' width='200px' src='https://raw.githubusercontent.com/gpftc/qfunction/main/img/q_logo.png' style='height:200; witdh:200'>
 <br/>
<a href="https://github.com/perseu912"><img title="Autor" src="https://img.shields.io/badge/Autor-reinan_br-blue.svg?style=for-the-badge&logo=github"></a>
<br/>
<p align='center'>
<!-- github dados -->
<a href='https://python.org'><img src='https://img.shields.io/github/pipenv/locked/python-version/perseu912/toddy'></a>
<a href='#'><img src='https://img.shields.io/github/languages/code-size/perseu912/toddy'></a>
<a href='#'><img src='https://img.shields.io/github/commit-activity/w/perseu912/toddy'></a>
<a href='#'><img src='https://img.shields.io/github/last-commit/perseu912/toddy'></a>
<br/>
<!-- sites de pacotes -->
<a href='https://pypi.org/project/qfunction/'><img src='https://img.shields.io/pypi/v/toddy'></a>
<a href='#'><img src='https://img.shields.io/pypi/wheel/toddy'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/toddy"></a>
<a href='#'><img src='https://img.shields.io/pypi/implementation/toddy'></a>
<br/>
<!-- outros premios e analises -->
<a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/perseu912/toddy?logo=codefactor">
</a>
<!-- redes sociais -->
<br/>
<a href='https://instagram.com/gpftc_ifsertao/'><img src='https://shields.io/badge/insta-gpftc_ifsertao-violet?logo=instagram&style=flat'></a>
</p>
</p>
<p align='center'> <b>Library for development,  works, researches, and more other works and projects on the more points of physic  📈📊</b></p>

## First time
<br/>

## Installation:
<hr/>

this lib is found on the site of packages for python the <a href='https://pypi.org'>pypi</a> and on the site that is a repository for the codes and softwares with licenses from majority business of the word, the <a href='https://github.com'>github</a>.
### Linux
```bash
$ pip3 install candphy -U
```
### Windows
```cmd
C\:> python3 -m pip3 install candphy -U
```
<br/><br/>
##  Examples
<hr/>

### Waves

#### Signal Radio 
(need the RTL-SDR driver)

```py
from  candphy.waves import get_signal_radio as gr,plot_signal as ps
from candphy.logs import show_console 

#showing the logs from work lib
show_console(True)

#getting signals samples from 
#the around of the frequency 99.9Mhz
#(raio from space get is of 3.1Mhz)
s = gr(99.9)

print(s)

#plotting this signal radio
ps(s)
'''

```