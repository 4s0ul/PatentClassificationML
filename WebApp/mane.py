import streamlit as st
from data import process_data
from search import search
from award_stats import award_stats
from upload import upload_doc

data, nlp = process_data()

tab1, tab2, tab3 = st.tabs(["Search", "Upload", "Data"])

with tab1:

    col1, col2 = st.columns(2)
    
    with col1:

        st.header('Search')

        search_text = st.text_input('Input text')

        class_of_doc = st.selectbox('Class', ('None', 'Human Necessities', 'Performing Operations; Transporting', 'Chemistry; Metallurgy', 'Physics', 'Electricity'))

        if st.button('Search'):
            if search_text != '':
                most_similar_texts, result = search(class_of_doc, search_text, nlp, data)
                awards = []
                for i in most_similar_texts:
                    st.markdown(f"**Publication number:** {data['publication_number'][i]}")
                    st.markdown(f"**Class:** {data['label'][i]}")
                    awards.append(int(data['award'][i]))
                    st.markdown(f"**Award:** ${data['award'][i]}")
                    st.write(f"**Cosine similarity score:** {result[i]}")
                    st.subheader("Abstract:")
                    st.write(data['abstract'][i])
                    with st.expander("See description"):
                        st.subheader("Description:")
                        st.write(data['description'][i])
            elif search_text == '':
                st.write('Please write text')

            with col2:

                st.header('Award stats')

                sum_of_awards, avg_award = award_stats(awards)
                st.markdown(f"<h5 style='text-align: center;'>Sum of awards:</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5 style='text-align: center;'>${sum_of_awards}</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5 style='text-align: center;'>Average award per patent:</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5 style='text-align: center;'>${avg_award}</h5>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align: center;'>Distribution of awards</h3>", unsafe_allow_html=True)
                st.bar_chart(awards)
with tab2:

    st.header('Upload your stuff!')
    upload_publication_number = st.text_input(label = 'Publication number')
    upload_abstract = st.text_area(label='Insert Abstract of your document')
    upload_application_number = st.text_input(label = 'Application number')
    upload_description = st.text_area(label='Insert Description of your document')
    upload_award = st.text_input(label='Insert award')
    
    if st.button(label= 'Upload!'):
        if [upload_publication_number, upload_abstract, upload_application_number, upload_description] != ['', '', '', '']:
            data = upload_doc(upload_publication_number, upload_abstract, upload_application_number, upload_description, upload_award, data, nlp)
        elif [upload_publication_number, upload_abstract, upload_application_number, upload_description] == ['', '', '', '']:
            st.write('Make sure you have entered all information')

with tab3:
    display_data = data.drop('nlp_docs', axis = 1).tail()
    st.dataframe(display_data)
    # if st.button(label='delete last row'):
    #     data = data.drop(data.tail(1).index,inplace=True)

