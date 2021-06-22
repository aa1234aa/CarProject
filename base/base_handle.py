# 定义操作层的基类
class BaseHandle:
    
    # 定义针对元素的输入操作方法
    def input_text(self, element, text):
        """
        :param element: 表示的是元素对象
        :param text:  表示的是要输入的内容
        :return:
        """
        element.clear()
        element.send_keys(text)
        
        
     # 定义上传图片
    def send_image(self,element,image):
        element.send_keys(image)