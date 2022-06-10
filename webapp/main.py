import streamlit as st
import pickle
import numpy as np
# Title

import pandas as pd
import matplotlib.pyplot as plt
#st.container()
st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    animation_symbol='❅'
st.markdown(f"""<div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>
                <div class="snowflake">{animation_symbol}</div>""",unsafe_allow_html=True)


x = 1





st.set_option('deprecation.showPyplotGlobalUse', False)


data=pd.read_csv("final_data.csv")
data=data.drop("Unnamed: 0",axis='columns')
data2=pd.read_csv('data2.csv')




st.title("Bangalore Property Price Prediction")
#bhk=0
# Header

st.balloons()
locality = st.selectbox('Enter a locality:',('Electronic City Phase II', 'Chikka Tirupathi', 'Uttarahalli',
       'Lingadheeranahalli', 'Kothanur', 'Whitefield', 'Old Airport Road',
       'Rajaji Nagar', 'Marathahalli', 'other', '7th Phase JP Nagar',
       'Gottigere', 'Sarjapur', 'Mysore Road', 'Bisuvanahalli',
       'Raja Rajeshwari Nagar', 'Kengeri', 'Binny Pete', 'Thanisandra',
       'Bellandur', 'Electronic City', 'Ramagondanahalli', 'Yelahanka',
       'Hebbal', 'Kasturi Nagar', 'Kanakpura Road',
       'Electronics City Phase 1', 'Kundalahalli', 'Chikkalasandra',
       'Murugeshpalya', 'Sarjapur  Road', 'HSR Layout', 'Doddathoguru',
       'KR Puram', 'Bhoganhalli', 'Lakshminarayana Pura', 'Begur Road',
       'Varthur', 'Bommanahalli', 'Gunjur', 'Devarachikkanahalli',
       'Hegde Nagar', 'Haralur Road', 'Hennur Road', 'Kothannur',
       'Kalena Agrahara', 'Kaval Byrasandra', 'ISRO Layout',
       'Garudachar Palya', 'EPIP Zone', 'Dasanapura', 'Kasavanhalli',
       'Sanjay nagar', 'Domlur', 'Sarjapura - Attibele Road',
       'Yeshwanthpur', 'Chandapura', 'Nagarbhavi', 'Devanahalli',
       'Ramamurthy Nagar', 'Malleshwaram', 'Akshaya Nagar', 'Shampura',
       'Kadugodi', 'LB Shastri Nagar', 'Hormavu', 'Vishwapriya Layout',
       'Kudlu Gate', '8th Phase JP Nagar', 'Bommasandra Industrial Area',
       'Anandapura', 'Vishveshwarya Layout', 'Kengeri Satellite Town',
       'Kannamangala', 'Hulimavu', 'Mahalakshmi Layout', 'Hosa Road',
       'Attibele', 'CV Raman Nagar', 'Kumaraswami Layout', 'Nagavara',
       'Hebbal Kempapura', 'Vijayanagar', 'Pattandur Agrahara',
       'Nagasandra', 'Kogilu', 'Panathur', 'Padmanabhanagar',
       '1st Block Jayanagar', 'Kammasandra', 'Dasarahalli', 'Magadi Road',
       'Koramangala', 'Dommasandra', 'Budigere', 'Kalyan nagar',
       'OMBR Layout', 'Horamavu Agara', 'Ambedkar Nagar',
       'Talaghattapura', 'Balagere', 'Jigani', 'Gollarapalya Hosahalli',
       'Old Madras Road', 'Kaggadasapura', '9th Phase JP Nagar', 'Jakkur',
       'TC Palaya', 'Giri Nagar', 'Singasandra', 'AECS Layout',
       'Mallasandra', 'Begur', 'JP Nagar', 'Malleshpalya', 'Munnekollal',
       'Kaggalipura', '6th Phase JP Nagar', 'Ulsoor', 'Thigalarapalya',
       'Somasundara Palya', 'Basaveshwara Nagar', 'Bommasandra',
       'Ardendale', 'Harlur', 'Kodihalli', 'Narayanapura',
       'Bannerghatta Road', 'Hennur', '5th Phase JP Nagar', 'Kodigehaali',
       'Billekahalli', 'Jalahalli', 'Mahadevpura', 'Anekal', 'Sompura',
       'Dodda Nekkundi', 'Hosur Road', 'Battarahalli', 'Sultan Palaya',
       'Ambalipura', 'Hoodi', 'Brookefield', 'Yelenahalli', 'Vittasandra',
       '2nd Stage Nagarbhavi', 'Vidyaranyapura', 'Amruthahalli',
       'Kodigehalli', 'Subramanyapura', 'Basavangudi', 'Kenchenahalli',
       'Banjara Layout', 'Kereguddadahalli', 'Kambipura',
       'Banashankari Stage III', 'Sector 7 HSR Layout', 'Rajiv Nagar',
       'Arekere', 'Mico Layout', 'Kammanahalli', 'Banashankari',
       'Chikkabanavar', 'HRBR Layout', 'Nehru Nagar', 'Kanakapura',
       'Konanakunte', 'Margondanahalli', 'R.T. Nagar', 'Tumkur Road',
       'Vasanthapura', 'GM Palaya', 'Jalahalli East', 'Hosakerehalli',
       'Indira Nagar', 'Kodichikkanahalli', 'Varthur Road', 'Anjanapura',
       'Abbigere', 'Tindlu', 'Gubbalala', 'Parappana Agrahara',
       'Cunningham Road', 'Kudlu', 'Banashankari Stage VI', 'Cox Town',
       'Kathriguppe', 'HBR Layout', 'Yelahanka New Town',
       'Sahakara Nagar', 'Rachenahalli', 'Yelachenahalli',
       'Green Glen Layout', 'Thubarahalli', 'Horamavu Banaswadi',
       '1st Phase JP Nagar', 'NGR Layout', 'Seegehalli', 'BEML Layout',
       'NRI Layout', 'ITPL', 'Babusapalaya', 'Iblur Village',
       'Ananth Nagar', 'Channasandra', 'Choodasandra', 'Kaikondrahalli',
       'Neeladri Nagar', 'Frazer Town', 'Cooke Town', 'Doddakallasandra',
       'Chamrajpet', 'Rayasandra', '5th Block Hbr Layout', 'Pai Layout',
       'Banashankari Stage V', 'Sonnenahalli', 'Benson Town',
       '2nd Phase Judicial Layout', 'Poorna Pragna Layout',
       'Judicial Layout', 'Banashankari Stage II', 'Karuna Nagar',
       'Bannerghatta', 'Marsur', 'Bommenahalli', 'Laggere',
       'Prithvi Layout', 'Banaswadi', 'Sector 2 HSR Layout',
       'Shivaji Nagar', 'Badavala Nagar', 'Nagavarapalya', 'BTM Layout',
       'BTM 2nd Stage', 'Hoskote', 'Doddaballapur', 'Sarakki Nagar',
       'Bharathi Nagar', 'HAL 2nd Stage', 'Kadubeesanahalli'))
