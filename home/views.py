from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from firebase_admin import credentials, firestore, initialize_app
import pdb
import firebase_admin
import pandas as pd
import numpy as np

cred = credentials.Certificate('home/keyduc.json')
default_app = initialize_app(cred)
db = firestore.client()

def data_table(self):
    todo_ref = db.collection('dulieutam')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos)
    return data

def data_table1(self):
    todo_ref = db.collection('csvjson')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos)
    return data
##SCATTERHART
def CounTries(self):
    data = data_table(1)  
    data1 = data.loc[0,["World"]]
    return list(data1)
def d1980(self):
     data = data_table(1)  
     data2 = data.loc[0,["Nam"]]
     return list(data2)

def CounTries1(self):
    data = data_table(1)  
    c1 = data.loc[1,["World"]]
    return list(c1)
def d1981(self):
     data = data_table(1)  
     d1 = data.loc[1,["Nam"]]
     return list(d1)
     
def CounTries2(self):
    data = data_table(1)  
    c2 = data.loc[2,["World"]]
    return list(c2)
def d1982(self):
     data = data_table(1)  
     d2 = data.loc[2,["Nam"]]
     return list(d2)

def CounTries3(self):
    data = data_table(1)  
    c3 = data.loc[3,["World"]]
    return list(c3)
def d1983(self):
     data = data_table(1)  
     d3 = data.loc[3,["Nam"]]
     return list(d3)

def CounTries4(self):
    data = data_table(1)  
    c4 = data.loc[4,["World"]]
    return list(c4)
def d1984(self):
     data = data_table(1)  
     d4 = data.loc[4,["Nam"]]
     return list(d4)

def CounTries5(self):
    data = data_table(1)  
    c5 = data.loc[5,["World"]]
    return list(c5)
def d1985(self):
     data = data_table(1)  
     d5 = data.loc[5,["Nam"]]
     return list(d5)  

def CounTries6(self):
    data = data_table(1)  
    c6 = data.loc[6,["World"]]
    return list(c6)
def d1986(self):
     data = data_table(1)  
     d6 = data.loc[6,["Nam"]]
     return list(d6)

def CounTries7(self):
    data = data_table(1)  
    c7 = data.loc[7,["World"]]
    return list(c7)
def d1987(self):
     data = data_table(1)  
     d7 = data.loc[7,["Nam"]]
     return list(d7)

def CounTries8(self):
    data = data_table(1)  
    c8 = data.loc[8,["World"]]
    return list(c8)
def d1988(self):
     data = data_table(1)  
     d8 = data.loc[8,["Nam"]]
     return list(d8)

def CounTries9(self):
    data = data_table(1)  
    c9 = data.loc[9,["World"]]
    return list(c9)
def d1989(self):
     data = data_table(1)  
     d9 = data.loc[9,["Nam"]]
     return list(d9)    

def CounTries10(self):
    data = data_table(1)  
    c10 = data.loc[10,["World"]]
    return list(c10)
def d1990(self):
     data = data_table(1)  
     d10 = data.loc[10,["Nam"]]
     return list(d10)  

def CounTries11(self):
    data = data_table(1)  
    c11 = data.loc[11,["World"]]
    return list(c11)
def d1991(self):
     data = data_table(1)  
     d11 = data.loc[11,["Nam"]]
     return list(d11) 

def CounTries12(self):
    data = data_table(1)  
    c12 = data.loc[12,["World"]]
    return list(c12)
def d1992(self):
     data = data_table(1)  
     d12 = data.loc[12,["Nam"]]
     return list(d12) 

def CounTries13(self):
    data = data_table(1)  
    c13 = data.loc[13,["World"]]
    return list(c13)
def d1993(self):
     data = data_table(1)  
     d13 = data.loc[13,["Nam"]]
     return list(d13) 

def CounTries14(self):
    data = data_table(1)  
    c14 = data.loc[14,["World"]]
    return list(c14)
def d1994(self):
     data = data_table(1)  
     d14 = data.loc[14,["Nam"]]
     return list(d14) 

def CounTries15(self):
    data = data_table(1)  
    c15 = data.loc[15,["World"]]
    return list(c15)
