const assert = require('assert');
const calculateNumber = require('./1-calcul');

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

        
});