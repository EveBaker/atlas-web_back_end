const assert = require('assert');
const calculateNumber = require('./1-calcul');
const mocha = require('mocha');

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should return the sum of rounded numbers', () => {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        });
    });

        describe('SUBTRACT', () => {
            it('it should return the diffrence between rounded numbers', () => {
                assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
            });
        });

        describe('DIVIDE', function() {
            it('should return the quotient of rounded numbers', () => {
                assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
            });

        it('should return "Error" when attempting to divide by zero', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        });
        });

        describe('Edge cases and type validation', () => {
            it('should throw TypeError for non-numeric values', () => {
            assert.throws(() => calculateNumber('SUM', 'hello', 2), {
                name: 'TypeError',
                message: 'Parameters must be numbers'
            });
            });

            it('should throw Error for invalid type', () => {
                assert.throws(() => calculateNumber('MULTIPLY', 1, 2), {
                name: 'Error',
                message: 'Invalid type'
                });
            });
            });
        });