import streamlit as st
from page import home, image_upload, drawing_canvas
from config.settings import NAV_OPTIONS, PAGE_CONFIG

# Configure the page
st.set_page_config(**PAGE_CONFIG)

def main():
    # Initialize query params and session state
    query_params = st.query_params
    
    # Set default page to home if no page param exists
    if 'page' not in query_params:
        query_params.page = "home"
    
    # Initialize or update session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = query_params.page
    else:
        # Sync session state with URL params
        if st.session_state.current_page != query_params.page:
            st.session_state.current_page = query_params.page
    
    # Sidebar navigation
    st.sidebar.image("assets/mainLogo.png", use_container_width=True)
    st.sidebar.title("Navigation")
    
    # Navigation buttons
    for emoji, label, page_key in NAV_OPTIONS:
        if st.sidebar.button(f"{emoji} **{label}**", 
                           key=f"nav_{page_key}", 
                           use_container_width=True,
                           type="primary" if st.session_state.current_page == page_key else "secondary"):
            st.session_state.current_page = page_key
            st.query_params.page = page_key
            st.rerun()
    
    st.sidebar.divider()
    
    # Route to appropriate page
    if st.session_state.current_page == "home":
        home.show()
    elif st.session_state.current_page == "image_upload":
        image_upload.show()
    elif st.session_state.current_page == "drawing_canvas":
        drawing_canvas.show()

if __name__ == "__main__":
    main()