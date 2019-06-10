# Copyright (C) 2013 Yusuke Suzuki <utatane.tea@gmail.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'use strict'

expect = require('chai').expect
esutils = require '../'

KW = [
    'if'
    'in'
    'do'
    'var'
    'for'
    'new'
    'try'
    'this'
    'else'
    'case'
    'void'
    'with'
    'enum'
    'while'
    'break'
    'catch'
    'throw'
    'const'
    'class'
    'super'
    'return'
    'typeof'
    'delete'
    'switch'
    'export'
    'import'
    'default'
    'finally'
    'extends'
    'function'
    'continue'
    'debugger'
    'instanceof'
]

SRW = [
    'implements'
    'interface'
    'package'
    'private'
    'protected'
    'public'
    'static'
    'let'
]

describe 'keyword', ->
    describe 'isKeywordES6', ->
        it 'returns true if provided string is keyword under non-strict mode', ->
            for word in KW
                expect(esutils.keyword.isKeywordES6(word, no)).to.be.true

            expect(esutils.keyword.isKeywordES6('yield', no)).to.be.true

        it 'returns false if provided string is not keyword under non-strict mode', ->
            words = [
                'hello'
                '20'
                '$'
                'ゆゆ式'
            ]

            for word in words
                expect(esutils.keyword.isKeywordES6(word, no)).to.be.false

            for word in SRW
                expect(esutils.keyword.isKeywordES6(word, no)).to.be.false

        it 'returns true if provided string is keyword under strict mode', ->
            for word in KW
                expect(esutils.keyword.isKeywordES6(word, yes)).to.be.true

            expect(esutils.keyword.isKeywordES6('yield', yes)).to.be.true

            for word in SRW
                expect(esutils.keyword.isKeywordES6(word, yes)).to.be.true


        it 'returns false if provided string is not keyword under strict mode', ->
            words = [
                'hello'
                '20'
                '$'
                'ゆゆ式'
            ]

            for word in words
                expect(esutils.keyword.isKeywordES6(word, yes)).to.be.false

    describe 'isKeywordES5', ->
        it 'returns true if provided string is keyword under non-strict mode', ->
            for word in KW
                expect(esutils.keyword.isKeywordES5(word, no)).to.be.true

        it 'returns false if provided string is not keyword under non-strict mode', ->
            words = [
                'hello'
                '20'
                '$'
                'ゆゆ式'
            ]

            for word in words
                expect(esutils.keyword.isKeywordES5(word, no)).to.be.false

            for word in SRW
                expect(esutils.keyword.isKeywordES5(word, no)).to.be.false

            expect(esutils.keyword.isKeywordES5('yield', no)).to.be.false

        it 'returns true if provided string is keyword under strict mode', ->
            for word in KW
                expect(esutils.keyword.isKeywordES5(word, yes)).to.be.true

            expect(esutils.keyword.isKeywordES5('yield', yes)).to.be.true

            for word in SRW
                expect(esutils.keyword.isKeywordES5(word, yes)).to.be.true


        it 'returns false if provided string is not keyword under strict mode', ->
            words = [
                'hello'
                '20'
                '$'
                'ゆゆ式'
            ]

            for word in words
                expect(esutils.keyword.isKeywordES5(word, yes)).to.be.false

    describe 'isRestrictedWord', ->
        it 'returns true if provided string is "eval" or "arguments"', ->
            expect(esutils.keyword.isRestrictedWord('eval')).to.be.true
            expect(esutils.keyword.isRestrictedWord('arguments')).to.be.true

        it 'returns false if provided string is not "eval" or "arguments"', ->
            words = [
                'hello'
                '20'
                '$'
                'ゆゆ式'
            ]

            for word in words
                expect(esutils.keyword.isRestrictedWord(word)).to.be.false


    describe 'isIdentifierName', ->
        it 'returns false if provided string is empty', ->
            expect(esutils.keyword.isIdentifierName('')).to.be.false

        it 'returns true if provided string is IdentifierName', ->
            words = [
                'hello'
                '$'
                'ゆゆ式'
                '$20'
                'hello20'
                '_'
            ]

            for word in words
                expect(esutils.keyword.isIdentifierName(word)).to.be.true


        it 'returns false if provided string is not IdentifierName', ->
            words = [
                '+hello'
                '0$'
                '-ゆゆ式'
                '#_'
            ]

            for word in words
                expect(esutils.keyword.isIdentifierName(word)).to.be.false