def d1995(self):
     data = data_table(1)  
     d15 = data.loc[15,["Nam"]]
     return list(d15) 

def CounTries16(self):
    data = data_table(1)  
    c16 = data.loc[16,["World"]]
    return list(c16)
def d1996(self):
     data = data_table(1)  
     d16 = data.loc[16,["Nam"]]
     return list(d16) 


def CounTries17(self):
    data = data_table(1)  
    c17 = data.loc[17,["World"]]
    return list(c17)
def d1997(self):
     data = data_table(1)  
     d17 = data.loc[17,["Nam"]]
     return list(d17) 


def CounTries18(self):
    data = data_table(1)  
    c18 = data.loc[18,["World"]]
    return list(c18)
def d1998(self):
     data = data_table(1)  
     d18 = data.loc[18,["Nam"]]
     return list(d18) 


def CounTries19(self):
    data = data_table(1)  
    c19 = data.loc[19,["World"]]
    return list(c19)
def d1999(self):
     data = data_table(1)  
     d19 = data.loc[19,["Nam"]]
     return list(d19) 

def CounTries20(self):
    data = data_table(1)  
    c20 = data.loc[20,["World"]]
    return list(c20)
def d2000(self):
     data = data_table(1)  
     d20 = data.loc[20,["Nam"]]
     return list(d20) 

def CounTries21(self):
    data = data_table(1)  
    c21 = data.loc[21,["World"]]
    return list(c21)
def d2001(self):
     data = data_table(1)  
     d21 = data.loc[21,["Nam"]]
     return list(d21) 

def CounTries22(self):
    data = data_table(1)  
    c22 = data.loc[22,["World"]]
    return list(c22)
def d2002(self):
     data = data_table(1)  
     d22 = data.loc[22,["Nam"]]
     return list(d22) 

def CounTries23(self):
    data = data_table(1)  
    c23 = data.loc[23,["World"]]
    return list(c23)
def d2003(self):
     data = data_table(1)  
     d23 = data.loc[23,["Nam"]]
     return list(d23) 

def CounTries24(self):
    data = data_table(1)  
    c24 = data.loc[24,["World"]]
    return list(c24)
def d2004(self):
     data = data_table(1)  
     d24 = data.loc[24,["Nam"]]
     return list(d24) 

def CounTries25(self):
    data = data_table(1)  
    c25 = data.loc[25,["World"]]
    return list(c25)
def d2005(self):
     data = data_table(1)  
     d25 = data.loc[25,["Nam"]]
     return list(d25) 

def CounTries26(self):
    data = data_table(1)  
    c26 = data.loc[26,["World"]]
    return list(c26)
def d2006(self):
     data = data_table(1)  
     d26 = data.loc[26,["Nam"]]
     return list(d26) 

def CounTries27(self):
    data = data_table(1)  
    c27 = data.loc[27,["World"]]
    return list(c27)
def d2007(self):
     data = data_table(1)  
     d27 = data.loc[27,["Nam"]]
     return list(d27) 

def CounTries28(self):
    data = data_table(1)  
    c28 = data.loc[28,["World"]]
    return list(c28)
def d2008(self):
     data = data_table(1)  
     d28 = data.loc[28,["Nam"]]
     return list(d28) 

def CounTries29(self):
    data = data_table(1)  
    c29 = data.loc[29,["World"]]
    return list(c29)
def d2009(self):
     data = data_table(1)  
     d29 = data.loc[29,["Nam"]]
     return list(d29) 

def CounTries30(self):
    data = data_table(1)  
    c30 = data.loc[30,["World"]]
    return list(c30)
def d2010(self):
     data = data_table(1)  
     d30 = data.loc[30,["Nam"]]
     return list(d30) 
##LINECHART
def World(self):
     data = data_table(1)
     dfWorld = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"World"]
     
     return list(dfWorld)
def Year(self):
     data = data_table(1)
     dfYear = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"Nam"]
     
     return list(dfYear)
def North_America(self):
     data = data_table(1)
     dfNA = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"North America"]
     return list(dfNA)
def Central_South_America(self):
     data = data_table(1)
     dfCSA = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"Central andSouth America"]
     return list(dfCSA)
