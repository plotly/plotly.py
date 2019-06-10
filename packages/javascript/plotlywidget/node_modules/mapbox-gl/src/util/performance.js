// @flow

// Wraps performance.getEntriesByName to facilitate testing
// Not incorporated into browser.js because the latter is poisonous when used outside the main thread
const exported = {
    getEntriesByName: (url: string) => {
        if (performance && performance.getEntriesByName)
            return performance.getEntriesByName(url);
        else
            return false;
    }
};

export default exported;
