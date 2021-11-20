from candphy.waves import gwaves

#instanciamint the data of graviatitonal waves
gw = gwaves.Gwaves_Data()

#getting the name of last gwave from data
gw_name = gw.data_gw['Name'][0]

#getting the gwave of this name
gwave = gw.get_gwave(name_gwave=gw_name)

#ploting the gwave signal
plt_signal = gw.plot_gwave(gwave)

plt_signal.savefig(f'signal_{gw_name}.png',dpi=900)
plt_signal.show()



