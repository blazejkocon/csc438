# -*- coding: utf-8 -*-
db.define_table('transfer',
                Field('transferdate',type="datetime"),
                Field('amount',type ="float", requires= IS_NOT_EMPTY()),
                Field('description',type="string", requires=IS_NOT_EMPTY()),
                Field('from_acc',type="string", requires=IS_NOT_EMPTY()),
                Field('to_acc',type="string", requires=IS_NOT_EMPTY()))
