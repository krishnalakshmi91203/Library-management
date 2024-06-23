from flask import *
import jinja2
import dbase as db
from datetime import date
import os

def delete_pdf(filename):
      filepath = os.path.join(app.root_path, 'static', filename)
      if os.path.exists(filepath):
            os.remove(filepath)
            
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
      if request.method=="POST":
            a=request.form.get('form')
            if a=='libform':
                  if (request.form.get("libdas")=="libdas"):
                        return redirect(url_for('/librarian_dashboard'))
                  return render_template('libr.html')
      return render_template('home.html')

@app.route('/userlogin',methods=['GET','POST'])
def user():
      if (request.form.get("userreq")=="das"):
                        a1=request.form.get('uname')
                        a2=request.form.get('pwd')
                        k=db.userchk(a1,a2)
                        if k!=[]:
                              t=f"/user_dashboard/{a1}"
                              return redirect(t)
      return render_template('user.html')

@app.route('/librarian_dashboard',methods=['GET','POST'])
def libr():
      if (request.method=="POST") :
            a3=request.form.get('name')
            a4=request.form.get('search')
            a1=request.form.get('form')
            if a1:
                  k=db.delesec(a1)
                  for i in k:
                       delete_pdf(i[0]) 
            if request.form.get('same')=="search1":
                  return render_template('libdash.html',k=db.fun(0,[a3,a4]))
      return render_template('libdash.html',k=db.fun(0,0))

@app.route('/<section_id>/books',methods=['GET','POST'])
def books(section_id):
      if (request.method=="POST") :
            a3=request.form.get('name')
            a4=request.form.get('search')
            a1=request.form.get('form')
            if a1:
                  k=db.delebook(a1)
                  for i in k:
                       delete_pdf(i[0]) 
            if request.form.get('same')=="search1":
                  (k,b)=db.fun1(section_id,[a3,a4])
                  return render_template('libdashbook.html',k=k,b=b,a=section_id)
      (k,b)=db.fun1(section_id,0)
      return render_template('libdashbook.html',k=k,b=b,a=section_id)

@app.route('/sectionform/<req>',methods=['GET','POST'])
def sectionform(req):
      if str(req)=="new":
            a1=request.form.get('title')
            a2=date.today()
            a3=request.form.get('desc')
            if (request.form.get("libdas")=="j"):
                  db.addsection(a1,a2,a3)
                  return redirect(url_for('libr'))
            return render_template('sectionform.html',aa=str(req),a=a2)
      else:
            k=db.fun2(int(req),0)
            a1=request.form.get('title')
            a2=request.form.get('date')
            a3=request.form.get('desc')
            if (request.form.get("libdas")=="j"):
                  db.update(a1,a2,a3,req,0,0,0)
                  return redirect(url_for('libr'))
            return render_template('sectionform.html',aa=req,aa1=k[0],aa2=k[1],aa3=k[2])
      
@app.route('/<section_name>/bookform/<req>',methods=['GET','POST'])
def bookform(section_name,req):
      b2=db.fun(section_name,0)
      if req == "new":
              if request.method == "POST":
                  a1 = request.form.get('title')
                  a3 = request.form.get('auth')
                  a2 = request.files.get("content")
                  a4 = request.form.get('price')
                  if request.method == "POST" and request.form.get('libdas') == 'j':
                      if a2:
                            e = a2.filename
                            t = f"static/{e}"
                            a2.save(t)
                            a2 = e
                      db.addbook(a1, a2, a3, section_name, a4)
                      (k, b1) = db.fun1(b2[0][0], 0)
                      return render_template('libdashbook.html', k=k, b=b1)
              return render_template('bookform.html', b=b2[0][0], a=section_name, aa=req)
      else:
          k = db.fun2(int(req), 1)
          a1 = request.form.get('title')
          a2 = request.form.get('auth')
          a3 = request.files.get("content")
          a4 = request.form.get('price')
          if request.method == "POST" and request.form.get('libdas') == 'j':
              if a3:
                    e = a3.filename
                    t = f"static/{e}"
                    a3.save(t)
                    a3 = e
              db.update(a1, a2, a3, section_name, 1, req, a4)
              k1, b1 = db.fun1(b2[0][0], 0)
              return render_template('libdashbook.html', k=k1, b=b1)
          return render_template('bookform.html', b=b2[0][0], a=section_name, aa=req, aa1=k[0], aa2=k[1], aa3=k[2], aa4=k[3])

