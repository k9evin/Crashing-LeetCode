// Last updated: 12/29/2025, 1:40:16 AM
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function (fn, t) {
    let timeoutId = null;
    let nextTimeToCallFn = 0;

    return function (...args) {
        // update the delayed time to call the previous function
        const delay = Math.max(0, nextTimeToCallFn - Date.now());

        // clear the existing timeout to ensure only one timeout is running at a given time
        clearTimeout(timeoutId);

        // set a new timeout, invoke the function, and update the nextTimetoCallFn
        timeoutId = setTimeout(() => {
            fn.apply(this, args);
            nextTimeToCallFn = Date.now() + t;
        }, delay);
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */