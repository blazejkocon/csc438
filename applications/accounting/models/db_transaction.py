# -*- coding: utf-8 -*-
db.define_table('transfer',
                Field('tranfser_date',type="datetime", requires=IS_NOT_EMPTY()),
                Field('amount',type ="integer", requires= IS_NOT_EMPTY()),
                Field('description',type="string", requires=IS_NOT_EMPTY()),
                Field('account_from',type="string", requires=IS_NOT_EMPTY()),
                Field('account_to',type="string", requires=IS_NOT_EMPTY()))