def Europe(self):
     data = data_table(1)
     dfEorope = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"Europe"]
     return list(dfEorope)
def Eurasia(self):
     data = data_table(1)
     dfEurasia = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"Eurasia"]
     return list(dfEurasia)
def Middle_East(self):
     data = data_table(1)
     dfME = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"Middle East"]
     return list(dfME)
def Africa(self):
     data = data_table(1)
     dfA = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"Africa"]
     return list(dfA)
def Asia_Ocean(self):
     data = data_table(1)
     dfAO = data.loc[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"Asia and Oceania"]
     return list(dfAO)
##PIECHART
#dân sô các khu vực
def piedf1980(self):
    data = data_table1(1)  
    df1980 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff1980 =  data.loc[[0,7,52,94,111,126,183], "1980"]
    return list(df1980),list(dff1980)
def piedf1990(self):
    data = data_table1(1)  
    df1990 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff1990 =  data.loc[[0,7,52,94,111,126,183], "1990"]
    return list(df1990), list(dff1990)
def piedf2000(self):
    data = data_table1(1)  
    df2000 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff2000 =  data.loc[[0,7,52,94,111,126,183], "2000"]
    return list(df2000), list(dff2000)
def piedf2010(self):
    data = data_table1(1)  
    df2010 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff2010 =  data.loc[[0,7,52,94,111,126,183], "2010"]
    return list(df2010), list(dff2010)
#dân số các nước đông nam á
def dna1980(self):
     data = data_table1(1) 
     fdna1980 = data.loc[[189,190,191,199,204,206,216,218,222,223,227], "CounTries"]
     ffdna1980 = data.loc[[189,190,191,199,204,206,216,218,222,223,227], "1980"]
     return list(fdna1980), list(ffdna1980)
##BARCHART
def bardf1990(self):
    data = data_table1(1)  
    df1990 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff1990 =  data.loc[[0,7,52,94,111,126,183], "1990"]
    return list(df1990),list(dff1990)
def bardf1980(self):
    data = data_table1(1)
    df1980 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff1980 =  data.loc[[0,7,52,94,111,126,183], "1980"]
    return list(df1980),list(dff1980)
def bardf2000(self):
    data = data_table1(1)  
    df2000 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff2000 =  data.loc[[0,7,52,94,111,126,183], "2000"]
    return list(df2000),list(dff2000)
def bardf2010(self):
    data = data_table1(1)
    df2010 = data.loc[[0,7,52,94,111,126,183], "CounTries"]
    dff2010 =  data.loc[[0,7,52,94,111,126,183], "2010"]
    return list(df2010),list(dff2010)


# Create your views here.
User = get_user_model()
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bar_chart.html',{"customers": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100, 
        "customers": 10,
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
     authentication_classes = []
     permission_classes = []
     def get(self, request, format = None):
          data = {
               "sale": 100,
               "customers": 10,
               "user": User.objects.all().count()
          }
          return Response(data)

def index(request):
     return render(request, 'pages/base.html')
def data_analysis(request):
     return render(request, 'pages/data_analysis.html')
def simplechart(request):
     return render(request, 'pages/simplechart.html')
def base(request):
     return render(request, 'pages/base.html')
def home(request):
     return render(request, 'pages/home.html')
def bar_chart(request): 
     x1980,y1980 = bardf1980(1)
     x1990,y1990 = bardf1990(1)
     x2000,y2000 = bardf2000(1)
     x2010,y2010 = bardf2010(1)
     context=context={"x1980":x1980,'y1980':y1980,"x1990":x1990,'y1990':y1990,"x2000":x2000,'y2000':y2000,"x2010":x2010,'y2010':y2010}
     return render(request,'pages/bar_chart.html',context)
def line_chart(request):
     xYear = Year(1)
     yWorld = World(1)
     yNA = North_America(1)
     yCSA = Central_South_America(1)
     yEurope = Europe(1)
     yEurasia = Eurasia(1)
     yME = Middle_East(1)
     yA = Africa(1)
     yAO = Asia_Ocean(1)
     context = context = {"xYear": xYear, 'yWorld':yWorld, 'yNA':yNA, 'yCSA':yCSA, 'yEurope':yEurope, 'yEurasia':yEurasia, 'yME':yME, 'yA':yA, 'yAO':yAO}
     return render(request, 'pages/line_chart.html',context)