@app.route('/user_dashboard/<uname>',methods=['GET','POST'])
def usdash(uname):
      a3=request.form.get('name')
      a4=request.form.get('search')
      a1=request.form.get('book')
      if a1!=None:
            if db.chk(uname):
                  db.req(int(a1),uname)
            t=f'/user_dashboard/{uname}'
            return redirect(t)
      if request.form.get('same')=="search1":
            k=db.search(a3,a4,uname)
            return render_template('usdash.html',k=k,a=uname)
      return render_template('usdash.html',k=db.userdash(uname),a=uname)

@app.route('/user_dashboard/<uname>/mybook',methods=['GET','POST'])
def usreq(uname):
      a1=db.userreq(uname,'request')
      a2=db.userreq(uname,'granted')
      a3=db.userreq(uname,'completed')
      a4=request.form.get('select')
      a5=request.form.get('sub')
      if a5=='i':
            a6=request.form.get('book')
            a7=request.form.get('rate')            
            db.uprate(a6,a7)
            f=f'/user_dashboard/{uname}/mybook'
            return redirect(f)
      if a4:
            db.revoke(int(a4),uname)
            f=f'/user_dashboard/{uname}/mybook'
            return redirect(f)
      return render_template('usmybook.html',k1=a1,k2=a2,k3=a3,a=uname)

@app.route('/Registerform/<req>',methods=['GET','POST'])
def regform(req):
      if str(req)=='new':
            a1=request.form.get('name')
            a2=request.form.get('role')
            a3=request.form.get('uname')
            a4=request.form.get('pwd')
            a6=request.form.get('email')
            a5=request.form.get('num')
            if request.form.get('sub')=='j':
                  db.adduser(a1,a2,a3,a4,a5,a6)
                  return redirect('/userlogin')
            return render_template('regform.html',aa=req)
      else:
            a1=request.form.get('name')
            a2=request.form.get('role')
            a3=request.form.get('uname')
            a4=request.form.get('pwd')
            a6=request.form.get('email')
            a5=request.form.get('num')
            if request.form.get('sub')=='j':
                  db.deluser(req)
                  db.adduser(a1,a2,a3,a4,a5,a6)
                  t=f'/user_dashboard/{a3}'
                  return redirect(t)
            return render_template('regform.html',aa=req,k=db.userdetail(req))
      
@app.route('/librarian_dashboard/status',methods=['GET','POST'])
def libstatus():
      a3=request.form.get('grant')
      a4=request.form.get('grant1')
      if a3:
            a3=a3.split(',')
            db.libchoice(int(a3[0]),str(a3[1]))
            return redirect('/librarian_dashboard/status')
      if a4:
            a4=a4.split(',')
            db.reject(int(a4[0]),str(a4[1]))
            return redirect('/librarian_dashboard/status')
      a3=request.form.get('revoke')
      if a3!=None:
            a3=a3.split(',')
            db.revoke(int(a3[0]),str(a3[1]))
            return redirect('/librarian_dashboard/status')
      a1=db.libreq("request")
      a2=db.libreq("granted")
      return render_template('libstatus.html',k1=a1,k2=a2)

@app.route('/<uname>/profile',methods=['GET','POST'])
def profile(uname):
      return render_template('profile.html',a=uname,k=db.userdetail(uname))
@app.route('/<uname>/user_detail',methods=['GET','POST'])
def userdet(uname):
      k,k1=db.bookdet(uname)
      return render_template('userdet.html',a=uname,k=k,k1=k1)
@app.route('/<bookid>/status',methods=['GET','POST'])
def bookstat(bookid):
      k,k1,k2,k3=db.bookstat(int(bookid))
      return render_template('bookstat.html',a=bookid,k=k,k1=k1,k2=k2,k3=k3)

if __name__ == '__main__':
   db.default()
   app.run(debug=True)
