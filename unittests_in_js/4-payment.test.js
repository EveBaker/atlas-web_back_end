const { expect } = require('chai');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call calculateNumber and log the correct total', () => {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.equal(true);

    stub.restore();
    consoleSpy.restore();
});
});
