module.exports = function calculateNumber(a, b = 0) {
    const aNum = number(a);
    const bNum = number(b);

    if (Number.isNaN(aNum) || Number.isNaN(bNum)) {
        throw new TypeError('Parameters must be numbers');
    }

    return Math.round(aNum) + Math.round(bNum);
};