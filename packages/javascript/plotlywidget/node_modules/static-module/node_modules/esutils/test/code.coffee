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

describe 'code', ->
    describe 'isDecimalDigit', ->
        it 'returns true if provided code is decimal digit', ->
            for ch in [0..9]
                expect(esutils.code.isDecimalDigit((ch + '').charCodeAt(0))).to.be.true

        it 'returns false if provided code is not decimal digit', ->
            for code in ['a'.charCodeAt(0)..'z'.charCodeAt(0)]
                expect(esutils.code.isDecimalDigit(code)).to.be.false

            for code in ['A'.charCodeAt(0)..'Z'.charCodeAt(0)]
                expect(esutils.code.isDecimalDigit(code)).to.be.false

    describe 'isHexDigit', ->
        it 'returns true if provided code is hexadecimal digit', ->
            for ch in [0..9]
                expect(esutils.code.isHexDigit((ch + '').charCodeAt(0))).to.be.true

            for code in ['a'.charCodeAt(0)..'f'.charCodeAt(0)]
                expect(esutils.code.isHexDigit(code)).to.be.true

            for code in ['A'.charCodeAt(0)..'F'.charCodeAt(0)]
                expect(esutils.code.isHexDigit(code)).to.be.true

        it 'returns false if provided code is not hexadecimal digit', ->
            for code in ['g'.charCodeAt(0)..'z'.charCodeAt(0)]
                expect(esutils.code.isHexDigit(code)).to.be.false

            for code in ['G'.charCodeAt(0)..'Z'.charCodeAt(0)]
                expect(esutils.code.isHexDigit(code)).to.be.false

    describe 'isOctalDigit', ->
        it 'returns true if provided code is octal digit', ->
            for ch in [0..7]
                expect(esutils.code.isOctalDigit((ch + '').charCodeAt(0))).to.be.true

        it 'returns false if provided code is not octal digit', ->
            for ch in [8..9]
                expect(esutils.code.isOctalDigit((ch + '').charCodeAt(0))).to.be.false

            for code in ['a'.charCodeAt(0)..'z'.charCodeAt(0)]
                expect(esutils.code.isOctalDigit(code)).to.be.false

            for code in ['A'.charCodeAt(0)..'Z'.charCodeAt(0)]
                expect(esutils.code.isOctalDigit(code)).to.be.false

    describe 'isWhiteSpace', ->
        it 'returns true if provided code is white space', ->
            codes = [
                0x0009  # TAB
                0x000B  # VT
                0x000C  # FF
                0x0020  # SP
                0x00A0  # NBSP
                0xFEFF  # BOM

                # Zs
                0x1680
                0x180E
                0x2000
                0x2001
                0x2002
                0x2003
                0x2004
                0x2005
                0x2006
                0x2007
                0x2008
                0x2009
                0x200A
                0x202F
                0x205F
                0x3000
            ]
            for code in codes
                expect(esutils.code.isWhiteSpace(code)).to.be.true

        it 'returns false if provided code is not white space', ->
            for ch in [0..9]
                expect(esutils.code.isWhiteSpace((ch + '').charCodeAt(0))).to.be.false

            for code in ['a'.charCodeAt(0)..'z'.charCodeAt(0)]
                expect(esutils.code.isWhiteSpace(code)).to.be.false

            for code in ['A'.charCodeAt(0)..'Z'.charCodeAt(0)]
                expect(esutils.code.isWhiteSpace(code)).to.be.false

    describe 'isLineTerminator', ->
        it 'returns true if provided code is line terminator', ->
            codes = [
                0x000A
                0x000D
                0x2028
                0x2029
            ]
            for code in codes
                expect(esutils.code.isLineTerminator(code)).to.be.true

        it 'returns false if provided code is not line terminator', ->
            for ch in [0..9]
                expect(esutils.code.isLineTerminator((ch + '').charCodeAt(0))).to.be.false

            for code in ['a'.charCodeAt(0)..'z'.charCodeAt(0)]
                expect(esutils.code.isLineTerminator(code)).to.be.false

            for code in ['A'.charCodeAt(0)..'Z'.charCodeAt(0)]
                expect(esutils.code.isLineTerminator(code)).to.be.false

    describe 'isIdentifierStart', ->
        it 'returns true if provided code can be a start of Identifier', ->
            characters = [
                'a'
                '$'
                '_'
                'ゆ'
            ]
            for code in characters.map((ch) -> ch.charCodeAt(0))
                expect(esutils.code.isIdentifierStart(code)).to.be.true

        it 'returns false if provided code cannot be a start of Identifier', ->
            for ch in [0..9]
                expect(esutils.code.isIdentifierStart((ch + '').charCodeAt(0))).to.be.false

    describe 'isIdentifierPart', ->
        it 'returns true if provided code can be a part of Identifier', ->
            characters = [
                'a'
                '_'
                '$'
                'ゆ'
            ]
            for code in characters.map((ch) -> ch.charCodeAt(0))
                expect(esutils.code.isIdentifierPart(code)).to.be.true

            for ch in [0..9]
                expect(esutils.code.isIdentifierPart((ch + '').charCodeAt(0))).to.be.true

        it 'returns false if provided code cannot be a part of Identifier', ->
            expect(esutils.code.isIdentifierPart('+'.charCodeAt(0))).to.be.false
            expect(esutils.code.isIdentifierPart('-'.charCodeAt(0))).to.be.false
