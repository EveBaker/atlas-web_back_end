const assert = require('assert');
const calculateNumber = require('/0-calcul');
const mocha = require('mocha');

describe('calculateNumber', () => {
    it('should return the sum of two rounded numbers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(-1.5, 2.1), 1); // -1 + 2
    });
});