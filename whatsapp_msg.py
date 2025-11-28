# pip install pywhatkit
import pywhatkit as kit

kit.sendwhatmsg_instantly(
    phone_no="+917878275650",   
    message="Hello from Python!",
    wait_time=2,               
    tab_close=True
)