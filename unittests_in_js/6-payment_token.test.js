const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('returns a promise that resolves with the correct value when success is true', (done) => {
      getPaymentTokenFromAPI(true).then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done();
      }).catch(done);
    });
  });