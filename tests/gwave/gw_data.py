from candphy.waves import gwaves

gw = gwaves.Gwaves_Data()

#printing the DataFrame of Gravitational Waves
pd_gw = gw.data_gw
print('columns:')
print(pd_gw)