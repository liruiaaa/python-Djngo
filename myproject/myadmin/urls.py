from django.conf.urls import url

from . import views

urlpatterns = [
    #后台测试
    url(r'^$', views.index,name='index'),

    #后台管理路由
    #后台浏览界面
    url(r'users$',views.usersindex,name='myadmin_usersindex'),

    # 添加用户form表单界面
    url(r'^usersadd',views.usersadd,name='myadmin_usersadd'),

    #添加用户操作
    url(r'^usersinsert$',views.usersinsert,name='myadmin_usersinser'),

    #用户删除操作
    url(r'^usersdel/(?P<uid>[0-9]+)$', views.usersdel, name="myadmin_usersdel"),

    #加载用户信息
    url(r'^usersedit/(?P<uid>[0-9]+)$', views.usersedit, name="myadmin_usersedit"),


    #用户编辑操作
    url(r'^usersupdate/(?P<uid>[0-9]+)$', views.usersupdate, name="myadmin_usersupdate"),

    #用户登录验证
    url(r'^login$', views.login, name="myadmin_login"),
    url(r'^dologin$', views.dologin, name="myadmin_dologin"),
    url(r'^logout$', views.logout, name="myadmin_logout"),



    ################################生产计划

    url(r'^plans$',views.plans,name='myadmin_planusers'),
    url(r'^planadd$', views.planaddUsers, name="planaddusers"),  # 加载添加信息表单
    url(r'^planinsert$', views.planinsertUsers, name="planinsertusers"), #执行用户信息添加
    url(r'^(?P<uid>[0-9]+)/del$', views.plandelUsers, name="plandelusers"), #执行用户信息删除
    url(r'^(?P<uid>[0-9]+)/edit$', views.planeditUsers, name="planeditusers"), #加载用户信息编辑表单
    url(r'^update$', views.planupdateUsers, name="planupdateusers"), #执行用户信息编辑
#
#########################################生产领料
    url(r'^picks$', views.picks, name='myadmin_picks'),
    url(r'^pickadd$', views.pickaddUsers, name="pickaddusers"),  # 加载添加信息表单
    url(r'^pickinsert$', views.pickinsertUsers, name="pickinsertusers"), #执行用户信息添加
    url(r'^(?P<uid>[0-9]+)/pickdel$', views.pickdelUsers, name="pickdelusers"), #执行用户信息删除
    url(r'^(?P<uid>[0-9]+)/pickedit$', views.pickeditUsers, name="pickeditusers"), #加载用户信息编辑表单
    url(r'^update$', views.pickupdateUsers, name="pickupdateusers"), #执行用户信息编辑

    ################################供应商管理
    url(r'^gyss$', views.gyss, name='myadmin_gyss'),
    url(r'^(?P<uid>[0-9]+)/gysdel$', views.gysdelUsers, name="gysdelusers"),  # 执行用户信息删除
    url(r'^gysadd$', views.gysaddUsers, name="gysaddusers"),  # 加载添加信息表单
    url(r'^gysinsert$', views.gysinsertUsers, name="gysinsertusers"),  # 执行用户信息添加
###############################采购清单
    url(r'^cgs$', views.cgs, name='myadmin_cgusers'),
    url(r'^cgadd$', views.cgaddUsers, name="cgaddusers"),  # 加载添加信息表单
    url(r'^cginsert$', views.cginsertUsers, name="cginsertusers"),  # 执行用户信息添加
    url(r'^(?P<uid>[0-9]+)/cgdel$', views.cgdelUsers, name="cgdelusers"),  # 执行用户信息删除
    url(r'^(?P<uid>[0-9]+)/cgedit$', views.cgeditUsers, name="cgeditusers"),  # 加载用户信息编辑表单
    url(r'^update$', views.cgupdateUsers, name="cgupdateusers"),  # 执行用户信息



############################销售
    url(r'^xss$', views.xss, name='myadmin_xss'),
    url(r'^(?P<uid>[0-9]+)/xsdel$', views.xsdelUsers, name="xsdelusers"),  # 执行用户信息删除
    url(r'^xsadd$', views.xsaddUsers, name="xsaddusers"),  # 加载添加信息表单
    url(r'^xsinsert$', views.xsinsertUsers, name="xsinsertusers"),  # 执行用户信息添加

###################退货
    url(r'^ths$', views.ths, name='myadmin_ths'),
    url(r'^(?P<uid>[0-9]+)/thdel$', views.thdelUsers, name="thdelusers"),  # 执行用户信息删除
    url(r'^thadd$', views.thaddUsers, name="thaddusers"),  # 加载添加信息表单
    url(r'^thinsert$', views.thinsertUsers, name="thinsertusers"),  # 执行用户信息

    #########入库
    url(r'^rks$', views.rks, name='myadmin_rks'),
    url(r'^(?P<uid>[0-9]+)/rkdel$', views.rkdelUsers, name="rkdelusers"),  # 执行
################出库
    url(r'^cks$', views.cks, name='myadmin_cks'),
    url(r'^(?P<uid>[0-9]+)/ckdel$', views.ckdelUsers, name="ckdelusers"),  # 执行
###############库存
    url(r'^kcs$', views.kcs, name='myadmin_kcs'),
    url(r'^(?P<uid>[0-9]+)/kcdel$', views.kcdelUsers, name="kcdelusers"),  # 执行用户信息删除
    url(r'^kcadd$', views.kcaddUsers, name="kcaddusers"),  # 加载添加信息表单
    url(r'^kcinsert$', views.kcinsertUsers, name="kcinsertusers"),  # 执行用户信息添加

    ######################资金调动
    url(r'^zjs$', views.zjs, name='myadmin_zjs'),
    url(r'^zjadd$', views.zjaddUsers, name="zjaddusers"),  # 加载添加信息表单
    url(r'^zjinsert$', views.zjinsertUsers, name="zjinsertusers"),  # 执行用户信息添加
    url(r'^(?P<uid>[0-9]+)/zjdel$', views.zjdelUsers, name="zjdelusers"),  # 执行用户信息删除
    url(r'^(?P<uid>[0-9]+)/zjedit$', views.zjeditUsers, name="zjeditusers"),  # 加载用户信息编辑表单
    url(r'^update$', views.zjupdateUsers, name="zjupdateusers"),  # 执行用户信息
    ######################财务预算
######################资金调动
    url(r'^cws$', views.cws, name='myadmin_cws'),
    url(r'^cwadd$', views.cwaddUsers, name="cwaddusers"),  # 加载添加信息表单
    url(r'^cwinsert$', views.cwinsertUsers, name="cwinsertusers"),  # 执行用户信息添加
    url(r'^(?P<uid>[0-9]+)/cwdel$', views.cwdelUsers, name="cwdelusers"),  # 执行用户信息删除
    url(r'^(?P<uid>[0-9]+)/cwedit$', views.cweditUsers, name="cweditusers"),  # 加载用户信息编辑表单
    url(r'^update$', views.cwupdateUsers, name="cwupdateusers"),  # 执行用户信息
]