st.write('You selected:', locality)

#sqft=st.number_input("Area (Square Feet)")
sqft = st.slider('Area (Square Feet)', 0, 10000, 1000)
#st.write("I'm ", age, 'years old')

options=['1', '2', '3','4','5']
bathroom = st.slider("Bathrooms",0,6,2 )
#bathroom=st.number_input"**Bathrooms**",step=1)

bhk = st.slider("BHK",0,6,2)

bhk=int(bhk)
bathroom=int(bathroom)
#bhk=st.number_input("**BHK**",step=1)



pickled_model = pickle.load(open('model.pkl', 'rb'))

def predict_price(location,sqft,bath,bhk):
    loc_index = np.where(data.columns==locality)[0][0]

    X = np.zeros(len(data.columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >= 0:
        X[loc_index] = 1

    return pickled_model.predict([X])[0]


import requests
from bs4 import BeautifulSoup

# url variable store url
# START=input()
start = locality
end = "Bangalore City Railway Station, Karnataka, India"
url = "https://www.google.com/search?q=+" + start + "+to+" + end + "+distance&sxsrf=APq-WBu0rmeRDmVFxHLNImuTL5x2YhEcuQ%3A1647434473643&ei=6doxYuzNJovg2roP0rqI6Ac&ved=0ahUKEwis5t3U08r2AhULsFYBHVIdAn0Q4dUDCA8&uact=5&oq=banaras+to+mumbai+distance&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOhIILhDHARDRAxDIAxCwAxBDGAI6DwguENQCEMgDELADEEMYAjoMCC4QyAMQsAMQQxgCOgYIABAHEB46BAgAEAo6CAgAEAgQBxAeOgcIIxCwAhAnOgQIABANOggIABAIEA0QHkoECEEYAEoECEYYAVCTC1j6sAFg4L4BaAFwAXgAgAGcAYgBxgySAQQwLjExmAEAoAEByAETwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz"
print(url)
# Get method of requests module
# return response object
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html')
# print(soup.prettify())
t=soup.find('div',class_="BNeawe deIvCb AP7Wnd")
#print(t.text)


START=locality
END="bangalore_airport"
URL ="https://www.google.com/search?q=+"+START+"+to+"+END+"+distance&sxsrf=APq-WBu0rmeRDmVFxHLNImuTL5x2YhEcuQ%3A1647434473643&ei=6doxYuzNJovg2roP0rqI6Ac&ved=0ahUKEwis5t3U08r2AhULsFYBHVIdAn0Q4dUDCA8&uact=5&oq=banaras+to+mumbai+distance&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOhIILhDHARDRAxDIAxCwAxBDGAI6DwguENQCEMgDELADEEMYAjoMCC4QyAMQsAMQQxgCOgYIABAHEB46BAgAEAo6CAgAEAgQBxAeOgcIIxCwAhAnOgQIABANOggIABAIEA0QHkoECEEYAEoECEYYAVCTC1j6sAFg4L4BaAFwAXgAgAGcAYgBxgySAQQwLjExmAEAoAEByAETwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz"
print (URL)
# Get method of requests module
# return response object
html_text=requests.get(URL).text
soup=BeautifulSoup(html_text,'html')
V=soup.find('div',class_="BNeawe deIvCb AP7Wnd")



if st.button('Estimate Price'):
    if bhk !=0:
        result=predict_price(locality,sqft,bathroom,bhk)
        if result < 0:
            st.subheader("No property of these requirements are available")
        else:
            if result > 100:
                result = round(result / 100, 2)
                result = str(result) + ' Crore'
            else:
                result = str(result) + ' Lakhs'

            with st.expander("Result ", expanded=True):
                st.subheader("predicted price is aprrox {} ".format(result))

st.text("Scraped button will gives more information about the selected location ")
if st.sidebar.button('Scraped'):
    with st.expander("Railway ", expanded=True):
        st.subheader("Distance of {} from Bangalore City Railway Station".format(locality))
        if (t == None):
            st.text("data not found")
        else:
            st.text(t.text)

    with st.expander("Airport ", expanded=True):
        st.subheader("Distance of {} from Bangalore City Airport".format(locality))
        if (V == None):
            st.text("data not found")

        else:
            st.text(V.text)


st.text("Scatter button will show a Scatter plot")
if st.sidebar.button('Scatter'):
        bhk2 = data2[(data2.location == locality) & (data2.bhk == bhk)]
        fig, ax = plt.subplots()
        ax.scatter(bhk2.total_sqft, bhk2.price, color="blue", label="{} bhk".format(bhk), s=50)
        plt.title("price(in lakhs) vs total SQFT for {} BHK in {}".format(bhk, locality))
        plt.xlabel('sqft')
        plt.ylabel('price')
        with st.expander("Scatter", expanded=True):
            st.pyplot()



