from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


from myadmin.models import users
from myadmin.models import scjh
from myadmin.models import pick
from myadmin.models import gys
from myadmin.models import xs
from myadmin.models import cg
from myadmin.models import th
from myadmin.models import rk
from myadmin.models import ck
from myadmin.models import kc
from myadmin.models import zj
from myadmin.models import cw
import time
# Create your views here.

#========主页区========
def index(request):
    return render(request,'index.html')

#=============后台管理逻辑================
#用户展示界面
def usersindex(request):
    print('ok')
    list = users.objects.all()
    context = {'userslist':list}
    # return HttpResponse(list)
    return render(request,'users/index.html',context)

#管理员信息添加表单
def usersadd(request):
    return render(request,'users/add.html')

#管理信息添加
def usersinsert(request):
    try:
        ob = users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        #md5 方式加密传输密码
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding='utf-8'))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.addtime = time.time()
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}
    return render(request,'info.html',context)

#用户删除操作
def usersdel(request,uid):
    try:
        ob = users.objects.get(id = uid)
        ob.delete()
        context = {'info':'删除成功！！'}
    except:
        context = {'info':'删除失败！！'}
    return render(request,'info.html',context)

#加载用户界面
def usersedit(request,uid):
    try:
        ob = users.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"users/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
        return render(request,"info.html",context)


#用户编辑操作
def usersupdate(request,uid):
    try:
        ob = users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = request.POST['state']
        ob.save()
        context = {'info': '修改成功！'}
    except:
        context = {'info': '修改失败！'}
    return render(request, "info.html", context)


#===================后台用户登录严重====================

# 登录表单
def login(request):
    return render(request,'login.html')
# 执行登录
# 执行操作
def dologin(request):
    try:
        #根据账号获取登录者信息
        user = users.objects.get(username=request.POST['username'])
        print('ssss:-->',user.username)
        #判断当前用户是否是后台管理员用户
        if user.state == 0:
            # 验证密码
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'],encoding="utf8"))
            print('sss:',user.password,m.hexdigest())
            if user.password == m.hexdigest():

                #此处登录成功，将当前登录信息放入到session中，并跳转页面
                request.session['adminuser'] = user.name
                print('aaaaaaaaaaaaa!')
                #print(json.dumps(user))
                return redirect(reverse('index'))
            else:
                context = {'info':'登录密码错误！'}
        else:
            context = {'info':'此用户非后台管理用户！'}
    except:
        context = {'info':'登录账号错误！'}
    return render(request,"login.html",context)


# 管理员退出
def logout(request):
    try:
        # 清除登录的session信息
        del request.session['adminuser']
        # 跳转登录页面（url地址改变）
        return redirect(reverse('myadmin_login'))
    except:
        return render(request,'aa.html')




#===================生產計劃====================


def plans(request):
    lists = scjh.objects.all()
    context={'stu':lists}
    return render(request,'plan.html',context)
#添加用户
def planaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"planadd.html")

#添加动作
def planinsertUsers(request):
    try:
        ob=scjh()
        ob.num=request.POST['num']
        ob.goods=request.POST['goods']
        ob.leader=request.POST['leader']
        ob.amount=request.POST['amount']
        ob.need=request.POST['need']
        ob.kdate=request.POST['kdate']
        ob.wdate=request.POST['wdate']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)
# #删除
def plandelUsers(request,uid):
    try:
        ob = scjh.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
# #编辑
def planeditUsers(request,uid):

    ob = scjh.objects.get(id=uid)
    context = {"scjh":ob}
    return render(request,"planedit.html",context)
    # except:
    #     context = {'info':'没有找到要修改的信息！'}
    # return render(request,"planinfo.html",context)
#修改更新
def planupdateUsers(request):
    # try:
        ob = scjh.objects.get(id= request.POST['id'])
        ob.num = request.POST['num']
        ob.goods = request.POST['goods']
        ob.leader = request.POST['leader']
        ob.amount = request.POST['amount']
        ob.need = request.POST['need']
        ob.kdate = request.POST['kdate']
        ob.wdate = request.POST['wdate']
        ob.save()
        context = {'info':'修改成功！'}
    # except:
    #     context = {'info':'修改失败！'}
        return render(request,"planinfo.html",context)


