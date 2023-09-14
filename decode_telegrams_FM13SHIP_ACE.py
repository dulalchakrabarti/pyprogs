#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:44:10 2019
Final version on Mon Mar 30 12:15:00 2020

Code title:
Script in python to decode WMO FM13 SHIP telegram data recorded during the Antarctic Circumnavigation Expedition (ACE)

@authors:
Diogo Luís (Dept Physics, University of Aveiro, Portugal)
Irina Gorodetskaya (CESAM, Dept Physics, University of Aveiro, Portugal)
"""
import pandas as pd
import numpy as np
import glob

def ACE_telegram_decoder(file_name,output_path):
    '''
    Function for decoding Antarctic Circumnavigation Expedition (ACE) telegrams encoded with WMO FM 13 code form.
    More details on the SYNOP/SHIP code in WMO Manual on Codes (WMO-No.306), Volume I.1, Part A.
    
    Modify user-specific code lines: raw_data_directory and output_path. 
    
    Input arguments
    ---------------
    file_name : string
        Name and path of file containing the telegram to decode (e.g. './met_telegrams_ace/UBXH30202.03h').
    input file content (example for UBXH30202.03h):
     ¬¬’’ UBXH3 02031 99649 31553 41396 71806 11016 21021 49814 

     57011 77072 87500 22223 01012 20301 333// 41104 ICE 26092 =
        
    output_path : string
        Folder path where you want to save the .txt file with the decoded telegram (e.g. './Telegrams_folder/).
        
    Returns
    -------
    df : Pandas DataFrame with the information saved in the .txt file
    
    Saves a tab-separated ASCII .txt file with all the decoded information in the folder indicated in output_path with the name 'ACE_telegram_decoded_YYYY_MM_DD_HHh.txt'
    For more information on the decoded data please see the README.txt file.    
    '''
    
    telegram=open(file_name, encoding='koi8_r').readlines() #Load the telegram encoded with a russian codec
    telegram[0]=telegram[0].rstrip('\n') #Remove the newline character \n
    groups=' '.join(telegram).split() #Split the telegram by groups
    
    #Create DataFrame to save the decoded information
    df=pd.DataFrame(columns=['Symbol_Description','Code_Figure','Decoded_Information'],
                    index=['D....D','YYGG','iw','LaLaLa','Qc','LoLoLoLo','iR','ix','h','VV','N','dd','ff','1sn','TTT','2sn','TdTdTd','PPPP','a','ppp','ww','W1','W2','Nh','CL','CM','CH','GGgg','Ds','vs','ss','TwTwTw','PwPw','HwHw','dw1dw1','Pw1Pw1','Hw1Hw1','dw2dw2','Pw2Pw2','Hw2Hw2','Is','EsEs','Rs','sw','TbTbTb','ci','Si','bi','Di','zi']) 
    
    month=file_name[-8:-6] #Month of this telegram (ACE data months during 2016: 11,12; during 2017: 01,02,03,04)
    if int(month) > 10:
        year=2016
    elif int(month) < 5:
        year=2017 #Year of this telegram
    
    #List of Symbolic Letters and their description:
    #Section 0
    df.loc['D....D','Symbol_Description']='Ship call sign'
    df.loc['YYGG','Symbol_Description']='Day and Time of observation (UTC)'
    df.loc['iw','Symbol_Description']='Source and units of wind speed'
    df.loc['LaLaLa','Symbol_Description']='Latitude' #in tenths of a degree
    df.loc['Qc','Symbol_Description']='Quadrant of the globe'
    df.loc['LoLoLoLo','Symbol_Description']='Longitude' #in tenths of a degree
    #Section 1
    df.loc['iR','Symbol_Description']='Indicator for inclusion or omission of precipitation data'
    df.loc['ix','Symbol_Description']='Indicator for type of station operation and for present and past weather data'
    df.loc['h','Symbol_Description']='Height above surface of the base of the lowest cloud seen'
    df.loc['VV','Symbol_Description']='Horizontal visibility at surface'
    df.loc['N','Symbol_Description']='Total cloud cover'
    df.loc['dd','Symbol_Description']='True direction from which wind is blowing' #in tens of degrees
    df.loc['ff','Symbol_Description']='Wind speed (in units indicated by iw)'
    df.loc['1sn','Symbol_Description']='Sign of the Air temperature'
    df.loc['TTT','Symbol_Description']='Air temperature (degree Celsius)' #in tenths of a degree
    df.loc['2sn','Symbol_Description']='Sign of the Dew-point temperature'
    df.loc['TdTdTd','Symbol_Description']='Dew-point temperature (degree Celsius)' #in tenths of a degree
    df.loc['PPPP','Symbol_Description']='Pressure at mean sea level (hectopascal)' #in tenths of a hectopascal, omitting the thousands digit
    df.loc['a','Symbol_Description']='Characteristic of pressure tendency during the three hours preceding the time of observation'
    df.loc['ppp','Symbol_Description']='Amount of pressure tendency at station level during the three hours preceding the time of observation (hectopascal)' #in tenths of a hectopascal
    df.loc['ww','Symbol_Description']='Present weather'
    df.loc['W1','Symbol_Description']='Past weather during the preceding 3 hours'
    df.loc['W2','Symbol_Description']='Past weather during the preceding 3 hours'
    df.loc['Nh','Symbol_Description']='Total amount of sky covered by low (or medium clouds, if no low) cloud'
    df.loc['CL','Symbol_Description']='Types of Low Clouds (Sc, St, Cu, Cb)'
    df.loc['CM','Symbol_Description']='Types of Medium Clouds (Ac, As, Ns)'
    df.loc['CH','Symbol_Description']='Types of High Clouds (Ci, Cs, Cc)'
    df.loc['GGgg','Symbol_Description']='Time of observation, in hours and minutes UTC'
    #Section 2
    df.loc['Ds','Symbol_Description']='True direction of resultant displacement of the ship during the three hours preceding the time of observation'
    df.loc['vs','Symbol_Description']='Ship average speed made good during the three hours preceding the time of observation'
    df.loc['ss','Symbol_Description']='Indicator for the sign and type of measurement of sea-surface temperature'
    df.loc['TwTwTw','Symbol_Description']='Sea-surface temperature (degree Celsius)' #in tenths of a degree
    df.loc['PwPw','Symbol_Description']='Period of wind waves (seconds)' 
    df.loc['HwHw','Symbol_Description']='Height of wind waves (metre)'  #in units of 0.5 metre
    df.loc['dw1dw1','Symbol_Description']='True direction from which first swell waves are coming' #in tens of degrees
    df.loc['Pw1Pw1','Symbol_Description']='Period of first swell waves (seconds)'
    df.loc['Hw1Hw1','Symbol_Description']='Height of first swell waves (metre)'  #in units of 0.5 metre
    df.loc['dw2dw2','Symbol_Description']='True direction from which second swell waves are coming' #in tens of degrees    
    df.loc['Pw2Pw2','Symbol_Description']='Period of second swell waves (seconds)'
    df.loc['Hw2Hw2','Symbol_Description']='Height of second swell waves (metre)'  #in units of 0.5 metre
    df.loc['Is','Symbol_Description']='Ice accretion on ships'
    df.loc['EsEs','Symbol_Description']='Thickness of ice accretion on ships (centimetres)'
    df.loc['Rs','Symbol_Description']='Rate of ice accretion on ships'
    df.loc['sw','Symbol_Description']='Indicator for the sign and type of wet-bulb temperature reported'
    df.loc['TbTbTb','Symbol_Description']='Wet-bulb temperature (degree Celsius)' #in tenths of a degree
    df.loc['ci','Symbol_Description']='Concentration or arrangement of sea ice'
    df.loc['Si','Symbol_Description']='Stage of development'
    df.loc['bi','Symbol_Description']='Ice of land origin'
    df.loc['Di','Symbol_Description']='True bearing of principal ice edge'
    df.loc['zi','Symbol_Description']='Present ice situation and trend of conditions over preceding three hours'
  
    #---------- Section 0 ----------
    
    #D....D
    df.loc['D....D','Code_Figure']=groups[1]
    df.loc['D....D','Decoded_Information']=groups[1]
    
    #YYGGiw
    #YYGG:
    df.loc['YYGG','Code_Figure']=groups[2][0:4]
    df.loc['YYGG','Decoded_Information']=pd.Timestamp(year=int(year),month=int(month),day=int(groups[2][0:2]),hour=int(groups[2][2:4]))    
    #iw (Code table 1855):
    df.loc['iw','Code_Figure']=groups[2][4]
    if df.loc['iw','Code_Figure'] == '0':
        df.loc['iw','Decoded_Information']='Wind speed estimated (metres per second)'
    elif df.loc['iw','Code_Figure'] == '1':
        df.loc['iw','Decoded_Information']='Wind speed obtained from anemometer (metres per second)'
    elif df.loc['iw','Code_Figure'] == '3':
        df.loc['iw','Decoded_Information']='Wind speed estimated (knots)'
    elif df.loc['iw','Code_Figure'] == '4':
        df.loc['iw','Decoded_Information']='Wind speed obtained from anemometer (knots)'
    
    #99LaLaLa 
    df.loc['LaLaLa','Code_Figure']=groups[3][2:5]
    df.loc['LaLaLa','Decoded_Information']=int(df.loc['LaLaLa','Code_Figure'])*0.1    
    
    #QcLoLoLoLo
    #Qc (Code table 3333):
    df.loc['Qc','Code_Figure']=groups[4][0]
    if df.loc['Qc','Code_Figure'] == '1':
        df.loc['Qc','Decoded_Information']='North East'
    elif df.loc['Qc','Code_Figure'] == '3':
        df.loc['Qc','Decoded_Information']='South East'
    elif df.loc['Qc','Code_Figure'] == '5':
        df.loc['Qc','Decoded_Information']='South West'
    elif df.loc['Qc','Code_Figure'] == '7':
        df.loc['Qc','Decoded_Information']='North West'        
    #LoLoLoLo:
    df.loc['LoLoLoLo','Code_Figure']=groups[4][1:5]
    df.loc['LoLoLoLo','Decoded_Information']=int(df.loc['LoLoLoLo','Code_Figure'])*0.1    
    
    #---------- Section 1 ----------
    #Mandatory groups:
    
    #iRixhVV
    #iR (Code table 1819):
    df.loc['iR','Code_Figure']=groups[5][0]
    if df.loc['iR','Code_Figure'] == '0':
        df.loc['iR','Decoded_Information']='Group 6RRRtR is included in Sections 1 and 3'
    elif df.loc['iR','Code_Figure'] == '1':
        df.loc['iR','Decoded_Information']='Group 6RRRtR is included in Sections 1'
    elif df.loc['iR','Code_Figure'] == '2':
        df.loc['iR','Decoded_Information']='Group 6RRRtR is included in Sections 3'
    elif df.loc['iR','Code_Figure'] == '3':
        df.loc['iR','Decoded_Information']='Group 6RRRtR is omitted (precipitation amount = 0)'
    elif df.loc['iR','Code_Figure'] == '4':
        df.loc['iR','Decoded_Information']='Group 6RRRtR is omitted (precipitation amount not available)'
    #ix (Code table 1860):
    df.loc['ix','Code_Figure']=groups[5][1]
    if df.loc['ix','Code_Figure'] == '1':
        df.loc['ix','Decoded_Information']='Manned - Group 7wwW1W2 is included'
    elif df.loc['ix','Code_Figure'] == '2':
        df.loc['ix','Decoded_Information']='Manned - Group 7wwW1W2 is omitted (no significant phenomenon to report)'
    elif df.loc['ix','Code_Figure'] == '3':
        df.loc['ix','Decoded_Information']='Manned - Group 7wwW1W2 is omitted (no observation, data not available)'
    #h (Code table 1600):
    df.loc['h','Code_Figure']=groups[5][2]
    if df.loc['h','Code_Figure'] == '0':
        df.loc['h','Decoded_Information']='0 to 50 m'
    elif df.loc['h','Code_Figure'] == '1':
        df.loc['h','Decoded_Information']='50 to 100 m'
    elif df.loc['h','Code_Figure'] == '2':
        df.loc['h','Decoded_Information']='100 to 200 m'
    elif df.loc['h','Code_Figure'] == '3':
        df.loc['h','Decoded_Information']='200 to 300 m'
    elif df.loc['h','Code_Figure'] == '4':
        df.loc['h','Decoded_Information']='300 to 600 m'
    elif df.loc['h','Code_Figure'] == '5':
        df.loc['h','Decoded_Information']='600 to 1 000 m'
    elif df.loc['h','Code_Figure'] == '6':
        df.loc['h','Decoded_Information']='1 000 to 1 500 m'
    elif df.loc['h','Code_Figure'] == '7':
        df.loc['h','Decoded_Information']='1 500 to 2 000 m'
    elif df.loc['h','Code_Figure'] == '8':
        df.loc['h','Decoded_Information']='2 000 to 2 500 m'
    elif df.loc['h','Code_Figure'] == '9':
        df.loc['h','Decoded_Information']='2 500 m or more, or no clouds'
    elif df.loc['h','Code_Figure'] == '/':
        df.loc['h','Decoded_Information']='Height of base of cloud not known or base of clouds at a level lower and tops at a level higher than that of the station'
    #VV (Code table 4377):
    df.loc['VV','Code_Figure']=groups[5][3:5]
    if df.loc['VV','Code_Figure'] == '90':
        df.loc['VV','Decoded_Information']='< 0.05 km'
    elif df.loc['VV','Code_Figure'] == '91':
        df.loc['VV','Decoded_Information']='0.05 km'
    elif df.loc['VV','Code_Figure'] == '92':
        df.loc['VV','Decoded_Information']='0.2 km'
    elif df.loc['VV','Code_Figure'] == '93':
        df.loc['VV','Decoded_Information']='0.5 km'
    elif df.loc['VV','Code_Figure'] == '94':
        df.loc['VV','Decoded_Information']='1 km'
    elif df.loc['VV','Code_Figure'] == '95':
        df.loc['VV','Decoded_Information']='2 km'
    elif df.loc['VV','Code_Figure'] == '96':
        df.loc['VV','Decoded_Information']='4 km'
    elif df.loc['VV','Code_Figure'] == '97':
        df.loc['VV','Decoded_Information']='10 km'
    elif df.loc['VV','Code_Figure'] == '98':
        df.loc['VV','Decoded_Information']='20 km'
    elif df.loc['VV','Code_Figure'] == '99':
        df.loc['VV','Decoded_Information']='≥ 50 km'
    
    #Nddff
    #N (Code table 2700):
    df.loc['N','Code_Figure']=groups[6][0]
    if df.loc['N','Code_Figure'] == '0':
        df.loc['N','Decoded_Information']='0'
    elif df.loc['N','Code_Figure'] == '1':
        df.loc['N','Decoded_Information']='1 okta or less, but not zero'
    elif df.loc['N','Code_Figure'] == '2':
        df.loc['N','Decoded_Information']='2 oktas'
    elif df.loc['N','Code_Figure'] == '3':
        df.loc['N','Decoded_Information']='3 oktas'
    elif df.loc['N','Code_Figure'] == '4':
        df.loc['N','Decoded_Information']='4 oktas'
    elif df.loc['N','Code_Figure'] == '5':
        df.loc['N','Decoded_Information']='5 oktas'
    elif df.loc['N','Code_Figure'] == '6':
        df.loc['N','Decoded_Information']='6 oktas'
    elif df.loc['N','Code_Figure'] == '7':
        df.loc['N','Decoded_Information']='7 oktas or more, but not 8 oktas'
    elif df.loc['N','Code_Figure'] == '8':
        df.loc['N','Decoded_Information']='8 oktas'
    elif df.loc['N','Code_Figure'] == '9':
        df.loc['N','Decoded_Information']='Sky obscured by fog and/or other meteorological phenomena'
    elif df.loc['N','Code_Figure'] == '/':
        df.loc['N','Decoded_Information']='Cloud cover is indiscernible for reasons other than fog or other meteorological phenomena, or observation is not made'
    #dd (Code table 0877):
    df.loc['dd','Code_Figure']=groups[6][1:3]
    if df.loc['dd','Code_Figure'] == '00':
        df.loc['dd','Decoded_Information']='Calm'
    elif df.loc['dd','Code_Figure'] == '99':
        df.loc['dd','Decoded_Information']='Variable'
    else:
        df.loc['dd','Decoded_Information']=int(df.loc['dd','Code_Figure'])*10
    #ff
    df.loc['ff','Code_Figure']=groups[6][3:5]
    df.loc['ff','Decoded_Information']=int(df.loc['ff','Code_Figure'])    
    
    #Non-fixed groups:
    for group in groups[7:]:
        
        if group[0:3] == '222': #222 -> beginning of Section 2
            sec2=groups.index(group) #index of the first group of Section 2
            break
        
        #1snTTT
        elif group[0] == '1':
            #1sn (Code table 3845):
            df.loc['1sn','Code_Figure']=group[1]
            if df.loc['1sn','Code_Figure'] == '0':
                df.loc['1sn','Decoded_Information']='Positive or zero'
            elif df.loc['1sn','Code_Figure'] == '1':
                df.loc['1sn','Decoded_Information']='Negative'
            #TTT:
            df.loc['TTT','Code_Figure']=group[2:5]
            if df.loc['1sn','Code_Figure'] == '1':
                df.loc['TTT','Decoded_Information']=-1*int(df.loc['TTT','Code_Figure'])*0.1 
            else:
                df.loc['TTT','Decoded_Information']=int(df.loc['TTT','Code_Figure'])*0.1 
                
        #2snTdTdTd
        elif group[0] == '2':
            #2sn (Code table 3845):
            df.loc['2sn','Code_Figure']=group[1]
            if df.loc['2sn','Code_Figure'] == '0':
                df.loc['2sn','Decoded_Information']='Positive or zero'
            elif df.loc['2sn','Code_Figure'] == '1':
                df.loc['2sn','Decoded_Information']='Negative'
            elif df.loc['2sn','Code_Figure'] == '9':
                df.loc['2sn','Decoded_Information']='Relative humidity follows'
            #TdTdTd:
            df.loc['TdTdTd','Code_Figure']=group[2:5]
            if df.loc['2sn','Code_Figure'] == '9':
                df.loc['TdTdTd','Symbol_Description']='Relative humidity of the air (in per cent)'
                df.loc['TdTdTd','Decoded_Information']=int(df.loc['TdTdTd','Code_Figure']) 
            else:
                df.loc['TdTdTd','Symbol_Description']='Dew-point temperature (degree Celsius)' #in tenths of a degree
                if df.loc['2sn','Code_Figure'] == '1':
                    df.loc['TdTdTd','Decoded_Information']=-1*int(df.loc['TdTdTd','Code_Figure'])*0.1 
                else:
                    df.loc['TdTdTd','Decoded_Information']=int(df.loc['TdTdTd','Code_Figure'])*0.1 
                    
        #4PPPP
        elif group[0] == '4':
            #PPPP:
            df.loc['PPPP','Code_Figure']=group[1:5]
            if df.loc['PPPP','Code_Figure'][0] == '0':
                df.loc['PPPP','Decoded_Information']=1000+int(df.loc['PPPP','Code_Figure'])*0.1 
            else:
                df.loc['PPPP','Decoded_Information']=int(df.loc['PPPP','Code_Figure'])*0.1 
        
        #5appp
        elif group[0] == '5':
            #a (Code table 0200):
            df.loc['a','Code_Figure']=group[1]
            if df.loc['a','Code_Figure'] == '0':
                df.loc['a','Decoded_Information']='Increasing, then decreasing; atmospheric pressure the same or higher than three hours ago'
            elif df.loc['a','Code_Figure'] == '1':
                df.loc['a','Decoded_Information']='Increasing, then steady; or increasing, then increasing more slowly (Atmospheric pressure now higher than three hours ago)'
            elif df.loc['a','Code_Figure'] == '2':
                df.loc['a','Decoded_Information']='Increasing (steadily or unsteadily) (Atmospheric pressure now higher than three hours ago)'
            elif df.loc['a','Code_Figure'] == '3':
                df.loc['a','Decoded_Information']='Decreasing or steady, then increasing; or increasing, then increasing more rapidly (Atmospheric pressure now higher than three hours ago)'
            elif df.loc['a','Code_Figure'] == '4':
                df.loc['a','Decoded_Information']='Steady; atmospheric pressure the same as three hours ago'
            elif df.loc['a','Code_Figure'] == '5':
                df.loc['a','Decoded_Information']='Decreasing, then increasing; atmospheric pressure the same or lower than three hours ago'
            elif df.loc['a','Code_Figure'] == '6':
                df.loc['a','Decoded_Information']='Decreasing, then steady; or decreasing, then decreasing more slowly (Atmospheric pressure now lower than three hours ago)'
            elif df.loc['a','Code_Figure'] == '7':
                df.loc['a','Decoded_Information']='Decreasing (steadily or unsteadily) (Atmospheric pressure now lower than three hours ago)'
            elif df.loc['a','Code_Figure'] == '8':
                df.loc['a','Decoded_Information']='Steady or increasing, then decreasing; or decreasing, then decreasing more rapidly (Atmospheric pressure now lower than three hours ago)'
            #ppp:
            df.loc['ppp','Code_Figure']=group[2:5]
            df.loc['ppp','Decoded_Information']=int(df.loc['ppp','Code_Figure'])*0.1 
            
        #Group 6RRRtR not included in ACE Telegrams
        
        #7wwW1W2
        elif group[0] == '7':
            #ww (Code table 4677):
            df.loc['ww','Code_Figure']=group[1:3]
            if df.loc['ww','Code_Figure'] == '00':
                df.loc['ww','Decoded_Information']='Cloud development not observed or not observable'
            elif df.loc['ww','Code_Figure'] == '01':
                df.loc['ww','Decoded_Information']='Clouds generally dissolving or becoming less developed'
            elif df.loc['ww','Code_Figure'] == '02':
                df.loc['ww','Decoded_Information']='State of sky on the whole unchanged'
            elif df.loc['ww','Code_Figure'] == '03':
                df.loc['ww','Decoded_Information']='Clouds generally forming or developing'
            elif df.loc['ww','Code_Figure'] == '04':
                df.loc['ww','Decoded_Information']='Visibility reduced by smoke, e.g. veldt or forest fires, industrial smoke or volcanic ashes'
            elif df.loc['ww','Code_Figure'] == '05':
                df.loc['ww','Decoded_Information']='Haze'
            elif df.loc['ww','Code_Figure'] == '06':
                df.loc['ww','Decoded_Information']='Widespread dust in suspension in the air, not raised by wind at or near the station at the time of observation'
            elif df.loc['ww','Code_Figure'] == '07':
                df.loc['ww','Decoded_Information']='Blowing spray at the station'
            elif df.loc['ww','Code_Figure'] == '08':
                df.loc['ww','Decoded_Information']='Well-developed dust whirl(s) or sand whirl(s) seen at or near the station during the preceding hour or at the time of observation, but no duststorm or sandstorm'
            elif df.loc['ww','Code_Figure'] == '09':
                df.loc['ww','Decoded_Information']='Duststorm or sandstorm within sight at the time of observation, or at the station during the preceding hour'
            elif df.loc['ww','Code_Figure'] == '10':
                df.loc['ww','Decoded_Information']='Mist'
            elif df.loc['ww','Code_Figure'] == '11':
                df.loc['ww','Decoded_Information']='Patches of shallow fog or ice fog at the station, whether on land or sea, not deeper than about 2 metres on land or 10 metres at sea'
            elif df.loc['ww','Code_Figure'] == '12':
                df.loc['ww','Decoded_Information']='More or less continuous shallow fog or ice fog at the station, whether on land or sea, not deeper than about 2 metres on land or 10 metres at sea'
            elif df.loc['ww','Code_Figure'] == '13':
                df.loc['ww','Decoded_Information']='Lightning visible, no thunder heard'
            elif df.loc['ww','Code_Figure'] == '14':
                df.loc['ww','Decoded_Information']='Precipitation within sight, not reaching the ground or the surface of the sea'
            elif df.loc['ww','Code_Figure'] == '15':
                df.loc['ww','Decoded_Information']='Precipitation within sight, reaching the ground or the surface of the sea, but distant, i.e. estimated to be more than 5 km from the station'
            elif df.loc['ww','Code_Figure'] == '16':
                df.loc['ww','Decoded_Information']='Precipitation within sight, reaching the ground or the surface of the sea, near to, but not at the station'
            elif df.loc['ww','Code_Figure'] == '17':
                df.loc['ww','Decoded_Information']='Thunderstorm, but no precipitation at the time of observation'
            elif df.loc['ww','Code_Figure'] == '18':
                df.loc['ww','Decoded_Information']='Squalls at or within sight of the station during the preceding hour or at the time of observation'
            elif df.loc['ww','Code_Figure'] == '19':
                df.loc['ww','Decoded_Information']='Funnel cloud(s) at or within sight of the station during the preceding hour or at the time of observation'
            elif df.loc['ww','Code_Figure'] == '20':
                df.loc['ww','Decoded_Information']='Drizzle (not freezing) or snow grains not falling as shower(s)'
            elif df.loc['ww','Code_Figure'] == '21':
                df.loc['ww','Decoded_Information']='Rain (not freezing) not falling as shower(s)'
            elif df.loc['ww','Code_Figure'] == '22':
                df.loc['ww','Decoded_Information']='Snow not falling as shower(s)'
            elif df.loc['ww','Code_Figure'] == '23':
                df.loc['ww','Decoded_Information']='Rain and snow or ice pellets not falling as shower(s)'
            elif df.loc['ww','Code_Figure'] == '24':
                df.loc['ww','Decoded_Information']='Freezing drizzle or freezing rain not falling as shower(s)'
            elif df.loc['ww','Code_Figure'] == '25':
                df.loc['ww','Decoded_Information']='Shower(s) of rain'
            elif df.loc['ww','Code_Figure'] == '26':
                df.loc['ww','Decoded_Information']='Shower(s) of snow, or of rain and snow'
            elif df.loc['ww','Code_Figure'] == '27':
                df.loc['ww','Decoded_Information']='Shower(s) of hail, or of rain and hail'
            elif df.loc['ww','Code_Figure'] == '28':
                df.loc['ww','Decoded_Information']='Fog or ice fog'
            elif df.loc['ww','Code_Figure'] == '29':
                df.loc['ww','Decoded_Information']='Thunderstorm (with or without precipitation)'
            elif df.loc['ww','Code_Figure'] == '30':
                df.loc['ww','Decoded_Information']='Slight or moderate duststorm or sandstorm - has decreased during the preceding hour'
            elif df.loc['ww','Code_Figure'] == '31':
                df.loc['ww','Decoded_Information']='Slight or moderate duststorm or sandstorm - no appreciable change during the preceding hour'
            elif df.loc['ww','Code_Figure'] == '32':
                df.loc['ww','Decoded_Information']='Slight or moderate duststorm or sandstorm - has begun or has increased during the preceding hour'
            elif df.loc['ww','Code_Figure'] == '33':
                df.loc['ww','Decoded_Information']='Severe duststorm or sandstorm - has decreased during the preceding hour'
            elif df.loc['ww','Code_Figure'] == '34':
                df.loc['ww','Decoded_Information']='Severe duststorm or sandstorm - no appreciable change during the preceding hour'
            elif df.loc['ww','Code_Figure'] == '35':
                df.loc['ww','Decoded_Information']='Severe duststorm or sandstorm - has begun or has increased during the preceding hour'
            elif df.loc['ww','Code_Figure'] == '36':
                df.loc['ww','Decoded_Information']='Slight or moderate drifting snow, generally low (below eye level)'
            elif df.loc['ww','Code_Figure'] == '37':
                df.loc['ww','Decoded_Information']='Heavy drifting snow, generally low (below eye level)'
            elif df.loc['ww','Code_Figure'] == '38':
                df.loc['ww','Decoded_Information']='Slight or moderate blowing snow, generally high (above eye level)'
            elif df.loc['ww','Code_Figure'] == '39':
                df.loc['ww','Decoded_Information']='Heavy blowing snow, generally high (above eye level)'
            elif df.loc['ww','Code_Figure'] == '40':
                df.loc['ww','Decoded_Information']='Fog or ice fog at a distance at the time of observation, but not at the station during the preceding hour, the fog or ice fog extending to a level above that of the observer'
            elif df.loc['ww','Code_Figure'] == '41':
                df.loc['ww','Decoded_Information']='Fog or ice fog in patches'
            elif df.loc['ww','Code_Figure'] == '42':
                df.loc['ww','Decoded_Information']='Fog or ice fog, sky visible (has become thinner during the preceding hour)'
            elif df.loc['ww','Code_Figure'] == '43':
                df.loc['ww','Decoded_Information']='Fog or ice fog, sky invisible (has become thinner during the preceding hour)'
            elif df.loc['ww','Code_Figure'] == '44':
                df.loc['ww','Decoded_Information']='Fog or ice fog, sky visible (no appreciable change during the preceding hour)'
            elif df.loc['ww','Code_Figure'] == '45':
                df.loc['ww','Decoded_Information']='Fog or ice fog, sky invisible (no appreciable change during the preceding hour)'
            elif df.loc['ww','Code_Figure'] == '46':
                df.loc['ww','Decoded_Information']='Fog or ice fog, sky visible (has begun or has become thicker during the preceding hour)'
            elif df.loc['ww','Code_Figure'] == '47':
                df.loc['ww','Decoded_Information']='Fog or ice fog, sky invisible (has begun or has become thicker during the preceding hour)'
            elif df.loc['ww','Code_Figure'] == '48':
                df.loc['ww','Decoded_Information']='Fog, depositing rime, sky visible'
            elif df.loc['ww','Code_Figure'] == '49':
                df.loc['ww','Decoded_Information']='Fog, depositing rime, sky invisible'
            elif df.loc['ww','Code_Figure'] == '50':
                df.loc['ww','Decoded_Information']='Drizzle, not freezing, intermittent (slight at time of observation)'
            elif df.loc['ww','Code_Figure'] == '51':
                df.loc['ww','Decoded_Information']='Drizzle, not freezing, continuous (slight at time of observation)'
            elif df.loc['ww','Code_Figure'] == '52':
                df.loc['ww','Decoded_Information']='Drizzle, not freezing, intermittent (moderate at time of observation)'
            elif df.loc['ww','Code_Figure'] == '53':
                df.loc['ww','Decoded_Information']='Drizzle, not freezing, continuous (moderate at time of observation)'
            elif df.loc['ww','Code_Figure'] == '54':
                df.loc['ww','Decoded_Information']='Drizzle, not freezing, intermittent (heavy (dense) at time of observation)'
            elif df.loc['ww','Code_Figure'] == '55':
                df.loc['ww','Decoded_Information']='Drizzle, not freezing, continuous (heavy (dense) at time of observation)'
            elif df.loc['ww','Code_Figure'] == '56':
                df.loc['ww','Decoded_Information']='Drizzle, freezing, slight'
            elif df.loc['ww','Code_Figure'] == '57':
                df.loc['ww','Decoded_Information']='Drizzle, freezing, moderate or heavy (dense)'
            elif df.loc['ww','Code_Figure'] == '58':
                df.loc['ww','Decoded_Information']='Drizzle and rain, slight'
            elif df.loc['ww','Code_Figure'] == '59':
                df.loc['ww','Decoded_Information']='Drizzle and rain, moderate or heavy'
            elif df.loc['ww','Code_Figure'] == '60':
                df.loc['ww','Decoded_Information']='Rain, not freezing, intermittent (slight at time of observation)'
            elif df.loc['ww','Code_Figure'] == '61':
                df.loc['ww','Decoded_Information']='Rain, not freezing, continuous (slight at time of observation)'
            elif df.loc['ww','Code_Figure'] == '62':
                df.loc['ww','Decoded_Information']='Rain, not freezing, intermittent (moderate at time of observation)'
            elif df.loc['ww','Code_Figure'] == '63':
                df.loc['ww','Decoded_Information']='Rain, not freezing, continuous (moderate at time of observation)'
            elif df.loc['ww','Code_Figure'] == '64':
                df.loc['ww','Decoded_Information']='Rain, not freezing, intermittent (heavy at time of observation)'
            elif df.loc['ww','Code_Figure'] == '65':
                df.loc['ww','Decoded_Information']='Rain, not freezing, continuous (heavy at time of observation)'
            elif df.loc['ww','Code_Figure'] == '66':
                df.loc['ww','Decoded_Information']='Rain, freezing, slight'
            elif df.loc['ww','Code_Figure'] == '67':
                df.loc['ww','Decoded_Information']='Rain, freezing, moderate or heavy'
            elif df.loc['ww','Code_Figure'] == '68':
                df.loc['ww','Decoded_Information']='Rain or drizzle and snow, slight'
            elif df.loc['ww','Code_Figure'] == '69':
                df.loc['ww','Decoded_Information']='Rain or drizzle and snow, moderate or heavy'
            elif df.loc['ww','Code_Figure'] == '70':
                df.loc['ww','Decoded_Information']='Intermittent fall of snowflakes (slight at time of observation)'
            elif df.loc['ww','Code_Figure'] == '71':
                df.loc['ww','Decoded_Information']='Continuous fall of snowflakes (slight at time of observation)'
            elif df.loc['ww','Code_Figure'] == '72':
                df.loc['ww','Decoded_Information']='Intermittent fall of snowflakes (moderate at time of observation)'
            elif df.loc['ww','Code_Figure'] == '73':
                df.loc['ww','Decoded_Information']='Continuous fall of snowflakes (moderate at time of observation)'
            elif df.loc['ww','Code_Figure'] == '74':
                df.loc['ww','Decoded_Information']='Intermittent fall of snowflakes (heavy at time of observation)'
            elif df.loc['ww','Code_Figure'] == '75':
                df.loc['ww','Decoded_Information']='Continuous fall of snowflakes (heavy at time of observation)'
            elif df.loc['ww','Code_Figure'] == '76':
                df.loc['ww','Decoded_Information']='Diamond dust (with or without fog)'
            elif df.loc['ww','Code_Figure'] == '77':
                df.loc['ww','Decoded_Information']='Snow grains (with or without fog)'
            elif df.loc['ww','Code_Figure'] == '78':
                df.loc['ww','Decoded_Information']='Isolated star-like snow crystals (with or without fog)'
            elif df.loc['ww','Code_Figure'] == '79':
                df.loc['ww','Decoded_Information']='Ice pellets'
            elif df.loc['ww','Code_Figure'] == '80':
                df.loc['ww','Decoded_Information']='Rain shower(s), slight'
            elif df.loc['ww','Code_Figure'] == '81':
                df.loc['ww','Decoded_Information']='Rain shower(s), moderate or heavy'
            elif df.loc['ww','Code_Figure'] == '82':
                df.loc['ww','Decoded_Information']='Rain shower(s), violent'
            elif df.loc['ww','Code_Figure'] == '83':
                df.loc['ww','Decoded_Information']='Shower(s) of rain and snow mixed, slight'
            elif df.loc['ww','Code_Figure'] == '84':
                df.loc['ww','Decoded_Information']='Shower(s) of rain and snow mixed, moderate or heavy'
            elif df.loc['ww','Code_Figure'] == '85':
                df.loc['ww','Decoded_Information']='Snow shower(s), slight'
            elif df.loc['ww','Code_Figure'] == '86':
                df.loc['ww','Decoded_Information']='Snow shower(s), moderate or heavy'
            elif df.loc['ww','Code_Figure'] == '87':
                df.loc['ww','Decoded_Information']='Shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed - slight'
            elif df.loc['ww','Code_Figure'] == '88':
                df.loc['ww','Decoded_Information']='Shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed - moderate or heavy'
            elif df.loc['ww','Code_Figure'] == '89':
                df.loc['ww','Decoded_Information']='Shower(s) of hail, with or without rain or rainand snow mixed, not associated with thunder - slight'
            elif df.loc['ww','Code_Figure'] == '90':
                df.loc['ww','Decoded_Information']='Shower(s) of hail, with or without rain or rainand snow mixed, not associated with thunder - moderate or heavy'
            elif df.loc['ww','Code_Figure'] == '91':
                df.loc['ww','Decoded_Information']='Slight rain at time of observation (Thunderstorm during the preceding hour but not at time of observation)'
            elif df.loc['ww','Code_Figure'] == '92':
                df.loc['ww','Decoded_Information']='Moderate or heavy rain at time of observation (Thunderstorm during the preceding hour but not at time of observation)'
            elif df.loc['ww','Code_Figure'] == '93':
                df.loc['ww','Decoded_Information']='Slight snow, or rain and snow mixed or hail at time of observation (Thunderstorm during the preceding hour but not at time of observation)'
            elif df.loc['ww','Code_Figure'] == '94':
                df.loc['ww','Decoded_Information']='Moderate or heavy snow, or rain and snow mixed or hail at time of observation (Thunderstorm during the preceding hour but not at time of observation)'
            elif df.loc['ww','Code_Figure'] == '95':
                df.loc['ww','Decoded_Information']='Thunderstorm, slight or moderate, without hail, but with rain and/or snow at time of observation (Thunderstorm at time of observation)'
            elif df.loc['ww','Code_Figure'] == '96':
                df.loc['ww','Decoded_Information']='Thunderstorm, slight or moderate, with hail at time of observation (Thunderstorm at time of observation)'
            elif df.loc['ww','Code_Figure'] == '97':
                df.loc['ww','Decoded_Information']='Thunderstorm, heavy, without hail, but with rain and/or snow at time of observation (Thunderstorm at time of observation)'
            elif df.loc['ww','Code_Figure'] == '98':
                df.loc['ww','Decoded_Information']='Thunderstorm combined with duststorm or sandstorm at time of observation (Thunderstorm at time of observation)'
            elif df.loc['ww','Code_Figure'] == '99':
                df.loc['ww','Decoded_Information']='Thunderstorm, heavy, with hail at time of observation (Thunderstorm at time of observation)'
            #W1 (Code table 4561):
            df.loc['W1','Code_Figure']=group[3]
            if df.loc['W1','Code_Figure'] == '0':
                df.loc['W1','Decoded_Information']='Cloud covering 1/2 or less of the sky throughout the appropriate period'
            if df.loc['W1','Code_Figure'] == '1':
                df.loc['W1','Decoded_Information']='Cloud covering more than 1/2 of the sky during part of the appropriate period and covering 1/2 or less during part of the period'
            if df.loc['W1','Code_Figure'] == '2':
                df.loc['W1','Decoded_Information']='Cloud covering more than 1/2 of the sky throughout the appropriate period'
            if df.loc['W1','Code_Figure'] == '3':
                df.loc['W1','Decoded_Information']='Sandstorm, duststorm or blowing snow'
            if df.loc['W1','Code_Figure'] == '4':
                df.loc['W1','Decoded_Information']='Fog or ice fog or thick haze'
            if df.loc['W1','Code_Figure'] == '5':
                df.loc['W1','Decoded_Information']='Drizzle'
            if df.loc['W1','Code_Figure'] == '6':
                df.loc['W1','Decoded_Information']='Rain'
            if df.loc['W1','Code_Figure'] == '7':
                df.loc['W1','Decoded_Information']='Snow, or rain and snow mixed'
            if df.loc['W1','Code_Figure'] == '8':
                df.loc['W1','Decoded_Information']='Shower(s)'
            if df.loc['W1','Code_Figure'] == '9':
                df.loc['W1','Decoded_Information']='Thunderstorm(s) with or without precipitation'
            #W2 (Code table 4561):
            df.loc['W2','Code_Figure']=group[4]
            if df.loc['W2','Code_Figure'] == '0':
                df.loc['W2','Decoded_Information']='Cloud covering 1/2 or less of the sky throughout the appropriate period'
            if df.loc['W2','Code_Figure'] == '1':
                df.loc['W2','Decoded_Information']='Cloud covering more than 1/2 of the sky during part of the appropriate period and covering 1/2 or less during part of the period'
            if df.loc['W2','Code_Figure'] == '2':
                df.loc['W2','Decoded_Information']='Cloud covering more than 1/2 of the sky throughout the appropriate period'
            if df.loc['W2','Code_Figure'] == '3':
                df.loc['W2','Decoded_Information']='Sandstorm, duststorm or blowing snow'
            if df.loc['W2','Code_Figure'] == '4':
                df.loc['W2','Decoded_Information']='Fog or ice fog or thick haze'
            if df.loc['W2','Code_Figure'] == '5':
                df.loc['W2','Decoded_Information']='Drizzle'
            if df.loc['W2','Code_Figure'] == '6':
                df.loc['W2','Decoded_Information']='Rain'
            if df.loc['W2','Code_Figure'] == '7':
                df.loc['W2','Decoded_Information']='Snow, or rain and snow mixed'
            if df.loc['W2','Code_Figure'] == '8':
                df.loc['W2','Decoded_Information']='Shower(s)'
            if df.loc['W2','Code_Figure'] == '9':
                df.loc['W2','Decoded_Information']='Thunderstorm(s) with or without precipitation'
                
        #8NhCLCMCH
        elif group[0] == '8':
            #Nh (Code table 2700):
            df.loc['Nh','Code_Figure']=group[1]
            if df.loc['Nh','Code_Figure'] == '0':
                df.loc['Nh','Decoded_Information']='0'
            elif df.loc['Nh','Code_Figure'] == '1':
                df.loc['Nh','Decoded_Information']='1 okta or less, but not zero'
            elif df.loc['Nh','Code_Figure'] == '2':
                df.loc['Nh','Decoded_Information']='2 oktas'
            elif df.loc['Nh','Code_Figure'] == '3':
                df.loc['Nh','Decoded_Information']='3 oktas'
            elif df.loc['Nh','Code_Figure'] == '4':
                df.loc['Nh','Decoded_Information']='4 oktas'
            elif df.loc['Nh','Code_Figure'] == '5':
                df.loc['Nh','Decoded_Information']='5 oktas'
            elif df.loc['Nh','Code_Figure'] == '6':
                df.loc['Nh','Decoded_Information']='6 oktas'
            elif df.loc['Nh','Code_Figure'] == '7':
                df.loc['Nh','Decoded_Information']='7 oktas or more, but not 8 oktas'
            elif df.loc['Nh','Code_Figure'] == '8':
                df.loc['Nh','Decoded_Information']='8 oktas'
            elif df.loc['Nh','Code_Figure'] == '9':
                df.loc['Nh','Decoded_Information']='Sky obscured by fog and/or other meteorological phenomena'
            elif df.loc['Nh','Code_Figure'] == '/':
                df.loc['Nh','Decoded_Information']='Cloud cover is indiscernible for reasons other than fog or other meteorological phenomena, or observation is not made'
            #CL (Code table 0513):
            df.loc['CL','Code_Figure']=group[2]
            if df.loc['CL','Code_Figure'] == '0':
                df.loc['CL','Decoded_Information']='No clouds of type CL'
            elif df.loc['CL','Code_Figure'] == '1':
                df.loc['CL','Decoded_Information']='Cumulus with little vertical extent and seemingly flattened, or ragged cumulus other than of bad weather, or both'
            elif df.loc['CL','Code_Figure'] == '2':
                df.loc['CL','Decoded_Information']='Cumulus of moderate or strong vertical extent, generally with protuberances in the form of domes or towers, either accompanied or not by other cumulus or by stratocumulus, all having their bases at the same level'
            elif df.loc['CL','Code_Figure'] == '3':
                df.loc['CL','Decoded_Information']='Cumulonimbus the summits of which, at least partially, lack sharp outlines, but are neither clearly fibrous (cirriform) nor in the form of an anvil; cumulus, stratocumulus or Stratus may also be present'
            elif df.loc['CL','Code_Figure'] == '4':
                df.loc['CL','Decoded_Information']='Stratocumulus formed by the spreading out of cumulus; cumulus may also be present'
            elif df.loc['CL','Code_Figure'] == '5':
                df.loc['CL','Decoded_Information']='Stratocumulus not resulting from the spreading out of cumulus'
            elif df.loc['CL','Code_Figure'] == '6':
                df.loc['CL','Decoded_Information']='Stratus in a more or less continuous sheet or layer, or in ragged shreds, or both, but no Stratus fractus of bad weather'
            elif df.loc['CL','Code_Figure'] == '7':
                df.loc['CL','Decoded_Information']='Stratus fractus of bad weather or cumulus fractus of bad weather, or both (pannus), usually below altostratus or nimbostratus'
            elif df.loc['CL','Code_Figure'] == '8':
                df.loc['CL','Decoded_Information']='Cumulus and stratocumulus other than that formed from the spreading out of cumulus; the base of the cumulus is at a different level from that of the stratocumulus'
            elif df.loc['CL','Code_Figure'] == '9':
                df.loc['CL','Decoded_Information']='Cumulonimbus, the upper part of which is clearly fibrous (cirriform), often in the form of an anvil; either accompanied or not by cumulonimbus without anvil or fibrous upper part, by cumulus, stratocumulus, stratus or pannus'
            elif df.loc['CL','Code_Figure'] == '/':
                df.loc['CL','Decoded_Information']='Stratocumulus, stratus, cumulus and cumulonimbus invisible owing to darkness, fog, blowing dust or sand, or other similar phenomena'
            #CM (Code table 0515):
            df.loc['CM','Code_Figure']=group[3]
            if df.loc['CM','Code_Figure'] == '0':
                df.loc['CM','Decoded_Information']='No clouds of type CM'
            elif df.loc['CM','Code_Figure'] == '1':
                df.loc['CM','Decoded_Information']='Altostratus, the greater part of which is semi-transparent; through this part the sun or moon may be weakly visible, as through ground glass'
            elif df.loc['CM','Code_Figure'] == '2':
                df.loc['CM','Decoded_Information']='Altostratus, the greater part of which is sufficiently dense to hide the sun or moon, or nimbostratus'
            elif df.loc['CM','Code_Figure'] == '3':
                df.loc['CM','Decoded_Information']='Altocumulus, the greater part of which is semi-transparent; the various elements of the cloud change only slowly and are all at a single level'
            elif df.loc['CM','Code_Figure'] == '4':
                df.loc['CM','Decoded_Information']='Patches (often in the form of almonds or fish) of altocumulus, the greater part of which is semi-transparent; the clouds occur at one or more levels and the elements are continually changing in appearance'
            elif df.loc['CM','Code_Figure'] == '5':
                df.loc['CM','Decoded_Information']='Semi-transparent altocumulus in bands, or altocumulus, in one or more fairly continuous layer (semi-transparent or opaque), progressively invading the sky; these altocumulus clouds generally thicken as a whole'
            elif df.loc['CM','Code_Figure'] == '6':
                df.loc['CM','Decoded_Information']='Altocumulus resulting from the spreading out of cumulus (or cumulonimbus)'
            elif df.loc['CM','Code_Figure'] == '7':
                df.loc['CM','Decoded_Information']='Altocumulus in two or more layers, usually opaque in places, and not progressively invading the sky; or opaque layer of altocumulus, not progressively invading the sky; or altocumulus together with altostratus or nimbostratus'
            elif df.loc['CM','Code_Figure'] == '8':
                df.loc['CM','Decoded_Information']='Altocumulus with sproutings in the form of small towers or battlements, or altocumulus having the appearance of cumuliform tufts'
            elif df.loc['CM','Code_Figure'] == '9':
                df.loc['CM','Decoded_Information']='Altocumulus of a chaotic sky, generally at several levels'
            elif df.loc['CM','Code_Figure'] == '/':
                df.loc['CM','Decoded_Information']='Altocumulus, altostratus and nimbostratus invisible owing to darkness, fog, blowing dust or sand, or other similar phenomena, or more often because of the presence of a continuous layer of lower clouds'
            #CH (Code table 0509):
            df.loc['CH','Code_Figure']=group[4]
            if df.loc['CH','Code_Figure'] == '0':
                df.loc['CH','Decoded_Information']='No clouds of type CH'
            elif df.loc['CH','Code_Figure'] == '1':
                df.loc['CH','Decoded_Information']='Cirrus in the form of filaments, strands or hooks, not progressively invading the sky'
            elif df.loc['CH','Code_Figure'] == '2':
                df.loc['CH','Decoded_Information']='Dense cirrus, in patches or entangled sheaves, which usually do not increase and sometimes seem to be the remains of the upper part of a cumulonimbus; or cirrus with sproutings in the form of small turrets or battlements, or cirrus having the appearance of cumuliform tufts'
            elif df.loc['CH','Code_Figure'] == '3':
                df.loc['CH','Decoded_Information']='Dense cirrus, often in the form of an anvil, being the remains of the upper parts of cumulonimbus'
            elif df.loc['CH','Code_Figure'] == '4':
                df.loc['CH','Decoded_Information']='Cirrus in the form of hooks or of filaments, or both, progressively invading the sky; they generally become denser as a whole'
            elif df.loc['CH','Code_Figure'] == '5':
                df.loc['CH','Decoded_Information']='Cirrus (often in bands converging towards one point or two opposite points of the horizon) and cirrostratus, or cirrostratus alone; in either case, they are progressively invading the sky, and generally growing denser as a whole, but the continuous veil does not reach 45 degrees above the horizon'
            elif df.loc['CH','Code_Figure'] == '6':
                df.loc['CH','Decoded_Information']='Cirrus (often in bands converging towards one point or two opposite points of the horizon) and cirrostratus, or cirrostratus alone; in either case, they are progressively invading the sky, and generally growing denser as a whole; the continuous veil extends more than 45 degrees above the horizon, without the sky being totally covered'
            elif df.loc['CH','Code_Figure'] == '7':
                df.loc['CH','Decoded_Information']='Veil of cirrostratus covering the celestial dome'
            elif df.loc['CH','Code_Figure'] == '8':
                df.loc['CH','Decoded_Information']='Cirrostratus not progressively invading the sky and not completely covering the celestial dome'
            elif df.loc['CH','Code_Figure'] == '9':
                df.loc['CH','Decoded_Information']='Cirrocumulus alone, or cirrocumulus accompanied by cirrus or cirrostratus, or both, but cirrocumulus is predominant'
            elif df.loc['CH','Code_Figure'] == '/':
                df.loc['CH','Decoded_Information']='Cirrus, cirrocumulus and cirrostratus invisible owing to darkness, fog, blowing dust or sand, or other similar phenomena, or more often because of the presence of a continuous layer of lower clouds'
                
        #9GGgg
        elif group[0] == '9':
            #GGgg:
            df.loc['GGgg','Code_Figure']=group[1:5]
            df.loc['GGgg','Decoded_Information']=pd.Timestamp(year=int(year),month=int(month),day=int(groups[2][0:2]),hour=int(group[1:3]),minute=int(group[3:5]))
            
    #---------- Section 2 ----------
    
    groups2=iter(groups[sec2:]) #List of groups in Section 2
    
    for group in groups2:
        
        #222Dsvs
        if group[0:3] == '222':
            #Ds (Code table 0700):
            df.loc['Ds','Code_Figure']=group[3]
            if df.loc['Ds','Code_Figure'] == '0':
                df.loc['Ds','Decoded_Information']='Stationary'
            elif df.loc['Ds','Code_Figure'] == '1':
                df.loc['Ds','Decoded_Information']='NE'
            elif df.loc['Ds','Code_Figure'] == '2':
                df.loc['Ds','Decoded_Information']='E'
            elif df.loc['Ds','Code_Figure'] == '3':
                df.loc['Ds','Decoded_Information']='SE'
            elif df.loc['Ds','Code_Figure'] == '4':
                df.loc['Ds','Decoded_Information']='S'
            elif df.loc['Ds','Code_Figure'] == '5':
                df.loc['Ds','Decoded_Information']='SW'
            elif df.loc['Ds','Code_Figure'] == '6':
                df.loc['Ds','Decoded_Information']='W'
            elif df.loc['Ds','Code_Figure'] == '7':
                df.loc['Ds','Decoded_Information']='NW'
            elif df.loc['Ds','Code_Figure'] == '8':
                df.loc['Ds','Decoded_Information']='N'
            elif df.loc['Ds','Code_Figure'] == '9':
                df.loc['Ds','Decoded_Information']='Unknown'
            elif df.loc['Ds','Code_Figure'] == '/':
                df.loc['Ds','Decoded_Information']='Displacement of ship not reported'
            #vs (Code table 4451):
            df.loc['vs','Code_Figure']=group[4]
            if df.loc['vs','Code_Figure'] == '0':
                df.loc['vs','Decoded_Information']='0 km/h'
            elif df.loc['vs','Code_Figure'] == '1':
                df.loc['vs','Decoded_Information']='1-10 km/h'
            elif df.loc['vs','Code_Figure'] == '2':
                df.loc['vs','Decoded_Information']='11-19 km/h'
            elif df.loc['vs','Code_Figure'] == '3':
                df.loc['vs','Decoded_Information']='20-28 km/h'
            elif df.loc['vs','Code_Figure'] == '4':
                df.loc['vs','Decoded_Information']='29-37 km/h'
            elif df.loc['vs','Code_Figure'] == '5':
                df.loc['vs','Decoded_Information']='38-47 km/h'
            elif df.loc['vs','Code_Figure'] == '6':
                df.loc['vs','Decoded_Information']='48-56 km/h'
            elif df.loc['vs','Code_Figure'] == '7':
                df.loc['vs','Decoded_Information']='57-65 km/h'
            elif df.loc['vs','Code_Figure'] == '8':
                df.loc['vs','Decoded_Information']='66-75 km/h'
            elif df.loc['vs','Code_Figure'] == '9':
                df.loc['vs','Decoded_Information']='Over 75 km/h'
            elif df.loc['vs','Code_Figure'] == '/':
                df.loc['vs','Decoded_Information']='Not reported'
            
        #0ssTwTwTw
        elif group[0] == '0':
            #ss (Code table 3850):
            df.loc['ss','Code_Figure']=group[1]
            if df.loc['ss','Code_Figure'] == '0':
                df.loc['ss','Decoded_Information']='Positive or zero; Intake'
            elif df.loc['ss','Code_Figure'] == '1':
                df.loc['ss','Decoded_Information']='Negative; Intake'
            elif df.loc['ss','Code_Figure'] == '2':
                df.loc['ss','Decoded_Information']='Positive or zero; Bucket'
            elif df.loc['ss','Code_Figure'] == '3':
                df.loc['ss','Decoded_Information']='Negative; Bucket'
            elif df.loc['ss','Code_Figure'] == '4':
                df.loc['ss','Decoded_Information']='Positive or zero; Hull contact sensor'
            elif df.loc['ss','Code_Figure'] == '5':
                df.loc['ss','Decoded_Information']='Negative; Hull contact sensor'
            elif df.loc['ss','Code_Figure'] == '6':
                df.loc['ss','Decoded_Information']='Positive or zero; Other'
            elif df.loc['ss','Code_Figure'] == '7':
                df.loc['ss','Decoded_Information']='Negative; Other'
            #TwTwTw:
            df.loc['TwTwTw','Code_Figure']=group[2:5]
            if df.loc['ss','Code_Figure'] == '1' or df.loc['ss','Code_Figure'] == '3' or df.loc['ss','Code_Figure'] == '5' or df.loc['ss','Code_Figure'] == '7':
                df.loc['TwTwTw','Decoded_Information']=-1*int(df.loc['TwTwTw','Code_Figure'])*0.1 
            else:
                df.loc['TwTwTw','Decoded_Information']=int(df.loc['TwTwTw','Code_Figure'])*0.1 
                
        #2PwPwHwHw
        elif group[0] == '2':
            #PwPw:
            df.loc['PwPw','Code_Figure']=group[1:3]
            if group[1:5] == '0000':
                df.loc['PwPw','Decoded_Information']='Calm'
            elif df.loc['PwPw','Code_Figure'] == '99':
                df.loc['PwPw','Decoded_Information']='Confused sea'
            elif df.loc['PwPw','Code_Figure'] == '//':
                df.loc['PwPw','Decoded_Information']=np.nan
            else:
                df.loc['PwPw','Decoded_Information']=int(df.loc['PwPw','Code_Figure'])
            #HwHw:
            df.loc['HwHw','Code_Figure']=group[3:5]
            if group[1:5] == '0000':
                df.loc['HwHw','Decoded_Information']='Calm'
            elif df.loc['HwHw','Code_Figure'] == '//':
                df.loc['HwHw','Decoded_Information']=np.nan
            else:
                df.loc['HwHw','Decoded_Information']=int(df.loc['HwHw','Code_Figure'])*0.5
                
        #3dw1dw1dw2dw2
        elif group[0] == '3':
            #dw1dw1 (Code table 0877):
            df.loc['dw1dw1','Code_Figure']=group[1:3]
            if df.loc['dw1dw1','Code_Figure'] == '00':
                df.loc['dw1dw1','Decoded_Information']='Calm'
            elif df.loc['dw1dw1','Code_Figure'] == '99':
                df.loc['dw1dw1','Decoded_Information']='Variable'
            else:
                df.loc['dw1dw1','Decoded_Information']=int(df.loc['dw1dw1','Code_Figure'])*10
            #dw2dw2 (Code table 0877):
            df.loc['dw2dw2','Code_Figure']=group[3:5]
            if df.loc['dw2dw2','Code_Figure'] == '00':
                df.loc['dw2dw2','Decoded_Information']='Calm'
            elif df.loc['dw2dw2','Code_Figure'] == '99':
                df.loc['dw2dw2','Decoded_Information']='Variable'
            elif df.loc['dw2dw2','Code_Figure'] == '//':
                df.loc['dw2dw2','Decoded_Information']='Only one system of swell is observed'
            else:
                df.loc['dw2dw2','Decoded_Information']=int(df.loc['dw2dw2','Code_Figure'])*10
        
        #4Pw1Pw1Hw1Hw1
        elif group[0] == '4':
            #Pw1Pw1:
            df.loc['Pw1Pw1','Code_Figure']=group[1:3]
            if group[1:5] == '0000':
                df.loc['Pw1Pw1','Decoded_Information']='Calm'
            elif df.loc['Pw1Pw1','Code_Figure'] == '99':
                df.loc['Pw1Pw1','Decoded_Information']='Confused sea'
            elif df.loc['Pw1Pw1','Code_Figure'] == '//':
                df.loc['Pw1Pw1','Decoded_Information']=np.nan
            else:
                df.loc['Pw1Pw1','Decoded_Information']=int(df.loc['Pw1Pw1','Code_Figure'])
            #Hw1Hw1:
            df.loc['Hw1Hw1','Code_Figure']=group[3:5]
            if group[1:5] == '0000':
                df.loc['Hw1Hw1','Decoded_Information']='Calm'
            elif df.loc['Hw1Hw1','Code_Figure'] == '//':
                df.loc['Hw1Hw1','Decoded_Information']=np.nan
            else:
                df.loc['Hw1Hw1','Decoded_Information']=int(df.loc['Hw1Hw1','Code_Figure'])*0.5
                
        #5Pw2Pw2Hw2Hw2
        elif group[0] == '5':
            #Pw2Pw2:
            df.loc['Pw2Pw2','Code_Figure']=group[1:3]
            if group[1:5] == '0000':
                df.loc['Pw2Pw2','Decoded_Information']='Calm'
            elif df.loc['Pw2Pw2','Code_Figure'] == '99':
                df.loc['Pw2Pw2','Decoded_Information']='Confused sea'
            elif df.loc['Pw2Pw2','Code_Figure'] == '//':
                df.loc['Pw2Pw2','Decoded_Information']=np.nan
            else:
                df.loc['Pw2Pw2','Decoded_Information']=int(df.loc['Pw2Pw2','Code_Figure'])
            #Hw2Hw2:
            df.loc['Hw2Hw2','Code_Figure']=group[3:5]
            if group[1:5] == '0000':
                df.loc['Hw2Hw2','Decoded_Information']='Calm'
            elif df.loc['Hw2Hw2','Code_Figure'] == '//':
                df.loc['Hw2Hw2','Decoded_Information']=np.nan
            else:
                df.loc['Hw2Hw2','Decoded_Information']=int(df.loc['Hw2Hw2','Code_Figure'])*0.5
                
        #6IsEsEsRs
        elif group[0] == '6' and len(group) == 5:
            #Is (Code table 1751):
            df.loc['Is','Code_Figure']=group[1]
            if df.loc['Is','Code_Figure'] == '1':
                df.loc['Is','Decoded_Information']='Icing from ocean spray'
            elif df.loc['Is','Code_Figure'] == '2':
                df.loc['Is','Decoded_Information']='Icing from fog'
            elif df.loc['Is','Code_Figure'] == '3':
                df.loc['Is','Decoded_Information']='Icing from spray and fog'
            elif df.loc['Is','Code_Figure'] == '4':
                df.loc['Is','Decoded_Information']='Icing from rain'
            elif df.loc['Is','Code_Figure'] == '5':
                df.loc['Is','Decoded_Information']='Icing from spray and rain'
            #EsEs:
            df.loc['EsEs','Code_Figure']=group[2:4]
            df.loc['EsEs','Decoded_Information']=int(df.loc['EsEs','Code_Figure'])
            #Rs (Code table 3551):
            df.loc['Rs','Code_Figure']=group[4]
            if df.loc['Rs','Code_Figure'] == '0':
                df.loc['Rs','Decoded_Information']='Ice not building up'
            elif df.loc['Rs','Code_Figure'] == '1':
                df.loc['Rs','Decoded_Information']='Ice building up slowly'
            elif df.loc['Rs','Code_Figure'] == '2':
                df.loc['Rs','Decoded_Information']='Ice building up rapidly'
            elif df.loc['Rs','Code_Figure'] == '3':
                df.loc['Rs','Decoded_Information']='Ice melting or breaking up slowly'
            elif df.loc['Rs','Code_Figure'] == '4':
                df.loc['Rs','Decoded_Information']='Ice melting or breaking up rapidly'
                
        #8swTbTbTb
        elif group[0] == '8':
            #sw (Code table 3855):
            df.loc['sw','Code_Figure']=group[1]
            if df.loc['sw','Code_Figure'] == '0':
                df.loc['sw','Decoded_Information']='Positive or zero measured wet-bulb temperature'
            elif df.loc['sw','Code_Figure'] == '1':
                df.loc['sw','Decoded_Information']='Negative measured wet-bulb temperature'
            elif df.loc['sw','Code_Figure'] == '2':
                df.loc['sw','Decoded_Information']='Iced bulb measured wet-bulb temperature'
            elif df.loc['sw','Code_Figure'] == '5':
                df.loc['sw','Decoded_Information']='Positive or zero computed wet-bulb temperature'
            elif df.loc['sw','Code_Figure'] == '6':
                df.loc['sw','Decoded_Information']='Negative computed wet-bulb temperature'
            elif df.loc['sw','Code_Figure'] == '7':
                df.loc['sw','Decoded_Information']='Iced bulb computed wet-bulb temperature'
            #TbTbTb:
            df.loc['TbTbTb','Code_Figure']=group[2:5]
            if df.loc['sw','Code_Figure'] == '1' or df.loc['sw','Code_Figure'] == '2' or df.loc['sw','Code_Figure'] == '6' or df.loc['sw','Code_Figure'] == '7':
                df.loc['TbTbTb','Decoded_Information']=-1*int(df.loc['TbTbTb','Code_Figure'])*0.1 
            else:
                df.loc['TbTbTb','Decoded_Information']=int(df.loc['TbTbTb','Code_Figure'])*0.1 
        
        #ICE ciSibiDizi        
        elif group == 'ICE':
            ICE_group=next(groups2) #2nd part of ICE group
            if len(ICE_group) != 5: #if 2nd part of ICE group don't exist
                break
            #ci (Code table 0639):
            df.loc['ci','Code_Figure']=ICE_group[0]
            if df.loc['ci','Code_Figure'] == '0':
                df.loc['ci','Decoded_Information']='No sea ice in sight'
            elif df.loc['ci','Code_Figure'] == '1':
                df.loc['ci','Decoded_Information']='Ship in open lead more than 1.0 nautical mile wide, or ship in fast ice with boundary beyond limit of visibility'
            elif df.loc['ci','Code_Figure'] == '2':
                df.loc['ci','Decoded_Information']='Sea ice present in concentrations less than 3/10, open water or very open pack ice; Sea ice concentration is uniform in the observation area; Ship in ice or within 0.5 nautical mile of ice edge'
            elif df.loc['ci','Code_Figure'] == '3':
                df.loc['ci','Decoded_Information']='4/10 to 6/10, open pack ice; Sea ice concentration is uniform in the observation area; Ship in ice or within 0.5 nautical mile of ice edge'
            elif df.loc['ci','Code_Figure'] == '4':
                df.loc['ci','Decoded_Information']='7/10 to 8/10, close pack ice; Sea ice concentration is uniform in the observation area; Ship in ice or within 0.5 nautical mile of ice edge'
            elif df.loc['ci','Code_Figure'] == '5':
                df.loc['ci','Decoded_Information']='9/10 or more, but not 10/10, very close pack ice; Sea ice concentration is uniform in the observation area; Ship in ice or within 0.5 nautical mile of ice edge'
            elif df.loc['ci','Code_Figure'] == '6':
                df.loc['ci','Decoded_Information']='Strips and patches of pack ice with open water between; Sea ice concentration is not uniform in the observation area; Ship in ice or within 0.5 nautical mile of ice edge'
            elif df.loc['ci','Code_Figure'] == '7':
                df.loc['ci','Decoded_Information']='Strips and patches of close or very close pack ice with areas of lesser concentration between; Sea ice concentration is not uniform in the observation area; Ship in ice or within 0.5 nautical mile of ice edge'
            elif df.loc['ci','Code_Figure'] == '8':
                df.loc['ci','Decoded_Information']='Fast ice with open water, very open or open pack ice to seaward of the ice boundary; Sea ice concentration is not uniform in the observation area; Ship in ice or within 0.5 nautical mile of ice edge'
            elif df.loc['ci','Code_Figure'] == '9':
                df.loc['ci','Decoded_Information']='Fast ice with close or very close pack ice to seaward of the ice boundary; Sea ice concentration is not uniform in the observation area; Ship in ice or within 0.5 nautical mile of ice edge'
            elif df.loc['ci','Code_Figure'] == '/':
                df.loc['ci','Decoded_Information']='Unable to report, because of darkness, lack of visibility, or because ship is more than 0.5 nautical mile away from ice edge'
            #Si (Code table 3739):
            df.loc['Si','Code_Figure']=ICE_group[1]
            if df.loc['Si','Code_Figure'] == '0':
                df.loc['Si','Decoded_Information']='New ice only (frazil ice, grease ice, slush, shuga)'
            elif df.loc['Si','Code_Figure'] == '1':
                df.loc['Si','Decoded_Information']='Nilas or ice rind, less than 10 cm thick'
            elif df.loc['Si','Code_Figure'] == '2':
                df.loc['Si','Decoded_Information']='Young ice (grey ice, grey-white ice), 10-30 cm thick'
            elif df.loc['Si','Code_Figure'] == '3':
                df.loc['Si','Decoded_Information']='Predominantly new and/or young ice with some first-year ice'
            elif df.loc['Si','Code_Figure'] == '4':
                df.loc['Si','Decoded_Information']='Predominantly thin first-year ice with some new and/or young ice'
            elif df.loc['Si','Code_Figure'] == '5':
                df.loc['Si','Decoded_Information']='All thin first-year ice (30-70 cm thick)'
            elif df.loc['Si','Code_Figure'] == '6':
                df.loc['Si','Decoded_Information']='Predominantly medium first-year ice (70-120 cm thick) and thick first-year ice (>120 cm thick) with some thinner (younger) first-year ice'
            elif df.loc['Si','Code_Figure'] == '7':
                df.loc['Si','Decoded_Information']='All medium and thick first-year ice'
            elif df.loc['Si','Code_Figure'] == '8':
                df.loc['Si','Decoded_Information']='Predominantly medium and thick first-year ice with some old ice (usually more than 2 metres thick)'
            elif df.loc['Si','Code_Figure'] == '9':
                df.loc['Si','Decoded_Information']='Predominantly old ice'
            elif df.loc['Si','Code_Figure'] == '/':
                df.loc['Si','Decoded_Information']='Unable to report, because of darkness, lack of visibility or because only ice of land origin is visible or because ship is more than 0.5 nautical mile away from ice edge'
            #bi (Code table 0439):
            df.loc['bi','Code_Figure']=ICE_group[2]
            if df.loc['bi','Code_Figure'] == '0':
                df.loc['bi','Decoded_Information']='No ice of land origin'
            elif df.loc['bi','Code_Figure'] == '1':
                df.loc['bi','Decoded_Information']='1-5 icebergs, no growlers or bergy bits'
            elif df.loc['bi','Code_Figure'] == '2':
                df.loc['bi','Decoded_Information']='6-10 icebergs, no growlers or bergy bits'
            elif df.loc['bi','Code_Figure'] == '3':
                df.loc['bi','Decoded_Information']='11-20 icebergs, no growlers or bergy bits'
            elif df.loc['bi','Code_Figure'] == '4':
                df.loc['bi','Decoded_Information']='Up to and including 10 growlers and bergy bits - no icebergs'
            elif df.loc['bi','Code_Figure'] == '5':
                df.loc['bi','Decoded_Information']='More than 10 growlers and bergy bits - no icebergs'
            elif df.loc['bi','Code_Figure'] == '6':
                df.loc['bi','Decoded_Information']='1-5 icebergs, with growlers and bergy bits'
            elif df.loc['bi','Code_Figure'] == '7':
                df.loc['bi','Decoded_Information']='6-10 icebergs, with growlers and bergy bits'
            elif df.loc['bi','Code_Figure'] == '8':
                df.loc['bi','Decoded_Information']='11-20 icebergs, with growlers and bergy bits'
            elif df.loc['bi','Code_Figure'] == '9':
                df.loc['bi','Decoded_Information']='More than 20 icebergs, with growlers and bergy bits - a major hazard to navigation'
            elif df.loc['bi','Code_Figure'] == '/':
                df.loc['bi','Decoded_Information']='Unable to report, because of darkness, lack of visibility or because only sea ice is visible'
            #Di (Code table 0739):
            df.loc['Di','Code_Figure']=ICE_group[3]
            if df.loc['Di','Code_Figure'] == '0':
                df.loc['Di','Decoded_Information']='Ship in shore or flaw lead'
            elif df.loc['Di','Code_Figure'] == '1':
                df.loc['Di','Decoded_Information']='Principal ice edge towards NE'
            elif df.loc['Di','Code_Figure'] == '2':
                df.loc['Di','Decoded_Information']='Principal ice edge towards E'
            elif df.loc['Di','Code_Figure'] == '3':
                df.loc['Di','Decoded_Information']='Principal ice edge towards SE'
            elif df.loc['Di','Code_Figure'] == '4':
                df.loc['Di','Decoded_Information']='Principal ice edge towards S'
            elif df.loc['Di','Code_Figure'] == '5':
                df.loc['Di','Decoded_Information']='Principal ice edge towards SW'
            elif df.loc['Di','Code_Figure'] == '6':
                df.loc['Di','Decoded_Information']='Principal ice edge towards W'
            elif df.loc['Di','Code_Figure'] == '7':
                df.loc['Di','Decoded_Information']='Principal ice edge towards NW'
            elif df.loc['Di','Code_Figure'] == '8':
                df.loc['Di','Decoded_Information']='Principal ice edge towards N'
            elif df.loc['Di','Code_Figure'] == '9':
                df.loc['Di','Decoded_Information']='Not determined (ship in ice)'
            elif df.loc['Di','Code_Figure'] == '/':
                df.loc['Di','Decoded_Information']='Unable to report, because of darkness, lack of visibility or because only ice of land origin is visible'
            #zi (Code table 5239):
            df.loc['zi','Code_Figure']=ICE_group[4]
            if df.loc['zi','Code_Figure'] == '0':
                df.loc['zi','Decoded_Information']='Ship in open water with floating ice in sight'
            elif df.loc['zi','Code_Figure'] == '1':
                df.loc['zi','Decoded_Information']='Ship in easily penetrable ice; conditions improving (Ship in ice)'
            elif df.loc['zi','Code_Figure'] == '2':
                df.loc['zi','Decoded_Information']='Ship in easily penetrable ice; conditions not changing (Ship in ice)'
            elif df.loc['zi','Code_Figure'] == '3':
                df.loc['zi','Decoded_Information']='Ship in easily penetrable ice; conditions worsening (Ship in ice)'
            elif df.loc['zi','Code_Figure'] == '4':
                df.loc['zi','Decoded_Information']='Ship in ice difficult to penetrate; conditions improving (Ship in ice)'
            elif df.loc['zi','Code_Figure'] == '5':
                df.loc['zi','Decoded_Information']='Ship in ice difficult to penetrate; conditions not changing (Ship in ice)'
            elif df.loc['zi','Code_Figure'] == '6':
                df.loc['zi','Decoded_Information']='Ice forming and floes freezing together (Ship in ice difficult to penetrate and conditions worsening)'
            elif df.loc['zi','Code_Figure'] == '7':
                df.loc['zi','Decoded_Information']='Ice under slight pressure (Ship in ice difficult to penetrate and conditions worsening)'
            elif df.loc['zi','Code_Figure'] == '8':
                df.loc['zi','Decoded_Information']='Ice under moderate or severe pressure (Ship in ice difficult to penetrate and conditions worsening)'
            elif df.loc['zi','Code_Figure'] == '9':
                df.loc['zi','Decoded_Information']='Ship beset (Ship in ice difficult to penetrate and conditions worsening)'
            elif df.loc['zi','Code_Figure'] == '/':
                df.loc['zi','Decoded_Information']='Unable to report, because of darkness or lack of visibility'            
            break        
    
    #Sections 3, 4 and 5 not included in ACE Telegrams
    
    #Significant figures of floating point values:
    for i in df.index:
        if type(df.loc[i,'Decoded_Information']) is float:
            df.loc[i,'Decoded_Information']='{:.1f}'.format(df.loc[i,'Decoded_Information'])    
    
    #Save decoded telegram to ascii tab-separate .txt:
   # df.to_csv(output_path + 'ACE_telegram_decoded_' + df.loc['YYGG','Decoded_Information'].strftime('%Y') + '_' +
   #           df.loc['YYGG','Decoded_Information'].strftime('%m') + '_' + df.loc['YYGG','Decoded_Information'].strftime('%d')
   #           + '_' + df.loc['YYGG','Decoded_Information'].strftime('%H') + 'h.txt',
   #           sep='\t', index_label='Symbolic_Letters', encoding='ascii', na_rep='nan', date_format='%Y-%m-%dT%H:%M:%S+00:00')
    
    #Save decoded telegram to ascii comma-separated .csv:
    df.to_csv(output_path + 'ACE_telegram_decoded_' + df.loc['YYGG','Decoded_Information'].strftime('%Y') + '_' +
              df.loc['YYGG','Decoded_Information'].strftime('%m') + '_' + df.loc['YYGG','Decoded_Information'].strftime('%d')
              + '_' + df.loc['YYGG','Decoded_Information'].strftime('%H') + 'h.csv',
              sep=',', index_label='Symbolic_Letters', encoding='ascii', na_rep='nan', date_format='%Y-%m-%dT%H:%M:%S+00:00')
        
    return df

def main():

    from glob import glob

    # Specify input and output paths:
    raw_data_directory = '../../data_raw/Telegrams/'
    output_path='../Telegrams_decoded/'


    # Names of all original telegram files:
    raw_file_list = sorted(glob(raw_data_directory + '*'))

    # Call decoding function for each file:

    for file in raw_file_list:
        print("Processing ", file)
        df = ACE_telegram_decoder(file, output_path)

if __name__ == '__main__':
    main()
