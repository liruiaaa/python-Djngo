from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    state = models.IntegerField(default=1)
    addtime = models.IntegerField()

class scjh(models.Model):
    num = models.IntegerField(default=1)
    goods = models.CharField(max_length=16)
    leader = models.CharField(max_length=32)
    amount = models.IntegerField()
    need = models.IntegerField()
    kdate = models.IntegerField()
    wdate = models.IntegerField()

class pick(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    texture = models.CharField(max_length=32)
    amount = models.IntegerField()
    man = models.CharField(max_length=16)
    gdate = models.IntegerField()

#供应商
class gys(models.Model):
    name = models.CharField(max_length=32)
    namejc = models.CharField(max_length=16)
    kind = models.CharField(max_length=32)
    area = models.CharField(max_length=16)
    rank = models.CharField(max_length=16)

#采购清单
class cg(models.Model):
    clname = models.CharField(max_length=32)
    amount = models.IntegerField()
    need = models.IntegerField()
    money = models.CharField(max_length=16)
    gys = models.CharField(max_length=32)

#销售订单
class xs(models.Model):
    kehu = models.CharField(max_length=32)
    ymoney = models.CharField(max_length=16)
    hmoney = models.CharField(max_length=32)
    fh = models.CharField(max_length=16)
    ddate = models.CharField(max_length=32)

 #退货信息
class th(models.Model):
    thr = models.CharField(max_length=32)
    thzl = models.CharField(max_length=16)
    thsl = models.CharField(max_length=32)
    thyy = models.CharField(max_length=50)
    thrq = models.CharField(max_length=16)

#######入库
class rk(models.Model):
    kind = models.CharField(max_length=32)
    jhr = models.CharField(max_length=16)
    yhr = models.CharField(max_length=32)
    rkr = models.CharField(max_length=50)
    rkamount = models.IntegerField()
    rkdate = models.CharField(max_length=50)
##################出库
class ck(models.Model):
    kind = models.CharField(max_length=32)
    jhr = models.CharField(max_length=16)
    yhr = models.CharField(max_length=32)
    rkr = models.CharField(max_length=50)
    rkamount = models.IntegerField()
    rkdate = models.CharField(max_length=50)
    #######################库存清单
class kc(models.Model):
    name = models.CharField(max_length=32)
    sl = models.IntegerField()
    color = models.CharField(max_length=32)
    xh = models.IntegerField()

    ############################资金调动审批
class zj(models.Model):
    ddqx = models.CharField(max_length=32)
    sqr = models.CharField(max_length=16)
    ssbm = models.CharField(max_length=32)
    sqrq = models.CharField(max_length=50)
    sfty = models.CharField(max_length=50)
    #####################财务预算
class cw(models.Model):
    yt= models.CharField(max_length=32)
    bm = models.CharField(max_length=16)
    ysfy = models.CharField(max_length=32)
    ysr = models.CharField(max_length=50)
    spzt = models.CharField(max_length=50)