####################生产领料##############################
def picks(request):
    lists = pick.objects.all()
    context={'pi':lists}
    return render(request,'picking.html',context)
#添加用户
def pickaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"pickadd.html")

#添加动作
def pickinsertUsers(request):
    try:
        ob=pick()
        ob.name=request.POST['name']
        ob.color=request.POST['color']
        ob.texture=request.POST['texture']
        ob.amount=request.POST['amount']
        ob.man=request.POST['man']
        ob.gdate=request.POST['gdate']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)
def pickdelUsers(request,uid):
    try:
        ob = pick.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
# #编辑
def pickeditUsers(request,uid):

    ob = pick.objects.get(id=uid)
    context = {"pick":ob}
    return render(request,"pickedit.html",context)
    # except:
    #     context = {'info':'没有找到要修改的信息！'}
    # return render(request,"planinfo.html",context)
#修改更新
def pickupdateUsers(request):
    # try:
        ob = pick.objects.get(id= request.POST['id'])
        ob.name = request.POST['name']
        ob.color = request.POST['color']
        ob.texture = request.POST['texture']
        ob.amount = request.POST['amount']
        ob.man = request.POST['man']
        ob.gdate = request.POST['gdate']
        ob.save()
        context = {'info':'修改成功！'}
    # except:
    #     context = {'info':'修改失败！'}
        return render(request,"planinfo.html",context)

#########################采购管理
def gyss(request):
    lists = gys.objects.all()
    context={'gy':lists}
    return render(request,'gys.html',context)
def gysdelUsers(request,uid):
    try:
        ob = gys.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
#添加用户
def gysaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"gysadd.html")

#添加动作
def gysinsertUsers(request):
    try:
        ob=gys()
        ob.name=request.POST['name']
        ob.namejc=request.POST['namejc']
        ob.kind=request.POST['kind']
        ob.area=request.POST['area']
        ob.rank=request.POST['rank']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)
#######采购清单
def cgs(request):
    lists = cg.objects.all()
    context={'stu':lists}
    return render(request,'cg.html',context)
#添加用户
def cgaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"cgadd.html")

#添加动作
def cginsertUsers(request):
    try:
        ob=cg()
        ob.clname=request.POST['clname']
        ob.amount=request.POST['amount']
        ob.need=request.POST['need']
        ob.money=request.POST['money']
        ob.gys=request.POST['gys']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)
# #删除
def cgdelUsers(request,uid):
    try:
        ob = cg.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
# #编辑
def cgeditUsers(request,uid):

    ob = cg.objects.get(id=uid)
    context = {"cg":ob}
    return render(request,"cgedit.html",context)
    # except:
    #     context = {'info':'没有找到要修改的信息！'}
    # return render(request,"planinfo.html",context)
#修改更新
def cgupdateUsers(request):
    # try:
        ob = cg.objects.get(id= request.POST['id'])
        ob.clname = request.POST['clname']
        ob.amount = request.POST['amount']
        ob.need = request.POST['need']
        ob.money = request.POST['money']
        ob.gys = request.POST['gys']
        ob.save()
        context = {'info':'修改成功！'}
    # except:
    #     context = {'info':'修改失败！'}
        return render(request,"planinfo.html",context)




##################销售
def xss(request):
    lists = xs.objects.all()
    context={'xs':lists}
    return render(request,'xs.html',context)
def xsdelUsers(request,uid):
    try:
        ob = xs.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
#添加用户
def xsaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"xsadd.html")

#添加动作
def xsinsertUsers(request):
    try:
        ob=xs()
        ob.kehu=request.POST['kehu']
        ob.ymoney=request.POST['ymoney']
        ob.hmoney=request.POST['hmoney']
        ob.fh=request.POST['fh']
        ob.ddtae=request.POST['ddate']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)


##############################退货
def ths(request):
    lists = th.objects.all()
    context={'th':lists}
    return render(request,'th.html',context)
def thdelUsers(request,uid):
    try:
        ob = th.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
#添加用户
def thaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"thadd.html")

