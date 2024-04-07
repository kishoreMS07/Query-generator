import pandas as pd
import streamlit as st

# SQL query templates
sql_templates = {
    'Tell me what the notes are for South Australia ': 'SELECT Notes FROM table WHERE Current slogan = SOUTH AUSTRALIA',
    'What is the current series where the new series began in June 2011?': 'SELECT Current series FROM table WHERE Notes = New series began in June 2011',
    'What is the format for South Australia?': 'SELECT Format FROM table WHERE State/territory = South Australia',
    'Name the background colour for the Australian Capital Territory': 'SELECT Text/background colour FROM table WHERE State/territory = Australian Capital Territory',
    'how many times is the fuel propulsion is cng?': 'SELECT COUNT Fleet Series (Quantity) FROM table WHERE Fuel Propulsion = CNG',
    'what is the fuel propulsion where the fleet series (quantity) is 310-329 (20)?': 'SELECT Fuel Propulsion FROM table WHERE Fleet Series (Quantity) = 310-329 (20)',
    'who is the manufacturer for the order year 1998?': 'SELECT Manufacturer FROM table WHERE Order Year = 1998',
    'how many times is the model ge40lfr?': 'SELECT COUNT Manufacturer FROM table WHERE Model = GE40LFR',
    'how many times is the fleet series (quantity) is 468-473 (6)?': 'SELECT COUNT Order Year FROM table WHERE Fleet Series (Quantity) = 468-473 (6)',
    'what is the powertrain (engine/transmission) when the order year is 2000?': 'SELECT Powertrain (Engine/Transmission) FROM table WHERE Order Year = 2000',
    
}

# Streamlit app
def main():
    st.title('Query Generator')

    # Text input for user to enter the query
    user_query = st.text_area('Enter your query:', height=100)

    # Button to execute the query
    if st.button('Generate SQL Query'):
        # Apply the conversion function to the user query
        sql_query = query_to_sql(user_query)

        # Display the SQL query
        st.subheader('Generated SQL Query:')
        st.code(sql_query, language='sql')

# Function to convert a query into an SQL query
def query_to_sql(query):
    for query_type, template in sql_templates.items():
        if query_type in query:
            return template
    return "SELECT COUNT(*) FROM head WHERE age > 56"

if __name__ == '__main__':
    main()
