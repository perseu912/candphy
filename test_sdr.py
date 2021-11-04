from  candphy.waves import get_signal_radio as gr,plot_signal as ps
from candphy.logs import show_console 


show_console(False)

s = gr(99.9)

print(s)

ps(s)
