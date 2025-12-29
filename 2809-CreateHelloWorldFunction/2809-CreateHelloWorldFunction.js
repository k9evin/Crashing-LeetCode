// Last updated: 12/29/2025, 1:40:14 AM
/**
 * @return {Function}
 */
var createHelloWorld = function () {

    return function (...args) {
        return "Hello World";
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */