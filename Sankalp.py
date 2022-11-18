import streamlit as st
import sqlite3
import numpy as np

conn = sqlite3.connect('RSS_Thane_Sankalp_2022.db')
c = conn.cursor()
c.execute('SELECT Nagar_Code,Nagar_Name_Unicode FROM Nagar_Master order by Nagar_Code')
Nagar=c.fetchall()
# Nagar1 = ["Select Nagar"]+[row[1] for row in Nagar]
Nagar1 = [row[1] for row in Nagar]
Nagar2 = [row[0] for row in Nagar]



num1=[1,2,3,4]
num2=[5,6,7,8]
num3=[9,10,11,12]
num4=[13,14,15,16]
save_shakha=""
save_milan = ""
Text_Key=["" for x in range(10)]

st.header("राष्ट्रीय स्वयंसेवक संघ, ठाणे ")
st.subheader("संकल्प २०२२-२३ ")

def Milan_Karykarta1_callback():
    
    # if(Karykarta1.isnumeric()):
    #     st.error("Please Enter Valid Name !")
    st.write(st.session_state.get('row_index',0))
    # st.text(st.session_state.mytext)


def Load_ShakhaDetails(a,i):

    Up_Nagar19=np.arange(a*10*i+1,a*10*i+5)
    Vasti_No=np.arange(a*10*i+1,a*10*i+15)
    # st.write(Up_Nagar19)
    # my_string="[ "+str(i)+" ]  "+item[3]+" ( "+item[4]+" ) "
    # st.write(my_string) 
    
    Units_12 = st.selectbox("",Sankalp_Units_12 )
    Units_121=Units_12.split("(")[0]

    query="select * from sankalp_unit left join vasti_master on sankalp_unit.vasti_code=vasti_master.vasti_code where trim(Unit_Name)=trim('"+Units_121+"')"
    # st.write(query)
    # st.write(Units_121)
  
    c.execute(query)
    Units_Info=c.fetchall()



    Sankalp_Unit_Upngar = [row[23] for row in Units_Info]
    Sankalp_Unit_Vasti = [row[20] for row in Units_Info]

    

    # st.write(Sankalp_Unit_Upngar, "-", Sankalp_Unit_Vasti)

    if (Sankalp_Unit_Upngar[0]) is not None:
        Select_Unit_Upngar = Up_Nagar11.index(Sankalp_Unit_Upngar[0])
        Up_Nagar1=st.selectbox("उप-नगर",options=Up_Nagar11, index=Select_Unit_Upngar, key=Up_Nagar19)
    else :
        Up_Nagar1=st.selectbox("उप-नगर",options=Up_Nagar11,  key=Up_Nagar19)
    
    
    
    
    query="select * from Vasti_Master where upngar_code=(select upngar_code from upnagar_master where upngar_name_unicode='"+Up_Nagar1+"')"
    # st.write(query)
    c.execute(query)
    Vasti11=c.fetchall()
    Vasti_No1 = ["Select Vasti"]+[row[3] for row in Vasti11]
    

    if(Sankalp_Unit_Vasti[0] ) is not None  and Sankalp_Unit_Vasti[0] in Vasti_No1:
        Select_Unit_Vasti = Vasti_No1.index(Sankalp_Unit_Vasti[0])
        Vasti1=st.selectbox("वस्ती",options=Vasti_No1, index=Select_Unit_Vasti, key=Vasti_No)
    else :
        Vasti1=st.selectbox("वस्ती",options=Vasti_No1, key=Vasti_No)

    SU_K1= [row[11] for row in Units_Info]
    SU_M1= [row[12] for row in Units_Info]
    SU_K2= [row[13] for row in Units_Info]
    SU_M2= [row[14] for row in Units_Info]
    
    # st.write(SU_K1,SU_M1,SU_K2,SU_M2)
    
    Karykarta1=st.text_input("शाखा कार्यवाह",value=SU_K1[0],key=(i*10+1))
    Mobile1=st.text_input("Mobile1",value=SU_M1[0],key=(i*10+2))
    Karykarta2=st.text_input("शाखा मु.शिक्षक ",value=SU_K2[0],key=(i*10+3))
    Mobile2=st.text_input("Mobile2",value=SU_M2[0],key=(i*10+4))
    save_shakha=st.button("Save",key=1)

    
    if save_shakha:
        if Vasti1 == 'Select Vasti':
            # update_vasti_code=null
            query = "update Sankalp_Unit set Vasti_code=null where Unit_Name=trim('"+Units_121+"')"

        else :
            # update_vasti_code = Vasti1        
            query="update Sankalp_Unit set Vasti_code=(select vasti_code from vasti_master where Vasti_Name_Unicode='"+Vasti1+"') where Unit_Name=trim('"+Units_121+"')"
        
        # st.write(query)
        
        
        c.execute(query)
        conn.commit()

        query ="update Sankalp_Unit set "
        query+=" Karyakarta_1 = '" + Karykarta1 +"',"
        query+=" Mobile_1 = " + Mobile1 +","
        query+=" Karyakarta_2 = '" + Karykarta2 +"',"
        query+=" Mobile_2 = " + Mobile2 
        query+=" where Unit_Name=trim('"+Units_121+"')"
        # st.write(query)

        c.execute(query)
        conn.commit()
        st.success('Record updated successfully', icon="ℹ️")
        # st.write('Successfully updated')


def Load_MilanDetails(a,i):
    Unit_No = np.arange(a*100*i+1,a*100*i+20)
    Up_Nagar20=np.arange(a*100*i+1,a*100*i+5)
    Vasti_No=np.arange(a*100*i+1,a*100*i+15)
    # st.write(Up_Nagar19)
    # my_string="[ "+str(i)+" ]  "+item[3]+" ( "+item[4]+" ) "
    # st.write(my_string) 

    Units_11 = st.selectbox("",Sankalp_Units_11 )
    Units_111=Units_11.split("(")[0]

    query="select * from sankalp_unit left join vasti_master on sankalp_unit.vasti_code=vasti_master.vasti_code where trim(Unit_Name)=trim('"+Units_111+"')"
    # st.write(query)
    # st.write(Units_111)
    
    c.execute(query)
    Units_Info=c.fetchall()



    Sankalp_Unit_Upngar = [row[23] for row in Units_Info]
    Sankalp_Unit_Vasti = [row[20] for row in Units_Info]

    

    # st.write(Sankalp_Unit_Upngar, "-", Sankalp_Unit_Vasti)

    if (Sankalp_Unit_Upngar[0]) is not None :
        Select_Unit_Upngar = Up_Nagar11.index(Sankalp_Unit_Upngar[0])
        Up_Nagar1=st.selectbox("उप-नगर",options=Up_Nagar11, index=Select_Unit_Upngar, key=Up_Nagar20)
    else :
        Up_Nagar1=st.selectbox("उप-नगर",options=Up_Nagar11,  key=Up_Nagar20)
    
    
    
    
    query="select * from Vasti_Master where upngar_code=(select upngar_code from upnagar_master where upngar_name_unicode='"+Up_Nagar1+"')"
    #st.write(query)
    c.execute(query)
    Vasti11=c.fetchall()
    Vasti_No1 = ["Select Vasti"]+[row[3] for row in Vasti11]
    Vasti_No = [row[1] for row in Vasti11]

    if(Sankalp_Unit_Vasti[0] ) is not None and Sankalp_Unit_Vasti[0] in Vasti_No1:
        Select_Unit_Vasti = Vasti_No1.index(Sankalp_Unit_Vasti[0])
        Vasti1=st.selectbox("वस्ती",options=Vasti_No1, index=Select_Unit_Vasti, key=Vasti_No)
    else :
         Vasti1=st.selectbox("वस्ती",options=Vasti_No1, key=Vasti_No)

    SU_K1= [row[11] for row in Units_Info]
    SU_M1= [row[12] for row in Units_Info]
    SU_K2= [row[13] for row in Units_Info]
    SU_M2= [row[14] for row in Units_Info]

# on_change=Milan_Karykarta1_callback(),
    Text_Key[0] =str(i*100+1)
    # st.write(Text_Key[0])
    
    Karykarta1=st.text_input("मिलन प्रमुख",value=SU_K1[0],on_change=Milan_Karykarta1_callback(),key='Karykarta1')
    
    
    Mobile3=st.text_input("Mobile3",value=SU_M1[0], key=(i*100+2))
    if( Mobile3 is not None and not Mobile3.isnumeric() or len(Mobile3) < 10) :
        st.error("Please enter 10 digit Mobile Number !")
        
    Karykarta2=st.text_input("मिलन सह-प्रमुख ",value=SU_K2[0],key=(i*100+3))
    if(Karykarta2.isnumeric()):
        st.error("Please Enter Valid Name !")
    Mobile4=st.text_input("Mobile4",value=SU_M2[0],key=(i*100+4))
    if( not Mobile4.isnumeric() or len(Mobile4) < 10) :
        st.error("Please enter 10 digit Mobile Number !")

    save_milan=st.button("Save",key=2)

    if save_milan:
        if Vasti1 == 'Select Vasti':
            # update_vasti_code=null
            query = "update Sankalp_Unit set Vasti_code=null where Unit_Name=trim('"+Units_111+"')"

        else :
            # update_vasti_code = Vasti1        
            query="update Sankalp_Unit set Vasti_code=(select vasti_code from vasti_master where Vasti_Name_Unicode='"+Vasti1+"') where Unit_Name=trim('"+Units_111+"')"
        
        # st.write(query)
        c.execute(query)
        conn.commit()

        query ="update Sankalp_Unit set "
        query+=" Karyakarta_1 = '" + Karykarta1 +"',"
        query+=" Mobile_1 = " + Mobile3 +","
        query+=" Karyakarta_2 = '" + Karykarta2 +"',"
        query+=" Mobile_2 = " + Mobile4 
        query+=" where Unit_Name=trim('"+Units_111+"')"
        st.write(query)

        c.execute(query)
        conn.commit()
        st.success('Record updated successfully', icon="ℹ️")
        st.success('Record updated successfully', icon="ℹ️")


Selected_Nagar=st.selectbox("नगर",options=Nagar1, key=Nagar2)
query="select Upngar_Name_Unicode,Upngar_code from upnagar_master where nagar_code=(SELECT Nagar_Code FROM Nagar_Master where Nagar_Name_Unicode='"+Selected_Nagar+"')"
c.execute(query)
Upnagar11=c.fetchall()
Up_Nagar11 = ["Select Upngar"]+[row[0] for row in Upnagar11]
Up_Nagar12 = [row[1] for row in Upnagar11]

tab1, tab2 = st.tabs(["शाखा","साप्ताहिक मिलन"])
# with st.tabs("शाखा"):
with tab1:
    query="select * from sankalp_unit where nagar_code=(SELECT Nagar_Code FROM Nagar_Master where Nagar_Name_Unicode='"+Selected_Nagar+"')"
    query+="and sankalp_unit_type='शाखा' order by Age_Category"
    # st.write(query)
    c.execute(query)
    Sankalp_Units=c.fetchall()
    Sankalp_Units_12=[row[3]+" ( "+ row[4]+" ) " for row in Sankalp_Units]   
    
    # st.write(Sankalp_Units)
    i = 1
    # for item  in Sankalp_Units:
    Load_ShakhaDetails(Sankalp_Units[0][9],i)
        
    i+=1
    
    
    
    
   

# with st.tabs("मिलन"):
with tab2:
    query="select * from sankalp_unit where nagar_code=(SELECT Nagar_Code FROM Nagar_Master where Nagar_Name_Unicode='"+Selected_Nagar+"')"
    query+="and (sankalp_unit_type='साप्ताहिक मिलन' or sankalp_unit_type='IT मिलन') order by Age_Category"
    # st.write(query)
    c.execute(query)
    Sankalp_Units=c.fetchall()
    Sankalp_Units_11=[row[3]+" ( "+ row[4]+" ) " for row in Sankalp_Units]   

    # st.write(Sankalp_Units)
    i = 1
    # for item  in Sankalp_Units:
    Load_MilanDetails(Sankalp_Units[0][9],i)
    i+=1
    


