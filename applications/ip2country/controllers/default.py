# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
def tables():
    return repr(db.tables)

def table():
    return db[request.args(0)].select().as_json()


def mycountryform():
    
    from gluon import *
    import struct
    import socket
    form=FORM('ip', INPUT(_name='ip'), INPUT(_type='submit'))
    if form.process().accepted:
        try:
            ip = struct.unpack("!I", socket.inet_aton(request.vars.values()[0]))[0]
            country = db.executesql('SELECT c.country FROM ip2nationCountries c, ip2nation i WHERE i.code < ? AND c.code = i.country ORDER BY i.code DESC LIMIT 0,1;',(ip,))
            form.vars = str(country[0][0]).rstrip()[2:-1]
        except:
            response.flash = "invalid IP address"
        
    return dict(form=form,vars=form.vars)

def mycountry():
    from gluon import *
    import struct
    import socket
    ip = struct.unpack("!I", socket.inet_aton(current.request.client))[0]
    r = db.executesql('SELECT c.country FROM ip2nationCountries c, ip2nation i WHERE i.code < ? AND c.code = i.country ORDER BY i.code DESC LIMIT 0,1;',(ip,))
    return str(r[0][0]).rstrip()[2:-1]


def myip():
   from gluon import *
   return current.request.client
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
