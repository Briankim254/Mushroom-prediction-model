 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(gillsize, bruises, stalkshape, ringnumber, veilcolor, capsurface):   
 
    # Preprocessing user input    
    if gillsize == "narrow":
        gillsize_n = 1
    else:
        gillsize_n = 0
 
    if bruises == "false":
        bruises_t = 0
    else:
        bruises_t = 1

    if stalkshape == "tapering":
        stalkshape_t = 1
    else:
        stalkshape_t = 0

    if ringnumber =="one":
        ringnumber_o = 1
        ringnumber_t = 0  
    else :
        ringnumber_t = 1
        ringnumber_o = 0
    
        
    if veilcolor == "orange":
        veilcolor_o = 1
        veilcolor_w = 0
        veilcolor_y = 0
    elif veilcolor=="white":
        veilcolor_w = 1 
        veilcolor_o = 0
        veilcolor_y = 0   
    else:
        veilcolor_y = 1
        veilcolor_o = 0
        veilcolor_w = 0


    if  capsurface == "grooves":
        capsurface_g = 1
        capsurface_s = 0
        capsurface_y = 0
    elif  capsurface == "smooth":
        capsurface_s = 1
        capsurface_g = 0
        capsurface_y = 0
    else:
        capsurface_y = 1
        capsurface_s = 0
        capsurface_g = 0
    
    

    # Making predictions 
    prediction = classifier.predict( 
        [[gillsize_n, bruises_t, stalkshape_t, ringnumber_o, ringnumber_t, veilcolor_o, veilcolor_w, veilcolor_y, capsurface_g, capsurface_s, capsurface_y]])
     
    if prediction == 0:
        pred = 'poisonous'
    else:
        pred = 'edible'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Mushroom Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    gillsize = st.selectbox('gill size',("narrow","broad"))
    bruises = st.selectbox('bruises',("true","false")) 
    stalkshape = st.selectbox('stalk shape',("tapering","enlarging")) 
    ringnumber = st.selectbox('ring number',("one","two"))
    veilcolor = st.selectbox('veil colour',("yellow","orange","white"))
    capsurface = st.selectbox('cap surface',("smooth","scaly","grooves"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(gillsize, bruises, stalkshape, ringnumber, veilcolor, capsurface) 
        st.success('Your mushroom is {}'.format(result))
        # print(LoanAmount)
     
if __name__=='__main__': 
    main()
