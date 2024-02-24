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

        describe('DIVIDE', () => {
            it('should return the quotient of rounded numbers', () => {
                assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 0.2);
        });

        it('should return "Error" when attempting to divide by zero', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        });
        });
        
    });