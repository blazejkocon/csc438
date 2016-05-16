# -*- coding: utf-8 -*-
db.define_table('account',
                Field('name',type='string', requires=IS_NOT_EMPTY()),
                Field('balance',type='integer', requires= IS_NOT_EMPTY()))
