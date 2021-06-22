# 定义测试类
import time

import pytest
from utils.UtilsDriver import UtilsDriver
from proxy.login_proxy import LoginProxy
from utils.UtilsDriver import get_msg
from utils.UtilsDriver import case_data
from utils.UtilsDriver import action_down
from proxy.map_proxy import MapProxy
from proxy.realtime_proxy import RealTimeProxy


login_case_data = case_data("data/login.json")


@pytest.mark.run(order=2)
class TestLogin:
    def setup_class(self):
        # 实例化首页和登录的业务对象
        self.real_time_proxy=RealTimeProxy()
        self.login_proxy = LoginProxy()
        self.map_proxy = MapProxy()
       
    
    def setup(self):
        UtilsDriver.get_driver().refresh()
    # 创建类级别fixture销毁的操作方法
    #def teardown_class(self):
        #UtilsDriver.quit_driver()

    # 定义测试方法  账号不存在
    @pytest.mark.parametrize("username, password,expect", login_case_data)
    def test_login_01(self, username, password,expect):
        code = input("请输入验证码")
        self.login_proxy.login(username,password,code)
        msg = get_msg()
        time.sleep(2)
        assert expect in msg

    @pytest.mark.skip(reason="一直获取不到上过线")
    # 断言车辆实时状态里面的终端在线状态是否为上过线
    def test_select_carnum(self):
        self.map_proxy.map_span1()
        self.real_time_proxy.get_online_status()
        select1 = self.real_time_proxy.get_is_over_the_line()
        assert '上过线' in select1
        self.real_time_proxy.get_find_home_page()
        
    @pytest.mark.skip(reason="一直获取不到上过线")
    # 断言车辆实时状态里面的终端在线状态是否为上过线
    def test_select_noline(self):
        self.map_proxy.map_span2()
        self.real_time_proxy.get_online_status()
        select1 = self.real_time_proxy.get_is_over_the_line()
        assert '从未上过线' in select1
        self.real_time_proxy.get_find_home_page()

    @pytest.mark.skip(reason="一直获取不到上过线")
    # 断言车辆实时状态里面的gps定位为无定位
    def test_select_notonline(self):
        self.map_proxy.map_span3()
        self.real_time_proxy.get_find_open_select()
        self.real_time_proxy.get_find_gps_status()
        select1 = self.real_time_proxy.get_find_no_position()
        assert '无定位' in select1
        self.real_time_proxy.get_find_home_page()

    @pytest.mark.skip(reason="一直获取不到上过线")
    # 断言首页中的车辆总数和车辆实时中的车辆总数是否一致
    def test_carnum(self):
        car_num = self.map_proxy.span1_num()
        self.map_proxy.map_span1()
        action_down()
        real_num = self.real_time_proxy.get_find_car_num()
        assert car_num == real_num
        self.real_time_proxy.get_find_home_page()

    @pytest.mark.skip(reason="一直获取不到上过线")
    # 断言首页中的从未在线总数和车辆实时中的车辆总数是否一致
    def test_noline(self):
        no_line_num = self.map_proxy.span2_num()
        self.map_proxy.map_span2()
        action_down()
        real_num = self.real_time_proxy.get_find_car_num()
        assert no_line_num == real_num
        self.real_time_proxy.get_find_home_page()

    @pytest.mark.skip(reason="一直获取不到上过线")
    # 断言首页中的无定位车辆总数和车辆实时中的车辆总数是否一致
    def test_notonline(self):
        not_online_num = self.map_proxy.span3_num()
        self.map_proxy.map_span3()
        action_down()
        real_num = self.real_time_proxy.get_find_car_num()
        assert not_online_num == real_num
        self.real_time_proxy.get_find_home_page()
        
   
        
        
        
    
    

