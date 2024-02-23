ea=str(input("ඔයගෙ නම කියන්නකො:-"))
print("කොහොමද ඉතින් "+a+"!")
g=0
b=1
t=[]
while(b==1):
    c=str(input("OOOO :-"))
    if(c=="oyage nama mokadda"):
        print("tikiri")
    elif(c=="tikiri"):
        print("කියන්න "+a)
    elif(c=="oyage wayasa kiyada"):
        print("අනේ මං දැන් ටිකකට කලින්නෙ ඉපදුනෙ")
    elif(c=="oyagen mata karaganna puluwan weda monada" or c=="oyata monada karanna puluwan"):
        print("මට පුලුවන් ඔයාව හිනස්සන්න"+"\n"+"මට ඔව තමයි තම පුලුවන් මං තම චුටිනේ"+"\n"+"මං ලොකු උනම මාත් ලොකු ලොකු වැඩ ඉගෙන ගන්නන්කො"+"\n"+"දැනට මට පුලුවන් මෙව තමා  ඉතින් ")
    elif(c=="ehenan mawa hinassanna balanna" or c=="mata wihiluwak kiyanna"):
        g=g+1
        if(g==1):
            print("හිස් බඩ බිත්තර කියක් ගිලින්න පුලුවද"+"\n"+"1යි"+"\n"+"එයි එක බිත්තරයක් ගිල්ලම එක හිස් බඩ වෙන්නැනෙ")
        elif(g==2):
            print("ඔන්න දවසක් පිස්සෙක් අයිස් කැටයක් අතේ තියන් ඉන්නව ඩොකෙක් දැක්කලු"+"\n"+"ඩොකා:-සිරිවර්දන මොනවද ඔය අයිස් කැටයක් අතේ තියගෙන කරන්නෙ"+"\n"+"පිස්ස:-නැ ඩොක්ට මං මෙ බැලුවෙ මෙ අයිස් කැටෙන් වතුර ලික් වෙන්නෙ කොහෙන්ද කියලා")
        elif(g==3):
            print("හුනා කවදවත් නැට්ට කඩන්නැ එ අලුත් හාඩ් එක මරු කරන්න පොට් එක සුද්ද කරන්නෙ ")
        elif(g==4):
            print("බුරුව කියන්නෙ බුද්දිමත් රුමත් වසනා වන්තයින්ට")
        elif(g==5):
            print("හීඊඊඊඊඊඊඊ")
        elif(g==6):
            print("හූඌඌඌඌඌඌඌඌඌ")
        else:
            print("අනේ මං එච්චර විහිලු දන්නැ දන්න ටික තම මෙ")
    elif(c=="oya monatada asa"):
        print("මම ආස ඔය ගොඩක් ප්රශ්න අහනවට")
    else:
        import mysql.connector
        x=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="tikiri"
        )
        y=x.cursor()
        sql="select anka from daththa"
        y.execute(sql)
        h=y.fetchall()
        for cv in h:
            bo=str(cv)
            uo=int(bo[1:-2])
            t.append(uo)
        t.sort(reverse=True)
        o=t[0]
        o=o+1
        y=x.cursor()
        sql="select prashna from daththa"
        y.execute(sql)
        h=y.fetchall()
        
        for k in h:
            ji=str(k)
            fo=ji[2:-3]
            if(c==fo):
                y=x.cursor()
                sql="select uththara from daththa where prashna='"+c+"'"
                y.execute(sql)
                h=y.fetchall()
                for l in h:
                    jiw=str(l)
                    fio=jiw[2:-3]
                    print(fio)
        y=x.cursor()
        sql="select * from daththa WHERE prashna='"+c+"'"
        y.execute(sql)
        h=y.fetchall()
        ko=str(h)
        if(ko=="[]"):
            print("අනේ මම මේකට උත්තරය දන්නැනෙ"+"\n"+"අනේ මට මෙ ප්රශ්නෙට උත්තර දෙන හැටි කියල දෙන්නකො"+"\n"+"ඔයා දන්නෙත් නැත්තන් දන්නෙ කියල කියන්න කමක් නැ")
            fi=input("උත්තරය කියන්නකො:-")
            y=x.cursor()
            sql="INSERT INTO `daththa`(anka,prashna,uththara) VALUES (%s,%s,%s)"
            val=(o,c,fi)
            y.execute(sql,val)
            x.commit()
            print(y.rowcount,"ha")