#添加动作
def thinsertUsers(request):
    try:
        ob=th()
        ob.thr=request.POST['thr']
        ob.thzl=request.POST['thzl']
        ob.thsl=request.POST['thsl']
        ob.thyy=request.POST['thyy']
        ob.thrq=request.POST['thrq']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)

################入库
def rks(request):
    lists = rk.objects.all()
    context={'rk':lists}
    return render(request,'rk.html',context)
def rkdelUsers(request,uid):
    try:
        ob = rk.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
####出库
def cks(request):
    lists = ck.objects.all()
    context={'ck':lists}
    return render(request,'ck.html',context)
def ckdelUsers(request,uid):
    try:
        ob = ck.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
###################库存
def kcs(request):
    lists = kc.objects.all()
    context={'kc':lists}
    return render(request,'kc.html',context)
def kcdelUsers(request,uid):
    try:
        ob = kc.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
#添加用户
def kcaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"kcadd.html")

#添加动作
def kcinsertUsers(request):
    try:
        ob=kc()
        ob.name=request.POST['name']
        ob.sl=request.POST['sl']
        ob.color=request.POST['color']
        ob.xh=request.POST['xh']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)
##################资金调动审批
def zjs(request):
    lists = zj.objects.all()
    context={'zj':lists}
    return render(request,'zj.html',context)
#添加用户
def zjaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"zjadd.html")

#添加动作
def zjinsertUsers(request):
    try:
        ob=zj()
        ob.ddqx=request.POST['ddqx']
        ob.sqr=request.POST['sqr']
        ob.ssbm=request.POST['ssbm']
        ob.sqrq=request.POST['sqrq']
        ob.sfty=request.POST['sfty']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)
# #删除
def zjdelUsers(request,uid):
    try:
        ob = zj.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
# #编辑
def zjeditUsers(request,uid):

    ob = zj.objects.get(id=uid)
    context = {"zj":ob}
    return render(request,"zjedit.html",context)
    # except:
    #     context = {'info':'没有找到要修改的信息！'}
    # return render(request,"planinfo.html",context)
#修改更新
def zjupdateUsers(request):
    # try:
        ob = zj.objects.get(id= request.POST['id'])
        ob.ddqx = request.POST['ddqx']
        ob.sqr = request.POST['sqr']
        ob.ssbm = request.POST['ssbm']
        ob.sqrq = request.POST['sqrq']
        ob.sfty = request.POST['sfty']
        ob.save()
        context = {'info':'修改成功！'}
    # except:
    #     context = {'info':'修改失败！'}
        return render(request,"planinfo.html",context)
##################财务预算
def cws(request):
    lists = cw.objects.all()
    context={'cw':lists}
    return render(request,'cw.html',context)
#添加用户
def cwaddUsers(request):
    #return HttpResponse("添加操作触发")
    return render(request,"cwadd.html")

#添加动作
def cwinsertUsers(request):
    try:
        ob=cw()
        ob.yt=request.POST['yt']
        ob.bm=request.POST['bm']
        ob.ysfy=request.POST['ysfy']
        ob.ysr=request.POST['ysr']
        ob.spzt=request.POST['spzt']
        ob.save()
        context={"info":'添加成功'}
    except:
        context={'info':'修改失败！'}
    return render(request, "planinfo.html",context)
# #删除
def cwdelUsers(request,uid):
    try:
        ob = cw.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "planinfo.html", context)
# #编辑
def cweditUsers(request,uid):

    ob = cw.objects.get(id=uid)
    context = {"cw":ob}
    return render(request,"cwedit.html",context)
    # except:
    #     context = {'info':'没有找到要修改的信息！'}
    # return render(request,"planinfo.html",context)
#修改更新
def cwupdateUsers(request):
    # try:
        ob = cw.objects.get(id= request.POST['id'])
        ob.yt = request.POST['yt']
        ob.bm = request.POST['bm']
        ob.ysfy = request.POST['ysfy']
        ob.ysr = request.POST['ysr']
        ob.spzt = request.POST['spzt']
        ob.save()
        context = {'info':'修改成功！'}
    # except:
    #     context = {'info':'修改失败！'}
        return render(request,"planinfo.html",context)