# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
def account():
    if request.args:
        acc_id = request.args[0]
        rows = db((db.transfer.from_acc == acc_id) | (db.transfer.to_acc == acc_id)).select()
        return dict(rows = rows,acc_id=acc_id)
    
    
def accounts():
    rows = db(db.account.id > 0).select()
    return dict(rows=rows)


def create_transaction():
    form = SQLFORM(db.transfer)
    if form.process().accepted:
        amount = int(request.vars.amount)
        account_to = db(db.account.id == request.vars.to_acc).select().first()
        account_from = db(db.account.id == request.vars.from_acc).select().first()
        account_to.balance =  account_to.balance + amount
        account_from.balance =  account_from.balance - amount
        account_to.update_record()
        account_from.update_record()
        session.flash = 'form accepted'
        redirect(URL())
    return dict(form=form)

def create_account():
    form = SQLFORM(db.account)
    if form.process().accepted:
        session.flash = 'form accepted'
        redirect(URL('accounts'))

    return dict(form = form)

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
