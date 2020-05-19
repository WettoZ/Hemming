from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .forms import UserForm
import math
import random

def index(request):
    submitbutton= request.POST.get("submit")

    poolin = ''

    form = UserForm(request.POST or None)
    if form.is_valid():
        poolin = form.cleaned_data.get("poolin")

    ##############################
    def isTwo(t):
        while t > 2:
            t = t / 2

        if t == 2:
            return True
        else:
            return False

    def writeB(t):
        return str(t % 2)

    def steps(kl, strk):
        t = 0
        start = kl-1
        while start < len(strk):
            finish = start + kl
            if finish > len(strk):
                finish = len(strk)

            for s in range(start, finish):
                if strk[s] == '1':
                    t+= 1

            start = finish + kl

        return t


    def bControl(strk):
        kl = 0
        nstr = ''
        bnstr = ''
        for st in strk:
            kl += 1
            if st == 't':
                nstr += writeB(steps(kl, strk))
                bnstr += '<font color="blue">' + writeB(steps(kl, strk)) + '</font>'
            else:
                nstr += st
                bnstr += st

        blkb.append(bnstr)
        kb.append(nstr)


    def pBit(word):
        pool = ''
        for w in word:
            s = ''.join(format(ord(w), 'b'))
            while len(s) < 8:
                s = '0' + s

            pool+= s
            bn.append(w + ' = ' + s)

        return pool

    def WD(word):
        pool = pBit(word)
        while len(pool) > 0:
            if len(pool) >= 16:
                s = pool[:16]
            else:
                s = pool[:]
            pool = pool.replace(s, '')
            strk = 't'
            i = 0
            while len(s)>0:
                i +=1
                if isTwo(i+1):
                    strk += 't'
                else:
                    strk +=s[:1]
                    s = s[1:]

            bControl(strk)

    def fakeSymbol(kb):
        for k in kb:
            strk = k
            r = random.randint(0,len(strk)-1)
            l = 0
            nstr = ''
            pnstr = ''
            for s in strk:
                if l == r:
                    if s == '1':
                        nstr+= '0'
                        pnstr+= '<font color="red">0</font>'
                    else:
                        nstr+= '1'
                        pnstr+= '<font color="red">1</font>'
                else:
                    nstr+= s
                    pnstr+= s
                l+=1

            ob.append('В строке ' + pnstr + ' ошибка в символе ' + str(r+1))

            fb.append(nstr)

        return fb

    def DS(kb):
        for k in kb:
            kl = 0
            strk = k
            ch = ''

            for st in strk:
                if isTwo(kl+1) or kl == 0:
                    k = int(strk[kl] + writeB(steps(kl+1, strk))) % 2
                    ch += str(k)
                kl += 1

            ch = ch[::-1]
            bit = int(ch, 2)

            snrm.append("Синдром: " + ch + " == " + str(bit))

    kb = []
    blkb = []
    fb = []
    ob = []
    pob = []
    snrm = []
    bn = []
    WD(poolin)
    fakeSymbol(kb)
    DS(fb)


    context ={"form": form, 'submitbutton': submitbutton, 'kontrbit': blkb, 'syndrom': snrm, 'mark': ob, 'binv': bn}

    return render(request, 'front.html', context )

# Create your views here.
