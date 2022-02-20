import re

license_plates = 'A578BE777 0P233787 K901MH666 CT46599 CHN2929P777 666AMP666'
private_template = r'[ABEKMNOPCTUH]\d{3}[ABEKMNOPCTUH]{2}\d{2,3}'
taxi_template = r'[ABEKMNOPCTUH]{2}\d{3}\d{2,3}'

private_cars = re.findall(private_template, license_plates)
taxi_cars = re.findall(taxi_template, license_plates)
print(f'private license plates list: {private_cars}')
print(f'taxi cars list: {taxi_cars}')

gamers = ''' Dep3kuu_CaMypau41 3a_6a3ap_oTBeTb19 kypuTe_6aM6yk16 XoJIogHbIu_TankucT9  
BupTyaJlbHblu_BouH8 cepDuTblu_oxoTHuk6 TTaPHuLLIa6 Алмазик5  9I_ODun_Takou_KPyTou4 9l_aBTopuTeT4  
ABToMaT_kaJlaLLlHukoBa4 cepb3Hblu_4eJl4 cepb3Hblu_napHuLLIa4 kpyTa9l_6a3yka4 TIpocTo_He_xaMu4 ÊÐÌÑÕRÕG3  
3a_6a3ap_oTBe4al-o3 Cama_OTTacHocTb3 cepb3Hblu3 cJlblLLI_He_Tblkau3  M9TA3 MaJlo_BpeMeHu3  
ToHupoBka_no_kpyry3 '''

naming_rules = r'\s[a-wA-W][a-wA-W0-9\/_]{2,16}\s'
# Начало и конец заключены в \s чтобы отделить совпадения друг от друга
survivors = re.findall(naming_rules, gamers)
print(f'Список ников, прошедших проверку {survivors}')


letter = '''Уважаемые! Если вы к 09:00 не вернёте 
чемодан, то уже в 09:00:01 я за себя не отвечаю. 
PS. С отношением 25:50 всё нормально!'''

time_rule = r'([01]\d|2[0-3])(:[0-5][0-9]){1,2}'
time_swap = re.sub(time_rule, '(TBD)', letter)

print(f'Письмо Вовочки теперь выглядит так: {time_swap}')
