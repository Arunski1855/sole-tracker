import pages.brand_dashboard as brand
import pages.comp_finder as comp
import pages.growth_tracker as growth


# Page config
st.set_page_config(
    page_title="Sole Tracker",
    page_icon="👟",
    layout="wide",
)

# Sidebar navigation
st.sidebar.title("Sole Tracker Navigation")

# Load logos
try:
    eybl_logo = Image.open("assets/eybl.png")
    sssb_logo = Image.open("assets/3ssb.png")
    uaa_logo = Image.open("assets/uaa.png")
    puma_logo = Image.open("assets/puma.png")

    st.sidebar.image(eybl_logo, width=120)
    st.sidebar.image(sssb_logo, width=120)
    st.sidebar.image(uaa_logo, width=120)
    st.sidebar.image(puma_logo, width=120)

except:
    st.sidebar.warning("Logos not found. Continue without them.")

# Sidebar page selection
page = st.sidebar.radio("Go to:", ["Brand Dashboard", "Comp Finder", "Growth Tracker"])

if page == "Brand Dashboard":
    brand.show()
elif page == "Comp Finder":
    comp.show()
elif page == "Growth Tracker":
    growth.show()


