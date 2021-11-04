
<h1 align='center'>Candphy</h1>
<p align='center'>
<img height='275px' width='260px' src='https://raw.githubusercontent.com/perseu912/candphy/main/img/Candphy.png' style='height:450; witdh:200'>
 <br/>
<a href="https://twitter.com/BezerraReinan"><img title="Autor" src="https://img.shields.io/badge/Autor-reinan_br-blue.svg?style=for-the-badge&logo=twitter"></a>
<br/>
<p align='center'>
<!-- github dados -->
<a href='https://python.org'><img src='https://img.shields.io/github/pipenv/locked/python-version/perseu912/candphy'></a>
<a href='#'><img src='https://img.shields.io/github/languages/code-size/perseu912/candphy'></a>
<a href='#'><img src='https://img.shields.io/github/commit-activity/w/perseu912/candphy'></a>
<a href='#'><img src='https://img.shields.io/github/last-commit/perseu912/candphy'></a>
<br/>
<!-- sites de pacotes -->
<a href='https://pypi.org/project/qfunction/'><img src='https://img.shields.io/pypi/v/candphy'></a>
<a href='#'><img src='https://img.shields.io/pypi/wheel/candphy'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/candphy"></a>
<a href='#'><img src='https://img.shields.io/pypi/implementation/candphy'></a>
<br/>
<!-- outros premios e analises -->
<a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/perseu912/candphy?logo=codefactor">
</a>
<!-- redes sociais -->
<br/>
<a href='https://instagram.com/gpftc_ifsertao/'><img src='https://shields.io/badge/insta-gpftc_ifsertao-violet?logo=instagram&style=flat'></a>
</p>
</p>
<p align='center'> <b>Library from Python3.+ for development,  works, researches, and more other works and projects on the more points of physic  📈📊</b></p>

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
output:
```sh
Detached kernel driver
Found Rafael Micro R820T tuner
[R82XX] PLL not locked!
Exact sample rate is: 3100000.092387 Hz
Reattached kernel driver
{'freq_center': 99900000.0, 'freq_rate': 3100000.0, 'bytes': 1024, 'order': 1000000.0, 'size_signal': 262144, 'samples': array([-0.00392157-0.00392157j, -0.00392157-0.00392157j,
       -0.00392157-0.00392157j, ...,  0.1372549 -0.0745098j ,
       -0.10588235+0.15294118j, -0.16078431+0.10588235j]), 'type': 'signal_radio'}    
```
<img height='270px' src='https://raw.githubusercontent.com/perseu912/candphy/main/tests/signal_radio_plot.png' >