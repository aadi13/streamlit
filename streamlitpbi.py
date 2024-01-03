import streamlit as st

def embed_power_bi_report(embed_url, height=600, width=800):
    code = f"""
    <iframe width="{width}" height="{height}" src="{embed_url}" frameborder="0" allowfullscreen="true"></iframe>
    """
    return code

def main():
    st.title("Medicaid - Power BI Embedded Report")

    # Provided Power BI Embed URL
    power_bi_embed_url = "https://app.powerbi.com/reportEmbed?reportId=be9128c2-062d-4bb9-b1fb-52d55f91eaea&autoAuth=true&ctid=537777f2-95c5-4379-84bd-303c83dbe285"

    st.markdown(embed_power_bi_report(power_bi_embed_url), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
