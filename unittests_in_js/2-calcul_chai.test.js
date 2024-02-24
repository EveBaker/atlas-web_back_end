const assert = require('assert');
const calculateNumber = require('./2-calcul_chai');
const expect = require('chai').expect;

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should return the sum of rounded numbers', () => {
            expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        });
    });

        describe('SUBTRACT', () => {
            it('it should return the diffrence between rounded numbers', () => {
                expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
            });
        });

        describe('DIVIDE', () => {
            it('should return the quotient of rounded numbers', () => {
                expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
            });

        it('should return "Error" when attempting to divide by zero', () => {
            expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
        });
        });

        describe('Edge cases and type validation', () => {
            it('should throw TypeError for non-numeric values', () => {
                expect(() => calculateNumber('SUM', 'hello', 2)).to.throw(TypeError, 'Parameters must be numbers');
            });

            it('should throw Error for invalid type', () => {
                expect(() => calculateNumber('MULTIPLY', 1, 2)).to.throw(Error, 'Invalid type');
            });
            });
        });