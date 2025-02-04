class MyHomeUploadSelectors:
    AUTHENTICATION_BUTTON = "#root > section > article > button"
    EMAIL_INPUT_FIELD = "div.wrapper > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div > div > div > form > div.forms-group div:nth-of-type(1) > div > input"
    PASSWORD_INPUT_FIELD = "div.wrapper > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div > div > div > form > div:nth-of-type(1) div:nth-of-type(2) > div > input"
    CONFIRM_AUTHENTICATION_BUTTON = "div.wrapper > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div > div > div > form > div:nth-of-type(3) > button"
    PROPERTY_TYPE_BUTTONS = "#root > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(2) > div > div > div > div"
    PROPERTY_TYPE_TEXT = "label > div > div > span:nth-of-type(1)"
    TRANSACTION_TYPE_BUTTONS = "#root > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(3) > div > div > div >div"
    TRANSACTION_TYPE_TEXT = "label > div > div > span:nth-of-type(1)"
    INPUT_CITY = "#root > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(6) > div > div > div > div > input"
    SELECT_CITY = "#root > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(6) > div > div > div > div:nth-of-type(2) > ul > li"
    INPUT_STREET = "#root > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(7) > div > div:nth-of-type(1) > div:nth-of-type(2) > label > input"
    SELECT_STREET = "#root > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(7) > div > div:nth-of-type(1) > div:nth-of-type(2) > div > "