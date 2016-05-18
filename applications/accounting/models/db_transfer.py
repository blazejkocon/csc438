# -*- coding: utf-8 -*-
db.define_table('accounttransfer',
                Field('tranfser_date',type="datetime", requires=IS_NOT_EMPTY()),
                Field('amount',type ="float", requires= IS_NOT_EMPTY()),
                Field('description',type="string", requires=IS_NOT_EMPTY()),
                Field('account_from',type="string", requires=IS_NOT_EMPTY()),
                Field('account_to',type="string", requires=IS_NOT_EMPTY()))