def scatter_chart(request):
     c0 = CounTries(1)
     d0 = d1980(1)
     c1 = CounTries1(1)
     d1 = d1981(1)
     c2 = CounTries2(1)
     d2 = d1982(1)
     c3 = CounTries3(1)
     d3 = d1983(1)
     c4 = CounTries4(1)
     d4 = d1984(1)
     c5 = CounTries5(1)
     d5 = d1985(1)
     c6 = CounTries6(1)
     d6 = d1986(1)
     c7 = CounTries7(1)
     d7 = d1987(1)
     c8 = CounTries8(1)
     d8 = d1988(1)
     c9 = CounTries9(1)
     d9 = d1989(1)
     c10 = CounTries10(1)
     d10 = d1990(1)
     c11 = CounTries11(1)
     d11 = d1991(1)
     c12 = CounTries12(1)
     d12 = d1992(1)
     c13 = CounTries13(1)
     d13 = d1993(1)
     c14 = CounTries14(1)
     d14 = d1994(1)
     c15 = CounTries15(1)
     d15 = d1995(1)
     c16 = CounTries16(1)
     d16 = d1996(1)
     c17 = CounTries17(1)
     d17 = d1997(1)
     c18 = CounTries18(1)
     d18 = d1998(1)
     c19 = CounTries19(1)
     d19 = d1999(1)
     c20 = CounTries20(1)
     d20 = d2000(1)
     c21 = CounTries21(1)
     d21 = d2001(1)
     c22 = CounTries22(1)
     d22 = d2002(1)
     c23 = CounTries23(1)
     d23 = d2003(1)
     c24 = CounTries24(1)
     d24 = d2004(1)
     c25 = CounTries25(1)
     d25 = d2005(1)
     c26 = CounTries26(1)
     d26 = d2006(1)
     c27 = CounTries27(1)
     d27 = d2007(1)
     c28 = CounTries28(1)
     d28 = d2008(1)
     c29 = CounTries29(1)
     d29 = d2009(1)
     c30 = CounTries30(1)
     d30 = d2010(1)
     context = context = {"c0":c0,'d0':d0,"c1":c1,'d1':d1,"c2":c2,'d2':d2,"c3":c3,'d3':d3,
                          "c4":c4,'d4':d4,"c5":c5,'d5':d5,"c6":c6,'d6':d6,"c7":c7,'d7':d7,
                          "c8":c8,'d8':d8,"c9":c9,'d9':d9,"c10":c10,'d10':d10,"c11":c11,'d11':d11,
                          "c12":c12,'d12':d12,"c13":c13,'d13':d13,"c14":c14,'d14':d14,"c15":c15,'d15':d15,
                          "c16":c16,'d16':d16,"c17":c17,'d17':d17,"c18":c18,'d18':d18,"c19":c19,'d19':d19,
                          "c20":c20,'d20':d20,"c21":c21,'d21':d21,"c22":c22,'d22':d22,"c23":c23,'d23':d23,
                           "c24":c24,'d24':d24,"c25":c25,'d25':d25,"c26":c26,'d26':d26,"c27":c27,'d27':d27,
                           "c28":c28,'d28':d28,"c29":c29,'d29':d29,"c30":c30,'d30':d30}
     return render(request, 'pages/scatter_chart.html',context)
def pie_chart(request):
     #dan số các khu vực 
     df1980, dff1980= piedf1980(1)
     df1990, dff1990 = piedf1990(1)
     df2000, dff2000 = piedf2000(1)
     df2010, dff2010 = piedf2010(1)
     #dân số các nước ĐNA 
     fdna1980, ffdna1980 = dna1980(1)
     context=context={"df1980":df1980,'dff1980':dff1980,"df1990":df1990,'dff1990':dff1990,"df2000":df2000,'dff2000':dff2000,"df2010":df2010,'dff2010':dff2010,
     "fdna1980":fdna1980,'ffdna1980':ffdna1980}
     return render(request, 'pages/pie_chart.html',context)
def gant_chart(request):
     return render(request, 'pages/gant_chart.html')     
