mkdir -p ~/.streamlit/
echo "\[theme]\n\
base = "light"\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
enableWebsocketCompression = false\n\
" > ~/.streamlit/config.toml
