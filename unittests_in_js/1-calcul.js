module.exports = function calculateNumber(type, a, b) {
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
            const roundedB = Math.round(bNum);
            if (roundedB === 0) return 'Error';
            return Math.round(aNum) / roundedB;
        default:
            throw new Error('Invalid type');
    }
};