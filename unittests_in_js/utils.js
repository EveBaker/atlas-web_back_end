const Utils = {
    calculateNumber(type, a, b = 0) {
      const aNum = Number(a);
      const bNum = Number(b);
  
      if (Number.isNaN(aNum) || Number.isNaN(bNum)) {
        throw new TypeError('Parameters must be numbers');
      }
  
      switch (type) {
        case 'SUM':
          return Math.round(aNum) + Math.round(bNum);
        case 'SUBTRACT':
          return Math.round(aNum) - Math.round(bNum);
        case 'DIVIDE':
          if (bNum === 0) {
            return 'Error';
          }
          return Math.round(aNum) / Math.round(bNum);
        default:
          throw new Error('Invalid type');
      }
    },
  };
  
  module.exports = Utils;