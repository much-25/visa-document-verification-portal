from utils import extract_text
import streamlit as st
import pycountry

from countries import (
    default_requirements,
    special_requirements
)

st.title("Visa Document Verification Portal")

countries = sorted(
    [country.name for country in pycountry.countries]
)

# Country dropdown
selected_country = st.selectbox(
    "Select Country",
    countries
)

st.subheader("Required Documents")

all_documents = default_requirements.copy()

for doc in default_requirements:
    st.write(f"- {doc}")

if selected_country in special_requirements:

    st.subheader("Additional Requirements")

    for doc in special_requirements[selected_country]:

        st.write(f"- {doc}")

        all_documents.append(doc)

uploaded_files = {}

st.subheader("Upload Documents")

for doc in all_documents:

    uploaded_files[doc] = st.file_uploader(
        f"Upload {doc}",
        type=["pdf", "png", "jpg", "jpeg"]
    )

if st.button("Verify Documents"):

    missing_docs = []

    for doc, file in uploaded_files.items():

        if file is None:
            missing_docs.append(doc)

    if missing_docs:

        st.error("Missing Documents:")

        for doc in missing_docs:
            st.write(f"- {doc}")

    else:

        st.success("All required documents uploaded")

passport_file = uploaded_files.get("Passport")

if passport_file:

    extracted_text = extract_text(passport_file)

    st.subheader("Extracted Passport Text")

    st.write(extracted_text)


