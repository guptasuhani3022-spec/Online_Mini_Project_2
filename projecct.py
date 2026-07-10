import pandas as pd                                                                # for data 
import streamlit as st                                                             #for ui design
from sklearn.model_selection import train_test_split                               #for data devide
from sklearn.tree import DecisionTreeClassifier                                    # ml model selection
from sklearn.metrics import accuracy_score                                         #for accurecy check

st.set_page_config(page_title="Loan Approval App",page_icon="🏦")
# run command in terminal = streamlit run app.py  #8501
#streamlit run app.py --server.port 8502 - these command use for specific port

#for page title
st.title("🏦 Loan Approval Prediction System")

#load dataset
df = pd.read_csv("loan.csv")

#create two variable(x,y) for input and output
x=df[["Income","CIBIL_Score","Loan_Amount","Employment_Years"]]
y=df["Loan_Status"]

#data devide
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42,stratify=y)
model = DecisionTreeClassifier(max_depth=3,min_samples_split=8,min_samples_leaf=4,random_state=42)
model.fit(x_train,y_train)
prediction = model.predict(x_test)
accuracy = accuracy_score(y_test,prediction)

st.success(f"Model Accuracy :{accuracy*100:.2f} %")

income = st.sidebar.number_input("💵 Income :",min_value=10000,max_value=100000,value=40000,step=5000)
cibil = st.sidebar.number_input("🎼 CIBIL Score :",min_value=300,max_value=900,value=700,step=50)
loan = st.sidebar.number_input("💰 Loan Ammount :",min_value=50000,max_value=1000000,value=200000,step=5000)
experience = st.sidebar.number_input("👱Employment Years :",min_value=0,max_value=40,value=5,step=5)

if st.button("Predict Loan"):
    result = model.predict([[income,cibil,loan,experience]])
    
    if result[0]==1:
        approved=min(loan,int(income*8+(cibil-650)*400+experience*12000)) 
        if approved<0:
            approved=0

        st.success("👏 Loan Approved")
        st.info(f"Approved Loan Ammount :₹ {approved:,}")
    else:
        st.error("❌ Loan Rejected")

st.markdown("---")
st.markdown(""" 
            <center> 
            
            ### Loan Approval Prediction System
             Developed by **Suhani Gupta** 
            Machine Learning Project /n
            Guided by **Chandrama Prashad Yadav sir**
            </center>
            """,unsafe_allow_html=True)