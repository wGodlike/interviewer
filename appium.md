### Selenium元素定位
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

#### appium元素定位
find_element_by_ios_uiautomation()
find_element_by_android_uiautomator("xx")

driver.find_element_by_id("id")   # id定位
driver.find_element_by_name("name")  # name定位
driver.find_element_by_link_text("text")  # 链接名定位
driver.find_element_by_partial_link_text("text")  # 通过元素部分可见链接文本定位
driver.find_element_by_tag_name("name")  # 通过查找html的标签名称定位元素
driver.find_element_by_xpath("xpath")  # 路径定位
driver.find_element_by_class_name("android.widget.LinearLayout")  # 类名定位
driver.find_element_by_css_selector("css") # css选择器定位

#### 1.appium获取content-desc文本值用element.get_attribute('name');
#### 2.appium获取text属性的文本值用element.text或者element.get_attribute('text');
#### 3.appium中属性值对应的定位方式：
#### text->find_element_by_name
#### resource_id->find_element_by_id
#### class->find_element_by_class_name
#### content-desc->find_element_by_accessibility_id