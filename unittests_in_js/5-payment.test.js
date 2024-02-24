const sinon = require('sinon');
const { expect, should } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
let consoleSpy;

beforeEach(() => {
    spy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('should log "the total is: 120" when called with 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.be.true;
    expect(consoleSpy.calledOnce).to.be.true;
  });

  it('should log "The total is: 20" when called with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledWithExactly('The total is 20')).to.be.true;
    expect(consoleSpy.calledOnce).to.be.true;
  });
});
