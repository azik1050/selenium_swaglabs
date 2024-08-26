


def highlight(element, chrome_driver):
    chrome_driver = element._parent
    original_style = element.get_attribute('style')
    chrome_driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])",
                                 element, "style", "border: 2px solid red; " + original_style)
    return original_style
